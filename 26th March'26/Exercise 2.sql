CREATE DATABASE capstone_sql;
USE capstone_sql;

CREATE TABLE students (
student_id INT PRIMARY KEY,
student_name VARCHAR(100),
city VARCHAR(50),
age INT
);

CREATE TABLE enrollments (
enrollment_id INT PRIMARY KEY,
student_id INT,
course_name VARCHAR(100),
trainer VARCHAR(100),
fee DECIMAL(10,2)
);

INSERT INTO students VALUES
(1,'Aarav Sharma','Hyderabad',22),
(2,'Priya Reddy','Bangalore',23),
(3,'Rahul Verma','Mumbai',24),
(4,'Sneha Kapoor',NULL,21),
(5,'Vikram Singh','Chennai',25),
(6,NULL,'Delhi',22);

INSERT INTO enrollments VALUES
(101,1,'MySQL','Abdullah Khan',5000),
(102,1,'Python','Abdullah Khan',7000),
(103,2,'Power BI','Kiran',6000),
(104,3,'Azure Data Factory','Sneha',8000),
(105,NULL,'Excel','Rohan',3000),
(106,8,'Databricks','Ananya',9000);

/* Exercise 1 */
select student_name, course_name
from Enrollments e inner join Students s
on e.student_id = s.student_id;

/* Exercise 2 */
select e.student_id, student_name, course_name
from Enrollments e left join Students s
on e.student_id = s.student_id;

/* Exercise 3 */
select e.student_id, student_name, course_name
from Enrollments e right join Students s
on e.student_id = s.student_id;

/* Exercise 4 */
select e.student_id, student_name, course_name
from Enrollments e left join Students s
on e.student_id = s.student_id
union
select e.student_id, student_name, course_name
from Enrollments e right join Students s
on e.student_id = s.student_id;

/* Exercise 5 */
select * 
from Enrollments e cross join Students s
on e.student_id = s.student_id;

/* Exercise 6 */
select student_name, course_name
from Enrollments e join Students s
on e.student_id = s.student_id
where city = 'Hyderabad';

/* Exercise 7 */
select course_name, fee from enrollments
where fee>6000;

/* Exercise 8 */
select e.student_id, student_name, count(course_name) as No_of_Course_Enrolled
from Enrollments e join Students s
on e.student_id = s.student_id
group by e.student_id;

/* Exercise 9 */
select e.student_id, student_name, sum(fee) as fee_paid
from Enrollments e join Students s
on e.student_id = s.student_id
group by e.student_id;

/* Exercise 10 */
select e.student_id, student_name, count(course_name) as Courses_enrolled
from Enrollments e join Students s
on e.student_id = s.student_id
group by e.student_id
having count(course_name)>1;

/* Exercise 11 */
select trainer, sum(fee) as total_fee_collected
from Enrollments e join Students s
on e.student_id = s.student_id
group by trainer
having sum(fee)>10000;

/* Exercise 12 */
select city, count(e.student_id) as Student_Count
from Enrollments e join Students s
on e.student_id = s.student_id
group by city
having count(e.student_id)>1;

/* Final Capstone Query */
select student_name, city, sum(fee) as Total_fee_paid
from Enrollments e join Students s
on e.student_id = s.student_id
group by student_name,city
having sum(fee)>5000
order by sum(fee) desc;

