# Customer Segmentation Using K-Means Clustering

## Project Overview
This project uses machine learning to group customers into meaningful segments based on age, annual income, and spending score. It applies the K-Means clustering algorithm to the Mall Customers dataset and produces visualizations, cluster labels, and a short profile report for each segment.

## Objectives
- Clean and preprocess customer data.
- Scale numerical features using `StandardScaler`.
- Use the Elbow Method to inspect a suitable number of clusters.
- Apply K-Means clustering.
- Visualize clusters using scatter plots.
- Profile customer groups and suggest marketing actions.
- Save customer cluster labels and cluster summary reports as CSV files.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Project Structure
```text
Customer-Segmentation/
├── Mall_Customers.csv
├── customer_segmentation.py
├── requirements.txt
├── README.md
└── outputs/
    ├── customer_clusters.csv
    ├── cluster_profile_report.csv
    ├── elbow_method.png
    └── customer_clusters_age_spending.png
```

## Dataset
The Mall Customers dataset includes:
- `CustomerID`: Customer identifier (excluded from clustering)
- `Gender`: Customer gender
- `Age`: Customer age
- `Annual Income (k$)`: Annual income in thousands of dollars
- `Spending Score (1-100)`: Spending behavior score

## Methodology
1. **Data cleaning:** remove duplicate rows, convert numeric columns, and remove records missing required clustering features.
2. **Feature scaling:** standardize Age, Annual Income, and Spending Score using `StandardScaler`.
3. **Elbow Method:** fit models for several values of K and plot inertia to help choose the number of clusters.
4. **K-Means:** assign each customer a cluster label. The provided script uses `k=5` as an initial segmentation choice.
5. **Visualization:** generate an elbow plot and a scatter plot of age versus spending score.
6. **Cluster profiling:** calculate customer count and average age, income, and spending score; include gender distribution when available.
7. **Marketing actions:** interpret each profile to propose segment-specific marketing ideas.

## Installation and Usage

### 1. Clone the repository
Replace `YOUR-USERNAME` with your GitHub username.
```bash
git clone https://github.com/YOUR-USERNAME/customer-segmentation-kmeans.git
cd customer-segmentation-kmeans
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the project
Keep `Mall_Customers.csv` in the project root, then run:
```bash
python customer_segmentation.py
```

The script creates an `outputs/` folder containing the generated CSV reports and charts.

## Output Files
| File | Description |
|---|---|
| `customer_clusters.csv` | Dataset with an assigned cluster label for each customer |
| `cluster_profile_report.csv` | Summary statistics for each cluster |
| `elbow_method.png` | Elbow curve used to inspect candidate K values |
| `customer_clusters_age_spending.png` | Scatter plot of customer age versus spending score |

## Example Marketing Strategies
- **High income and high spending:** loyalty rewards, premium bundles, and personalized recommendations.
- **High income and low spending:** curated product suggestions and value-focused offers.
- **Lower income and high spending:** affordable bundles and points-based rewards.
- **Lower income and low spending:** budget-friendly products and carefully tested promotions.
- **Older customers with moderate spending:** retention offers, convenience, and personalized service.

These strategies are examples. Use the actual cluster averages to determine the most appropriate actions for each segment.

## Advantages
- Helps reveal customer behavior patterns.
- Supports targeted marketing and customer retention.
- Produces interpretable cluster summaries and visualizations.
- Saves cluster labels for additional analysis.

## Limitations
- Results depend on the selected number of clusters and feature choices.
- K-Means can be sensitive to outliers.
- Cluster numbers are arbitrary and do not indicate a ranking.
- The sample dataset is small; recommendations should be validated against real campaign outcomes.

## Future Enhancements
- Build an interactive Streamlit dashboard.
- Compare K-Means with hierarchical clustering and DBSCAN.
- Compare candidate cluster counts using silhouette scores.
- Add purchase history and transaction features.
- Generate downloadable marketing reports.

## Conclusion
This project demonstrates an end-to-end customer segmentation workflow using data cleaning, feature scaling, the Elbow Method, K-Means clustering, visualization, and segment profiling. The resulting segments can help businesses develop more focused marketing strategies.

## Author
**Your Name**  
GitHub: `https://github.com/YOUR-USERNAME`

## License
For educational and academic use. Add an open-source license file if you intend to distribute the project under a specific license.
