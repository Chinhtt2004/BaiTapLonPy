import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Đọc dữ liệu
df = pd.read_csv('results.csv', header=[0, 1, 2])

# Làm sạch tên cột
df.columns = [tuple('' if 'Unnamed:' in x else x for x in col) for col in df.columns]

# Kiểm tra tên cột
print(df.columns)

# Lọc các cột số (float và int)
numeric_cols = df.select_dtypes(include=['float', 'int']).columns

# Vẽ histogram theo thuộc tính của toàn giải
for att in numeric_cols:
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x=att, kde=True, bins=20)
    title = f"Histogram {att[1]}_{att[2]} of All Players in the League"
    plt.title(title)
    plt.xlabel(f"{att[1]}_{att[2]}")
    plt.ylabel("Frequency")

    # Hiển thị biểu đồ
    plt.show()
    plt.close()  # Đóng hình để giải phóng bộ nhớ
