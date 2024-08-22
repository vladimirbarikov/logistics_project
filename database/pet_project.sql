/* begin database creation */

create database pet_project;

/* end database creation */

/* begin table creation */

create table main
(
    main_id VARCHAR(255),
    main_title VARCHAR(255),
    constraint pk_main primary key (main_id)
);

create table departments
(
    dept_id smallint unsigned not null auto_increment,
    main_id varchar(10),
    department varchar(255),
    constraint pk_departments primary key (dept_id, main_id)
);

/* end table creation */

/* begin data population */

load data local infile '/Users/vladimirbarikov/github_repository/sql/pet_project/database/main.csv' 
 into table main 
 fields terminated by ',' 
 lines terminated by '\n' 
 ignore 1 rows (main_id, main_title);

/* end data population */