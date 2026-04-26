SELECT * FROM sales;

SELECT SUM(Sales) AS total_sales
FROM sales;

SELECT SUM(Profit) AS total_profit
FROM sales;

SELECT Category, SUM(Sales) AS total_sales
FROM sales
GROUP BY Category
ORDER BY total_sales DESC;

SELECT City, SUM(Profit) AS total_profit
FROM sales
GROUP BY City
ORDER BY total_profit DESC;

SELECT Product, SUM(Quantity) AS total_quantity
FROM sales
GROUP BY Product
ORDER BY total_quantity DESC;

SELECT Payment_Mode, COUNT(*) AS total_orders
FROM sales
GROUP BY Payment_Mode
ORDER BY total_orders DESC;