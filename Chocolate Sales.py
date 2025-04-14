import pandas as pd 
import seaborn as sb
import matplotlib.pyplot as plt
df = pd.read_csv('Chocolate Sales.csv') 
# Remove $ and commas, then convert to float
df['Amount'] = df['Amount'].replace(r'[\$,]', '', regex=True).astype(float)


# Total Amount
total_amount = df['Amount'].sum()
print("Total Revenue: $", total_amount)
#Total Boxes 
total_boxes = df['Boxes Shipped'].sum()
print("Total Boxes Shipped: ", total_boxes)
#Total Sales made
count_sales = df['Amount'].count()
print("Total Sales made:", count_sales)
