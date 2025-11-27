import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load and preprocess data
df = pd.read_csv('Fitness.csv')
X = StandardScaler().fit_transform(df.select_dtypes(include=['float64', 'int64']))

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
k_labels = kmeans.fit_predict(X)
k_score = silhouette_score(X, k_labels)

# EM clustering (Gaussian Mixture)
gmm = GaussianMixture(n_components=3, random_state=42)
g_labels = gmm.fit_predict(X)
g_score = silhouette_score(X, g_labels)

# Print comparison
print(f"Silhouette Score - KMeans: {k_score:.3f}")
print(f"Silhouette Score - EM (GMM): {g_score:.3f}")

if k_score > g_score:
    print("KMeans produced better-defined clusters.")
elif g_score > k_score:
    print("EM (GMM) produced better-defined clusters.")
else:
    print("Both methods produced similar clustering quality.")

plt.figure(figsize=(10,12))

# Bar graph comparison
methods = ['KMeans', 'EM (GMM)']
scores = [k_score, g_score]
colors = ['blue', 'green']

plt.figure()  # New figure for bar graph
plt.bar(methods, scores, color=colors)
plt.ylabel('Silhouette Score')
plt.title('Clustering Method Comparison')
plt.ylim(0, max(scores) + 0.1)  # Adjust y-axis to show scores properly
plt.show()