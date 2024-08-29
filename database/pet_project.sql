/* database pet_project  creation*/

create database pet_project character set utf8;

/* begin to use database pet_project */

use pet_project database

/* begin tables creation */

create table main
 (main_id tinyint unsigned not null auto_increment,
  title varchar(15) not null,
  constraint pk_main primary key (main_id)
 );

create table branch
 (branch_id tinyint unsigned not null auto_increment,
  country tinitext,
  city varchar(30),
  constraint pk_branch primary key (branch_id)
 );

create table departments
 (dept_id tinyint unsigned not null auto_increment,
  main_id tinyint unsigned not null,
  department tinytext,
  constraint fk_departments_main foreign key (main_id) 
  references main (main_id) on delete cascade on update restrict,
  constraint pk_departments primary key (dept_id)
 );

create table staff
 (staff_id tinyint unsigned not null auto_increment,
  dept_id tinyint unsigned not null,
  f_name varchar(30),
  l_name varchar(30),
  phone varchar(30),
  email varchar(50),
  responsibility varchar(50) not null,
  company_id tinyint unsigned not null,
  leader_id tinyint unsigned,
  branch_id tinyint unsigned not null,
  constraint fk_staff_staff foreign key (leader_id)
  references staff (staff_id),
  constraint fk_staff_departments foreign key (dept_id) 
  references departments (dept_id) on delete cascade on update restrict,
  constraint fk_staff_company foreign key (company_id) 
  references company (company_id) on delete cascade on update restrict,
  constraint fk_staff_branch foreign key (branch_id) 
  references branch (branch_id) on delete cascade on update restrict,
  constraint pk_staff primary key (staff_id)
 );

create table customers
 (customer_id tinyint unsigned not null auto_increment,
  staff_id tinyint unsigned not null,
  customer_name varchar(30),
  city varchar(30),
  street varchar(30),
  building varchar(10),
  contact_person varchar(30),
  contact_phone varchar(30),
  work_start varchar(5),
  work_end varchar(5),
  constraint fk_customers_staff foreign key (staff_id)
  references staff (staff_id),
  constraint pk_customers primary key (customer_id)
 );

/* end table creation */

/* begin data population */

/* main data */
load data local infile '/Users/vladimirbarikov/github/pet_project_rep/database/main.csv'
 into table main 
 fields terminated by ';' 
 lines terminated by '\n' 
 ignore 1 rows
 (main_id, title);

/* departments data */
load data local infile '/Users/vladimirbarikov/github/pet_project_rep/database/departments.csv'
 into table departments 
 fields terminated by ';' 
 lines terminated by '\n' 
 ignore 1 rows
 (dept_id, main_id, department);

/* branch data */
load data local infile '/Users/vladimirbarikov/github/pet_project_rep/database/branch.csv'
 into table branch
 fields terminated by ';' 
 lines terminated by '\n' 
 ignore 1 rows
 (branch_id, country, city);

/* company data */
load data local infile '/Users/vladimirbarikov/github/pet_project_rep/database/joint_work.csv'
 into table joint_work
 fields terminated by ';' 
 lines terminated by '\n' 
 ignore 1 rows
 (company_id, company_name, responsibility);

/* staff data */
load data local infile '/Users/vladimirbarikov/github/pet_project_rep/database/staff.csv'
 into table staff
 fields terminated by ';' 
 lines terminated by '\n' 
 ignore 1 rows
 (staff_id, dept_id, @f_name, @l_name, @phone, @email, responsibility, company_id, @leader_id, branch_id)
 set f_name = if(@f_name='', null, @f_name),
     l_name = if(@l_name='', null, @l_name),
     phone = if(@phone='', null, @phone),
     email = if(@email='', null, @email),
     leader_id = if(@leader_id='', null, @leader_id);

/* customers data */
load data local infile '/Users/vladimirbarikov/github/pet_project_rep/database/customers.csv'
 into table customers
 fields terminated by ';'
 lines terminated by '\n'
 ignore 1 rows
 (customer_id, staff_id, @customer_name, @city, @street, @building, @contact_person, @contact_phone, @work_start, @work_end)
 set customer_name = if(@customer_name='', null, @customer_name),
     city = if(@city='', null, @city),
     street = if(@street='', null, @street),
     building = if(@building='', null, @building),
     contact_person = if(@contact_person='', null, @contact_person),
     contact_phone = if(@contact_phone='', null, @contact_phone),
     work_start = if(@work_start='', null, @work_start),
     work_end = if(@work_end='', null, @work_end);

/* end data population */