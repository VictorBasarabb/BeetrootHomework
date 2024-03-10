select
    first_name,
    last_name
from employees;

select distinct
    department_id
from employees;

select *
from employees
order by first_name desc;

select
    first_name,
    last_name,
    salary,
    salary * 0.12 as PF
from employees;

select
    max(salary) as max_salary,
    min(salary) as min_salary
from employees;

select
    employee_id,
    round(salary, 2)
from employees;