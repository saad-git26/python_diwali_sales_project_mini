# Diwali Mini Sales Report

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load: file kholo
df = pd.read_csv(r'D:\home\my work\python\Diwali sales project\Diwali Sales Data.csv', encoding='unicode_escape')

# 2. Clean: safai
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
df.dropna(inplace=True)
df['Amount'] = df['Amount'].astype('int')

# 3. Total: simple numbers
print("Total Sales =", df['Amount'].sum())
print("Total Orders =", df['Orders'].sum())

# 4. Sawaal 1: Kaun zyada kharidta hai? (Gender)
df.groupby('Gender')['Amount'].sum().plot(kind='bar', title='Gender wise Sales')
plt.show()

# 5. Sawaal 2: Kaunse top 5 State?
df.groupby('State')['Amount'].sum().nlargest(5).plot(kind='bar', title='Top 5 States')
plt.show()

# 6. Sawaal 3: Kaunsi top 5 Category?
df.groupby('Product_Category')['Amount'].sum().nlargest(5).plot(kind='bar', title='Top 5 Categories')
plt.show()