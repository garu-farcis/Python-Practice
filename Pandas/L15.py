"""
1. Merge sales_data with customers on customer_id.
Then calculate the average revenue per loyalty_tier and the percentage of total revenue contributed by each tier.
Sort the result by average revenue descending.

2. Using only Completed orders, find the top 3 products by total revenue in each region.
Return a DataFrame with columns: region, product, total_revenue, rank_in_region.

3. Create a monthly cohort-style summary: for every customer’s first purchase month, show how many of those customers made at least one purchase in the following months.
(Use order_date and customer_id).

4. Add a column `days_since_signup` by merging with customers and calculating the difference between order_date and signup_date.
Then compute the average revenue for orders placed within the first 90 days vs after 90 days of signup.

5. Using groupby + transform, create a column that shows each order’s revenue as a percentage of the customer’s total lifetime revenue.
Then filter to show only orders that represent more than 30% of that customer’s total revenue.

6. Reshape the data to show, for each region, the total quantity sold of every product.
Fill missing product-region combinations with 0 and sort the columns alphabetically.

7. Calculate a cumulative revenue column for each customer ordered by order_date.
Then find the order number (1st, 2nd, 3rd…) on which each customer first crossed $1000 in cumulative revenue.

8. Identify customers who have purchased from at least 3 different categories.
For those customers, show: customer_id, customer_name, number of categories, total revenue, and loyalty_tier.

9. Create a pivot table with region as rows and the combination of category + status as columns, showing total revenue.
Make sure Cancelled and Completed appear for every category (fill missing with 0).

10. Optimize both DataFrames for memory by converting suitable columns to category and downcasting numeric types.
Then perform an inner merge and compare the memory usage of the merged result before and after optimization.
Report the percentage memory reduction.
"""