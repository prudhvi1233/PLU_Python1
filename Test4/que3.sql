/*
Question 3
Consider the following table.
Product
| ProductID | ProductName | Category
| Price |
|--------- |----------- |----------- |----- |
| 1
| Mouse
| 2
| 3
| 4
| Laptop
| Chair
| Keyboard
Write SQL queries to:
| Electronics | 800 |
| Electronics | 65000 |
| Furniture | 4500 |
| Electronics | 1200 |
1. Display products costing more than ₹1000.
2. Display all Electronics products.
3. Display the Laptop record
*/

USE agri_connect;

CREATE TABLE Product (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price INT
);

INSERT INTO Product (ProductID, ProductName, Category, Price)
VALUES
(1, 'Mouse', 'Electronics', 800),
(2, 'Laptop', 'Electronics', 65000),
(3, 'Chair', 'Furniture', 4500),
(4, 'Keyboard', 'Electronics', 1200);

SELECT * FROM Product;

SELECT * FROM Product
WHERE Price > 1000;

SELECT * FROM Product
WHERE Category = 'Electronics';

SELECT * FROM Product
WHERE ProductName = 'Laptop';