USE agri_connect;

CREATE TABLE Orders (
    OrderID INT,
    CustomerName VARCHAR(100),
    OrderDate DATE,
    Amount INT
);

CREATE INDEX idx_OrderID
ON Orders(OrderID);

SHOW INDEX FROM Orders;