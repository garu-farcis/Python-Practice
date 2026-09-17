"""Load the CSV and create a new column `revenue` = quantity * unit_price * (1 - discount).
Then calculate the total revenue and the average revenue per order for Completed orders only."""
import pandas as pd
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"
df=pd.read_csv(file_path)
df['revenue']=df['quantity']*df['unit_price']*(1-df['discount'])
df_comp=df[df['status']=='Completed']
total_revenue=df_comp.groupby('order_id')['revenue'].sum()
print(total_revenue)
avg_revenue=total_revenue.mean()
print(avg_revenue)