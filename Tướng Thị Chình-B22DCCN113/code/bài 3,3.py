from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

# Bước 1: Tải dữ liệu
data = pd.read_csv('results.csv')

# Bước 2: Xử lý dữ liệu thiếu và chuẩn hóa
data_numeric = data.select_dtypes(include=['float64', 'int64'])  # Chọn các cột số
data_numeric = data_numeric.fillna(data_numeric.mean())  # Điền NaN bằng trung bình
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_numeric)

# Bước 3: Giảm chiều dữ liệu với PCA
pca = PCA(n_components=2)
data_2d = pca.fit_transform(data_scaled)

# Bước 4: Áp dụng K-means để phân cụm
kmeans = KMeans(n_clusters=4, random_state=0)
clusters = kmeans.fit_predict(data_scaled)

# Bước 5: Vẽ biểu đồ phân cụm
plt.figure(figsize=(10, 6))
plt.scatter(data_2d[:, 0], data_2d[:, 1], c=clusters, cmap='viridis', alpha=0.6)
plt.colorbar(label='Cluster')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('K-means Clustering Visualization in 2D using PCA')
plt.show()

