from sklearn.cluster import KMeans

# Standardize the data
X = scaler.transform(data)

# Train the K-Means model
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
