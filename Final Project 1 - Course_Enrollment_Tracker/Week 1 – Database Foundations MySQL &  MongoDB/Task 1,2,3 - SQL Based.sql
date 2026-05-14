CREATE DATABASE StudentManagement;
USE StudentManagement;

-- 1. Schema Creation
CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    INDEX (last_name) -- Index for searching by student
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    total_modules INT NOT NULL,
    INDEX (course_name) -- Index for searching by course
);

CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE progress (
    progress_id INT PRIMARY KEY AUTO_INCREMENT,
    enrollment_id INT,
    modules_completed INT DEFAULT 0,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (enrollment_id) REFERENCES enrollments(enrollment_id)
);

-- 2. CRUD Operations
INSERT INTO students (first_name, last_name, email) 
VALUES ('John', 'Doe', 'john.doe@example.com');

INSERT INTO courses (course_id, course_name, total_modules) 
VALUES (101, 'Python for Data Engineering', 10);

INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (1, 101, '2026-05-13');
INSERT INTO progress (enrollment_id, modules_completed) VALUES (LAST_INSERT_ID(), 0);

-- Update: Progress update
UPDATE progress 
SET modules_completed = 5 
WHERE enrollment_id = 1;

-- 3. Stored Procedure: Calculate Completion Percentage
DELIMITER //

CREATE PROCEDURE GetCourseCompletion(IN input_student_id INT, IN input_course_id INT)
BEGIN
    SELECT 
        s.first_name, 
        c.course_name,
        p.modules_completed,
        c.total_modules,
        (p.modules_completed / c.total_modules) * 100 AS completion_percentage
    FROM enrollments e
    JOIN students s ON e.student_id = s.student_id
    JOIN courses c ON e.course_id = c.course_id
    JOIN progress p ON e.enrollment_id = p.enrollment_id
    WHERE s.student_id = input_student_id AND c.course_id = input_course_id;
END //

DELIMITER ;