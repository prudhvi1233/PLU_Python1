USE agri_connect;

CREATE TABLE Book (
    BookID INT PRIMARY KEY,
    BookName VARCHAR(100),
    Author VARCHAR(100),
    Price INT
);

INSERT INTO Book (BookID, BookName, Author, Price)
VALUES
(1, 'Python Basics', 'Prudhvi', 500),
(2, 'Learning SQL', 'mohan', 700);

DELIMITER //

CREATE PROCEDURE GetBooks()
BEGIN
    SELECT * FROM Book;
END //

DELIMITER ;

CALL GetBooks();