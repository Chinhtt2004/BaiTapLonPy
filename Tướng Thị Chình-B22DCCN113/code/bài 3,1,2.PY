import warnings
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.impute import SimpleImputer

# Tải dữ liệu
df = pd.read_csv('results.csv')

# Chọn các cột số và xử lý NaN
X = df.select_dtypes(include=[float, int])

# Thay thế giá trị NaN bằng giá trị trung bình
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

sse = []

# Thực hiện phân cụm KMeans
for k in range(2, 10):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    sse.append(kmeans.inertia_)

# Vẽ biểu đồ phương pháp Elbow
plt.figure(figsize=(12, 5))
plt.plot(range(2, 10), sse, marker='o')
plt.xlabel("Số lượng cụm")
plt.ylabel("SSE")
plt.title("Phương pháp Elbow")
# Hiển thị biểu đồ
plt.tight_layout()
plt.show()
# chọn k=4
