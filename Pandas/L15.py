"""
1. Merge sales_data with customers on customer_id.
Then calculate the average revenue per loyalty_tier and the percentage of total revenue contributed by each tier.
Sort the result by average revenue descending.
"""
file_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/sales_data.csv"
cust_path="/Users/prse/PycharmProjects/Python-Refresher/Python-Practice/data/customers.csv"

import pandas as pd

df=pd.read_csv(file_path)
print(df.shape)
df1=pd.read_csv(cust_path)
print(df1.shape)
new_df=pd.merge(df,df1,'left','customer_id',sort=False)

new_df['revenue']=new_df['quantity']*new_df['unit_price']
print(new_df)
cust_metrics=new_df.groupby('loyalty_tier').agg(
    avg_rev=('revenue','mean'),
    total_rev=('revenue','sum')
)
cust_metrics['revenue_pct'] = (
    cust_metrics['total_rev'] / cust_metrics['total_rev'].sum()
) * 100
print(cust_metrics.sort_values('avg_rev',ascending=False))

#
# 2. Using only Completed orders, find the top 3 products by total revenue in each region.
# Return a DataFrame with columns: region, product, total_revenue, rank_in_region.

mask=df['status']=='Completed'
my_df=new_df[mask]
rev_by_reg=my_df.groupby(['region','product']).agg(
    total_rev=('revenue','sum')
)
rev_by_reg['rank_by_reg']=rev_by_reg.groupby('region').rank(method='first',ascending=False)
mask=rev_by_reg['rank_by_reg']<=3
print(rev_by_reg[mask].sort_values(['region', 'rank_by_reg']))



# 3. Create a monthly cohort-style summary: for every customer’s first purchase month, show how many of those customers made at least one purchase in the following months.
# (Use order_date and customer_id).

df['purchase_month']=pd.to_datetime(df['order_date']).dt.month
df['first_purchase_month'] = (
    df.groupby('customer_id')['purchase_month']
      .transform('min')
)
res = df.groupby(
    ['first_purchase_month', 'purchase_month']
)['customer_id'].nunique()

print(res)
# 4. Add a column `days_since_signup` by merging with customers and calculating the difference between order_date and signup_date.
# Then compute the average revenue for orders placed within the first 90 days vs after 90 days of signup.


new_df['days_since_signup']=(pd.to_datetime(df['order_date'])-pd.to_datetime(df1['signup_date'])).dt.days
new_df=new_df.dropna()
print(new_df)
mask_within_90=new_df['days_since_signup']<90
mask_after_90=new_df['days_since_signup']>90
avg_rev_within = new_df.loc[new_df['days_since_signup'] < 90,'revenue'].mean()
avg_rev_after = new_df.loc[new_df['days_since_signup'] > 90,'revenue'].mean()
print(avg_rev_within,avg_rev_after)
#
# 5. Using groupby + transform, create a column that shows each order’s revenue as a percentage of the customer’s total lifetime revenue.
# Then filter to show only orders that represent more than 30% of that customer’s total revenue.

total_lifetime_rev=new_df.groupby('order_id')['revenue'].transform('sum')
new_df['rev_perc']=(total_lifetime_rev/total_lifetime_rev.sum())*100
print(new_df)
filtre=new_df['rev_perc']>30



# 6. Reshape the data to show, for each region, the total quantity sold of every product.
# Fill missing product-region combinations with 0 and sort the columns alphabetically.
#
# 7. Calculate a cumulative revenue column for each customer ordered by order_date.
# Then find the order number (1st, 2nd, 3rd…) on which each customer first crossed $1000 in cumulative revenue.
#
# 8. Identify customers who have purchased from at least 3 different categories.
# For those customers, show: customer_id, customer_name, number of categories, total revenue, and loyalty_tier.
#
# 9. Create a pivot table with region as rows and the combination of category + status as columns, showing total revenue.
# Make sure Cancelled and Completed appear for every category (fill missing with 0).
#
# 10. Optimize both DataFrames for memory by converting suitable columns to category and downcasting numeric types.
# Then perform an inner merge and compare the memory usage of the merged result before and after optimization.
# Report the percentage memory reduction.
