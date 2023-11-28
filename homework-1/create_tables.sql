CREATE TABLE employees
(
	employee_id int PRIMARY KEY ,
	first_name varchar(100) NOT NULL,
	last_name varchar(100)NOT NULL,
	title varchar(100) NOT NULL, 
	birth_date date,
	notes text NOT NULL
);

SELECT * FROM employees

CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id SERIAL PRIMARY KEY,
	customer_id_ VARCHAR(10) NOT NULL REFERENCES customers(customer_id),
 	employee_id_ INT NOT NULL REFERENCES employees(employee_id),
	order_date DATE NOT NULL,
    ship_city VARCHAR(30) NOT NULL
);