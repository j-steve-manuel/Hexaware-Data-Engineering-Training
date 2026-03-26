CREATE DATABASE company_training;
USE company_training;

CREATE TABLE projects (
project_id INT PRIMARY KEY,
emp_id INT,
project_name VARCHAR(100),
project_budget DECIMAL(12,2),
project_status VARCHAR(50)
);

CREATE TABLE employees (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(100),
department VARCHAR(50),
city VARCHAR(50)
);

INSERT INTO employees VALUES
(1, 'Rohan Mehta', 'IT', 'Hyderabad'),
(2, 'Sneha Iyer', 'IT', 'Bangalore'),
(3, 'Kiran Patel', 'Finance', 'Mumbai'),
(4, 'Ananya Das', 'HR', NULL),
(5, 'Rahul Sharma', 'IT', 'Delhi'),
(6, NULL, 'Marketing', 'Chennai');

INSERT INTO projects VALUES
(101, 1, 'AI Chatbot', 120000, 'Active'),
(102, 1, 'ML Prediction', 90000, 'Active'),
(103, 2, 'Data Warehouse', 150000, 'Active'),
(104, 3, 'Financial Dashboard', 80000, 'Completed'),
(105, NULL, 'Website Revamp', 60000, 'Pending'),
(106, 8, 'Mobile App', 100000, 'Active');

/* Exercise 1 */
select emp_name, project_name, project_budget
from employees e join projects p
on e.emp_id = p.emp_id;

/* Exercise 2 */
select emp_name, project_name 
from employees e left join projects p
on e.emp_id = p.emp_id;

/* Exercise 3 */
select emp_name, project_name 
from employees e right join projects p
on e.emp_id = p.emp_id;

/* Exercise 4 */
select emp_name, project_name 
from employees e left join projects p
on e.emp_id = p.emp_id
UNION
select emp_name, project_name 
from employees e right join projects p
on e.emp_id = p.emp_id;

/* Exercise 5 */
select *
from employees e cross join projects p
on e.emp_id = p.emp_id;


/* 2 — Join with Filtering */

/* Exercise 6 */
select project_id, project_name, project_budget, project_status, department
from projects p join employees e
on p.emp_id = e.emp_id
where department = 'IT';

/* Exercise 7 */
select * 
from projects p join employees e
on p.emp_id = e.emp_id
where project_budget>100000;

/* Exercise 8 */
select e.emp_id, emp_name, department, project_id, project_name
from projects p join employees e
on p.emp_id = e.emp_id
where city = 'Hyderabad';

/* Exercise 9 */
select e.emp_id, emp_name, count(project_id) as 'No of Projects Assigned'
from projects p join employees e
on p.emp_id = e.emp_id
group by e.emp_id;

/* Exercise 10 */
select e.emp_id, emp_name, sum(project_budget) as 'Total Budget'
from projects p join employees e
on p.emp_id = e.emp_id
group by e.emp_id;

/* Exercise 11 */
select department, sum(project_budget) as 'Budget Per Department'
from projects p join employees e
on p.emp_id = e.emp_id
group by department;

/* Exercise 12 */
select department, count(project_id) as Total_projects
from projects p join employees e
on p.emp_id = e.emp_id
group by department;

/* Exercise 13 */
select department, sum(project_budget) as Total_Budget
from projects p join employees e
on p.emp_id = e.emp_id
group by department;

/* Exercise 14 */
select city, count(e.emp_id) as Employee_count
from projects p join employees e
on p.emp_id = e.emp_id
group by city;

/* Exercise 15 */
select p.emp_id, emp_name, count(project_name) as Project_count
from projects p join employees e
on p.emp_id = e.emp_id
group by p.emp_id
having count(project_name)>1;

/* Exercise 16 */
select department, sum(project_budget) as Budget_alloted
from projects p join employees e
on p.emp_id = e.emp_id
group by department
having sum(project_budget)>150000;

/* Exercise 17 */
select p.emp_id, emp_name, sum(project_budget) as Total_Project_Budget
from projects p join employees e
on p.emp_id = e.emp_id
group by p.emp_id
having sum(project_budget)>100000;


/* 6 — Capstone Query */

select p.emp_id, emp_name, department, sum(project_budget) as Total_Project_Budget
from projects p join employees e
on p.emp_id = e.emp_id
group by p.emp_id
having sum(project_budget)>100000
order by sum(project_budget) desc;




