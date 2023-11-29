import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('output.csv')

# Extract the data
ratio = [float(value[:-1]) for value in df.iloc[33:36, 3]]
labels = ['金融电子商务服务', '金融数据服务', '互联网广告服务等'] 
colors = ['#FF8000', '#00FF00', '#FFFF00']

# Plot the pie chart
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.pie(ratio, labels=labels, colors=colors, wedgeprops={'width': 0.5})
plt.title('2021-12-31 按产品分类收入比例圆环图')
plt.legend(loc='upper left', prop={'size': 8})

plt.show()