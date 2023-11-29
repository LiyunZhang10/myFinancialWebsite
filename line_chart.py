import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('output.csv')

# Calculate the sum of data for a specified row and the following three rows
def sum_data(df, start_row, col):
    rows = df.iloc[start_row: start_row + 4, col]
    total = 0.0
    for value in rows:
        if value.endswith('万'):
            number = float(value[:-1]) / 1000
        elif value.endswith('亿'):
            number = float(value[:-1]) * 10
        else:
            number = float(value)
        total += number
    return total

income = [sum_data(df, 42, 0), sum_data(df, 32, 0), sum_data(df, 23, 0), sum_data(df, 15, 0), sum_data(df, 4, 0)]
profit = [sum_data(df, 42, 4), sum_data(df, 32, 4), sum_data(df, 23, 4), sum_data(df, 15, 4), sum_data(df, 4, 4)]

time = ['2021-06-30', '2021-12-31', '2022-06-30', '2022-12-31', '2023-06-30']

# Plot the line chart
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(8, 6))  
plt.plot(time, income, marker='o', linewidth=2)  
plt.plot(time, profit, marker='o', linewidth=2)
plt.xlabel('时间/半年')
plt.ylabel('金额/千万')
plt.title('按产品分类的主营收入随时间的变化折线图')
plt.xticks(rotation=45)  # Adjust the rotation angle of x-axis tick labels
plt.yticks(range(0, int(max(income)) + 400, 200))  # Adjust the range and interval of y-axis ticks
for i in range(len(time)):
    plt.annotate(f'{income[i]:.2f}', xy=(time[i], income[i]), xytext=(0, 15), textcoords='offset points', ha='center', va='bottom') 
    plt.annotate(f'{profit[i]:.2f}', xy=(time[i], profit[i]), xytext=(0, -24), textcoords='offset points', ha='center', va='bottom')  # Add data labels with downward offset
plt.legend(['主营收入', '主营利润'], loc='best')
plt.tight_layout()

plt.show()