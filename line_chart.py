import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('output.csv')

# 定义函数sum_data，计算指定行及后面的三行数据的总和
def sum_data(df, start_row, col):
    # 提取指定行及后面的三行数据
    rows = df.iloc[start_row: start_row + 4, col]
    total = 0.0

    for value in rows:
        # 判断最后一位字符并进行相应的浮点数转换和累加操作
        if value.endswith('万'):
            number = float(value[:-1]) / 1000
        elif value.endswith('亿'):
            number = float(value[:-1]) * 10
        else:
            number = float(value)
        
        total += number

    return total

# 计算主营收入
income = [sum_data(df, 42, 0), sum_data(df, 32, 0), sum_data(df, 23, 0), sum_data(df, 15, 0), sum_data(df, 4, 0)]
profit = [sum_data(df, 42, 4), sum_data(df, 32, 4), sum_data(df, 23, 4), sum_data(df, 15, 4), sum_data(df, 4, 4)]

# 时间轴
time = ['2021-06-30', '2021-12-31', '2022-06-30', '2022-12-31', '2023-06-30']

# 绘制折线图
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(8, 6))  # 调整图形尺寸
plt.plot(time, income, marker='o', linewidth=2)  # 调整线条样式
plt.plot(time, profit, marker='o', linewidth=2)
plt.xlabel('时间/半年')
plt.ylabel('金额/千万')
plt.title('按产品分类的主营收入随时间的变化折线图')
plt.xticks(rotation=45)  # 调整x轴刻度标签的旋转角度
plt.yticks(range(0, int(max(income)) + 400, 200))  # 调整y轴刻度范围和间隔
for i in range(len(time)):
    plt.annotate(f'{income[i]:.2f}', xy=(time[i], income[i]), xytext=(0, 15), textcoords='offset points', ha='center', va='bottom') 
    plt.annotate(f'{profit[i]:.2f}', xy=(time[i], profit[i]), xytext=(0, -24), textcoords='offset points', ha='center', va='bottom') # 添加数据标签，向下偏移
plt.legend(['主营收入', '主营利润'], loc='best')
plt.tight_layout()

plt.show()