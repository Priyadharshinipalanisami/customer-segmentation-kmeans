# Customer Segmentation Report

## Dataset and preparation
- Cleaned records used: 250
- Features scaled for clustering: Age, Annual Income (k$), Spending Score (1-100)
- Cleaning: trimmed column names and gender values, removed duplicate rows, converted numeric fields, and removed rows missing clustering features.
- Scaling: StandardScaler (z-score standardization). CustomerID was excluded because it is an identifier, not a customer behavior feature.

## Model
- Algorithm: K-Means
- Selected k: 5 (interpretable five-segment solution; inspect elbow chart and silhouette scores to validate for your use case).
- Silhouette score at k=5: 0.402

## Cluster profiles and recommended actions

### Cluster 0: Mature steady customers
- Customers: 64 (25.6% of dataset)
- Average age: 55.8
- Average annual income: $53.6k
- Average spending score: 39.8/100
- Female customers: 53.1%
- Marketing action: Prioritize convenience, reliable service, relevant essentials, and personalized retention offers.

### Cluster 1: Affluent cautious customers
- Customers: 49 (19.6% of dataset)
- Average age: 35.6
- Average annual income: $69.9k
- Average spending score: 23.5/100
- Female customers: 61.2%
- Marketing action: Use tailored recommendations, value demonstrations, and limited-time offers; avoid excessive discounting.

### Cluster 2: High-value spenders
- Customers: 89 (35.6% of dataset)
- Average age: 28.5
- Average annual income: $62.2k
- Average spending score: 72.4/100
- Female customers: 53.9%
- Marketing action: Offer premium bundles, loyalty rewards, early access, and personalized upsell campaigns.

### Cluster 3: High-value spenders
- Customers: 24 (9.6% of dataset)
- Average age: 31.5
- Average annual income: $241.5k
- Average spending score: 81.8/100
- Female customers: 41.7%
- Marketing action: Offer premium bundles, loyalty rewards, early access, and personalized upsell campaigns.

### Cluster 4: Affluent cautious customers
- Customers: 24 (9.6% of dataset)
- Average age: 42.2
- Average annual income: $237.9k
- Average spending score: 19.0/100
- Female customers: 62.5%
- Marketing action: Use tailored recommendations, value demonstrations, and limited-time offers; avoid excessive discounting.

## Interpretation notes
- Cluster IDs are arbitrary labels; compare the profile averages rather than treating a higher cluster number as a higher-value segment.
- Marketing actions are hypotheses based on age, income, and spending patterns. Validate them with campaign A/B tests and actual sales/conversion data.
- The Mall Customers dataset is a small demonstration dataset; it should not be treated as a representative customer population without validation.