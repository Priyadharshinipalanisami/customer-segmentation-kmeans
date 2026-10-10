"""
Customer Segmentation with K-Means
Run: python customer_segmentation.py
Input: Mall_Customers.csv in the same folder (or edit INPUT_FILE).
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

INPUT_FILE = "Mall_Customers.csv"
OUTPUT_DIR = "outputs"
FEATURES = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
CHOSEN_K = 5

os.makedirs(OUTPUT_DIR, exist_ok=True)
df = pd.read_csv(INPUT_FILE)
df.columns = [c.strip() for c in df.columns]
df = df.drop_duplicates().copy()
for col in FEATURES:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=FEATURES).copy()
if "Gender" in df.columns:
    df["Gender"] = df["Gender"].astype(str).str.strip().str.title()

scaler = StandardScaler()
X = scaler.fit_transform(df[FEATURES])

ks = list(range(2, 11))
inertias, silhouettes = [], []
for k in ks:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = km.fit_predict(X)
    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X, labels))

plt.figure(figsize=(8, 5))
plt.plot(ks, inertias, marker="o")
plt.title("Elbow Method for K-Means")
plt.xlabel("Number of clusters (k)")
plt.ylabel("Inertia")
plt.xticks(ks)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "elbow_method.png"), dpi=160)
plt.close()

model = KMeans(n_clusters=CHOSEN_K, random_state=42, n_init=10)
df["Cluster"] = model.fit_predict(X)
df.to_csv(os.path.join(OUTPUT_DIR, "customer_clusters.csv"), index=False)

agg = {
    "Customers": ("Cluster", "size"),
    "Avg_Age": ("Age", "mean"),
    "Avg_Annual_Income_k": ("Annual Income (k$)", "mean"),
    "Avg_Spending_Score": ("Spending Score (1-100)", "mean"),
}
if "Gender" in df.columns:
    agg["Female_Percent"] = ("Gender", lambda s: (s.str.lower() == "female").mean() * 100)
profile = df.groupby("Cluster").agg(**agg).round(2).reset_index()
profile.to_csv(os.path.join(OUTPUT_DIR, "cluster_profile_report.csv"), index=False)

plt.figure(figsize=(8, 5.5))
for cl in sorted(df["Cluster"].unique()):
    part = df[df["Cluster"] == cl]
    plt.scatter(part["Age"], part["Spending Score (1-100)"], label=f"Cluster {cl}", alpha=0.75)
plt.title("Customer Clusters: Age vs Spending Score")
plt.xlabel("Age")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "customer_clusters_age_spending.png"), dpi=160)
plt.close()

print("Cluster profiles:")
print(profile.to_string(index=False))
print(f"\nSilhouette score (k={CHOSEN_K}): {silhouette_score(X, df['Cluster']):.3f}")
print(f"Saved outputs to: {OUTPUT_DIR}")
