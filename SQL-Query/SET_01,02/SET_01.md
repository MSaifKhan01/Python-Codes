1.

create TABLE customers(
id INT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
address VARCHAR(100), 
phone_number VARCHAR(100)

)

2.

insert into customers(id,name,address,phone_number)
VALUES
	(1,'abc','Delhi','9120000000'),
    (2,'abc2','New delhi','9120000000'),
    (3,'abc3','Haryana','9120000000'),
    (4,'abc4','Noida','9120000000'),
    (5,'abc5','UP','9120000000')

3.

select * from customers

4.


select name,email from customers

5.

select * from customer where id=3


6.

select * from customers where name like "A%"


7.

select * from customers order by name desc

8.

update customers set address ="chennai" where id="4" 


9.

select * from customers order by id asc limit 3

10.

delete from customers where id=3

11.

select count(*) from customers

12. 


select * from customers order by name asc offset 2

13.

select * from customers where id>2 and name like 'B%'

14.


select * from customers where id<3 or name like "%s"


15. 
select  * from customers where phone_number IS NULL;