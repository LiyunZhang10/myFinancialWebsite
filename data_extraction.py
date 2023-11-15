from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
import os.path

def is_number_string(string):
    unit_words = {'万', '亿', '%'}
    for word in unit_words:
        if word in string:
            return True
    cleaned_str = ''.join(c for c in string if c.isdigit())
    return bool(cleaned_str) or string == '--'


# Create a WebDriver instance
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://emweb.securities.eastmoney.com/PC_HSF10/BusinessAnalysis/Index?type=web&code=SZ300059#')

# Get all table elements
tables = driver.find_elements(By.TAG_NAME, 'table')

all_data = []

# Iterate over each table
for table in tables:
    rows = table.find_elements(By.TAG_NAME, 'tr')

    for row in rows:
        cells = row.find_elements(By.TAG_NAME, 'td')
        part_data = []

        for cell in cells:
            if is_number_string(cell.text):
                part_data.append(str(cell.text))

        if part_data:
            all_data.append(part_data)

df = pd.DataFrame(all_data, columns=['主营收入(元)', '收入比例(元)', '主营成本(元)', '成本比例', '主营利润(元)', '利润比例', '毛利率(%)'])

# Store the data as a CSV file
parent_dir = os.path.dirname(__file__)
filename = os.path.join(parent_dir, 'output.csv')
df.to_csv(filename, index=False)