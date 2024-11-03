import pandas as pd

# Bước 1: Đọc dữ liệu từ file CSV
data = pd.read_csv('results2.csv')  # Thay thế bằng đường dẫn tới file của bạn

# Bước 2: Loại bỏ hàng có giá trị 'All' trong cột 'Team'
filtered_data = data[data['Team'] != 'All']

# Bước 3: Tìm đội bóng có giá trị cao nhất cho từng chỉ số
max_values = filtered_data.set_index('Team').idxmax()

# Hiển thị kết quả
print(max_values)
filtered_data['Total_Goals'] = filtered_data['Mean of Performance_non-Penalty Goals'] + filtered_data['Mean of Performance_Penalty Goals']

# Bước 4: Tìm đội có tổng điểm cao nhất
team_with_max_goals = filtered_data.loc[filtered_data['Total_Goals'].idxmax()]

# Hiển thị kết quả
print("Đội có tổng bàn thắng cao nhất:")
print(team_with_max_goals[['Team', 'Total_Goals']])