/* begin database pet_project creation */

create database pet_project character set utf8;

/* end database pet_project creation */

/* begin table creation */

create table main
 (main_id tinyint unsigned not null auto_increment,
  title varchar(50) not null,
  constraint pk_main primary key (main_id)
 );

create table departments
 (dept_id tinyint unsigned not null auto_increment,
  main_id tinyint unsigned not null,
  department varchar(100),
  constraint fk_departments_main foreign key (main_id) 
  references main (main_id) on delete cascade on update restrict,
  constraint pk_departments primary key (dept_id)
 );

create table branch
 (branch_id tinyint unsigned not null auto_increment,
  country varchar(100),
  city varchar(100),
  constraint pk_branch primary key (branch_id)
 );

create table company
 (company_id tinyint unsigned not null auto_increment,
  company_name varchar(100),
  responsibility varchar(100),
  constraint pk_company primary key (company_id)
 );

create table staff
 (staff_id tinyint unsigned not null auto_increment,
  dept_id tinyint unsigned not null,
  f_name varchar(100),
  l_name varchar(100),
  phone varchar(50),
  email varchar(100),
  responsibility varchar(100),
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

/* end table creation */

/* begin data population */

/* main data */
load data local infile '/Users/vladimirbarikov/github/pet_project_rep/database/main.csv'
 into table main 
 fields terminated by ';' 
 lines terminated by '\n' 
 ignore 1 rows (main_id, title);

/* departments data */
load data local infile '/Users/vladimirbarikov/github/pet_project_rep/database/departments.csv'
 into table departments 
 fields terminated by ';' 
 lines terminated by '\n' 
 ignore 1 rows (dept_id, main_id, department);

/* branch data */
load data local infile '/Users/vladimirbarikov/github/pet_project_rep/database/branch.csv'
 into table branch
 fields terminated by ';' 
 lines terminated by '\n' 
 ignore 1 rows (branch_id, country, city);

/* company data */
load data local infile '/Users/vladimirbarikov/github/pet_project_rep/database/company.csv'
 into table company
 fields terminated by ';' 
 lines terminated by '\n' 
 ignore 1 rows (company_id, company_name, responsibility);

/* staff data */


/* end data population */