import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('output.csv')

ratio = [float(value[:-1]) for value in df.iloc[42:46, 1]]

labels = ['证券业务', '金融电子商务服务', '金融数据服务', '互联网广告服务等']
merged_ratio = ratio[:-2] + [sum(ratio[-2:])]
merged_label = labels[:-2] + ['其他']

colors = ['red', 'steelblue', 'green', 'orange'] 

# 绘制饼图
plt.rcParams['font.sans-serif'] = ['SimHei']
patches, l_text, p_text = plt.pie(merged_ratio, colors=colors, labels=merged_label, labeldistance=1.1, autopct="%1.1f%%", startangle=90, pctdistance=0.6)
plt.axis("equal")  
plt.title('2021-06-30 按产品分类得到的收入比例饼图')
plt.legend()

plt.show()