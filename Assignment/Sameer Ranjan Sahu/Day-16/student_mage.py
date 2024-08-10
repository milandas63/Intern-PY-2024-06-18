-- Create the database
CREATE DATABASE StudentManagementSystem;

-- Use the database
USE StudentManagementSystem;

-- Create the Students Table
CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    house_id INT,
    class_id INT,
    optional_id INT,
    FOREIGN KEY (house_id) REFERENCES House(house_id),
    FOREIGN KEY (class_id) REFERENCES Classes(class_id),
    FOREIGN KEY (optional_id) REFERENCES Optional(optional_id)
);

-- Create the Classes Table
CREATE TABLE Classes (
    class_id INT PRIMARY KEY AUTO_INCREMENT,
    class_name VARCHAR(50) NOT NULL,
    class_teacher VARCHAR(100)
);

-- Create the House Table
CREATE TABLE House (
    house_id INT PRIMARY KEY AUTO_INCREMENT,
    house_name VARCHAR(50) NOT NULL,
    house_master VARCHAR(100)
);

-- Create the Optional Table
CREATE TABLE Optional (
    optional_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_name VARCHAR(
INSERT INTO Classes (class_name, class_teacher) VALUES 
('Class 1', 'Ms. Laura Smith'),
('Class 2', 'Mr. John Williams'),
('Class 3', 'Mrs. Emma Johnson'),
('Class 4', 'Mr. James Brown'),
('Class 5', 'Ms. Olivia Davis'),
('Class 6', 'Mr. Michael Miller'),
('Class 7', 'Ms. Sophia Wilson'),
('Class 8', 'Mr. William Moore'),
('Class 9', 'Mrs. Mia Taylor'),
('Class 10', 'Mr. Ethan Anderson');
INSERT INTO House (house_name, house_master) VALUES 
('Red House', 'Dr. Henry Adams'),
('Blue House', 'Mrs. Sarah Baker'),
('Green House', 'Mr. Charles Carter'),
('Yellow House', 'Ms. Nancy Cooper'),
('Purple House', 'Dr. Grace Evans'),
('Orange House', 'Mr. Benjamin Garcia'),
('Black House', 'Ms. Chloe Harris'),
('White House', 'Mr. Daniel Jackson'),
('Brown House', 'Mrs. Ella Lee'),
('Grey House', 'Mr. Jacob Lewis');
INSERT INTO Optional (subject_name) VALUES 
('Mathematics'),
('Science'),
('History'),
('Geography'),
('Art'),
('Music'),
('Physical Education'),
('Computer Science'),
('Economics'),
('Literature');
INSERT INTO Students (first_name, last_name, date_of_birth, gender, house_id, class_id, optional_id) VALUES 
('Alice', 'Johnson', '2007-01-15', 'Female', 1, 1, 1),
('Bob', 'Smith', '2006-02-20', 'Male', 2, 2, 2),
('Charlie', 'Brown', '2005-03-25', 'Male', 3, 3, 3),
('Diana', 'Evans', '2004-04-30', 'Female', 4, 4, 4),
('Ethan', 'Jones', '2003-05-10', 'Male', 5, 5, 5),
('Fiona', 'Williams', '2002-06-15', 'Female', 6, 6, 6),
('George', 'Taylor', '2001-07-20', 'Male', 7, 7, 7),
('Hannah', 'Davis', '2000-08-25', 'Female', 8, 8, 8),
('Ian', 'Wilson', '1999-09-30', 'Male', 9, 9, 9),
('Julia', 'Martinez', '1998-10-05', 'Female', 10, 10, 10);
-- Check Students table
SELECT * FROM Students;

-- Check Classes table
SELECT * FROM Classes;

-- Check House table
SELECT * FROM House;

-- Check Optional table
SELECT * FROM Optional;


