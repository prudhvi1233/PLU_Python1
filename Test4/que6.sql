/*

*/
USE agri_connect;
DROP TABLE Student;
CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name VARCHAR(100),
    CourseID INT
);
INSERT INTO Student (StudentID, Name, CourseID)
VALUES
(1, 'Rahul', 201),
(2, 'Neha', 202),
(3, 'Aman', NULL);
CREATE TABLE Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(100)
);
INSERT INTO Course (CourseID, CourseName)
VALUES
(201, 'Python'),
(202, 'SQL');
SELECT Student.Name, Course.CourseName
FROM Student
LEFT JOIN Course
ON Student.CourseID = Course.CourseID;