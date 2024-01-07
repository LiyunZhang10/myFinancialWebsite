import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('myFinancialWebsite\output.csv')

# Extract the data
ratio = [float(value[:-1]) for value in df.iloc[33:36, 3]]
labels = ['金融电子商务服务', '金融数据服务', '互联网广告服务等'] 
colors = ['#FF8000', '#00FF00', '#FFFF00']

# Set figure size
fig = plt.figure(figsize=(6, 6))

# Plot the pie chart without labels
plt.rcParams['font.sans-serif'] = ['SimHei']
patches, _ = plt.pie(ratio, colors=colors, wedgeprops={'width': 0.5})

# Remove labels
for patch in patches:
    plt.gca().text(0, 0, '', ha='center')

plt.title('2021-12-31 按产品分类收入比例圆环图')
plt.legend(patches, labels, loc='lower right', prop={'size': 8})

plt.show()