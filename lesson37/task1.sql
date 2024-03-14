select
    e.first_name,
    e.last_name,
    e.department_id,
    d.department_name
from
    employees e
 left join department d
     on e.department_id = d.department_id
;

select
    e.first_name,
    e.last_name,
    d.department_name,
    l.city,
    l.state_province
from employees e
left join department d
    on e.department_id = d.department_id
left join locations l on d.location_id = l.location_id
;


select
    e.first_name,
    e.last_name,
    d.department_id,
    d.department_name
from employees e
join department d on e.department_id = d.department_id
where e.department_id in (40, 80)
;


select
    d.department_name,
    e.first_name,
    e.last_name
from department d
left join employees e on d.department_id = e.department_id
;


select
    e1.first_name as employee_first_name,
    e2.first_name as manager_first_name
from employees e1
join employees e2 on e1.manager_id = e2.employee_id
;


select
    (e.first_name || ' ' || e.last_name) as fullname,
    (j.max_salary - e.salary) as salary_difference
from employees e
join jobs j on e.job_id = j.job_id
;


select
    j.job_title,
    avg(e.salary) as average_salary
from employees e
join jobs j where e.job_id = j.job_id
group by j.job_title
;


select
    concat(e.first_name, ' ', e.last_name) as full_name,
    e.salary
from employees e
join departments d on e.department_id = d.department_id
join locations l on d.location_id = l.location_id
where l.city = 'London'
;


select
    d.department_name,
    count(e.employee_id) as num_of_employees
from employees e
join department d on e.department_id = d.department_id
group by d.department_name
;