import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('myFinancialWebsite/output.csv')

labels = ['证券业务', '金融电子商务服务', '其他']
ratio = [float(value[:-1]) for value in df.iloc[32:36, 1]]
merged_ratio = ratio[:-2] + [sum(ratio[-2:])]

# Select three visually appealing colors
colors = ['#FF6384', '#36A2EB', '#FFCE56']

# Set figure size
fig = plt.figure(figsize=(6, 6))

# Plot the pie chart with empty labels
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.pie(merged_ratio, colors=colors, autopct='%1.1f%%')
plt.axis('equal')

# Set the title
plt.title('2021-06-30 按产品分类得到的收入比例')

# Add a legend and adjust its position
plt.legend(labels, loc='lower left')

plt.show()