from getpass import getpass
from mysql.connector import connect

# connection establishing
with connect(
    host='127.0.0.1',
    user='root',
    password=getpass('Пароль:'),
    database='pet_project',
) as connection:
    
# # creation pet_project database
#     create_pet_project_db = '''
#     create database pet_project character set utf8
#     '''

# # using pet_project database
#     use_pet_project_db = '''
#     use pet_project
#     '''

# creation tables
    create_table_main = '''
    create table main (
        main_id tinyint unsigned not null auto_increment,
        title varchar(30) not null,
        constraint pk_main primary key (main_id)
    )
    '''

    create_table_branch = '''
    create table branch (
        branch_id tinyint unsigned not null auto_increment,
        main_id tinyint unsigned not null,
        country tinytext,
        city varchar(20),
        constraint fk_branch_main foreign key (main_id)
        references main (main_id) on delete cascade on update restrict,
        constraint pk_branch primary key (branch_id)
    )
    '''

    create_table_departments = '''
    create table departments (
        dept_id tinyint unsigned not null auto_increment,
        main_id tinyint unsigned not null,
        department tinytext,
        constraint fk_departments_main foreign key (main_id)
        references main (main_id) on delete cascade on update restrict,
        constraint pk_departments primary key (dept_id)
    )
    '''

    create_table_staff = '''
    create table staff (
        staff_id tinyint unsigned not null auto_increment,
        dept_id tinyint unsigned not null,
        main_id tinyint unsigned not null,
        f_name tinytext,
        l_name tinytext,
        phone varchar(30),
        email varchar(50),
        responsibility tinytext not null,
        leader_id tinyint unsigned,
        branch_id tinyint unsigned not null,
        constraint fk_staff_main foreign key (main_id)
        references main (main_id) on delete cascade on update restrict,
        constraint fk_staff_branch foreign key (branch_id)
        references branch (branch_id) on delete cascade on update restrict,
        constraint fk_staff_departments foreign key (dept_id)
        references departments (dept_id) on delete cascade on update restrict,
        constraint fk_staff_staff foreign key (leader_id)
        references staff (staff_id) on delete cascade on update restrict,
        constraint pk_staff primary key (staff_id)
    )
    '''

    create_table_customers = '''
    create table customers (
        customer_id tinyint unsigned not null auto_increment,
        staff_id tinyint unsigned not null,
        main_id tinyint unsigned not null,
        customer_name varchar(50),
        country tinytext,
        city varchar(20),
        street varchar(30),
        building varchar(10),
        work_start varchar(5),
        work_end varchar(5),
        constraint fk_customers_main foreign key (main_id)
        references main (main_id) on delete cascade on update restrict,
        constraint fk_customers_staff foreign key (staff_id)
        references staff (staff_id) on delete cascade on update restrict,
        constraint pk_customers primary key (customer_id)
    )
    '''

    create_table_customer_contacts = '''
    create table customer_contacts (
        contact_id tinyint unsigned not null auto_increment,
        customer_id tinyint unsigned not null,
        f_name tinytext not null,
        l_name tinytext,
        phone varchar(30) not null,
        email varchar(50),
        responsibility tinytext,
        constraint fk_customer_contacts_customers foreign key (customer_id)
        references customers (customer_id) on delete cascade on update restrict,
        constraint pk_customer_contacts primary key (contact_id)
    )
    '''

    create_table_providers = '''
    create table providers (
        provider_id tinyint unsigned not null auto_increment,
        main_id tinyint unsigned not null,
        provider_name varchar(50) not null,
        responsibility tinytext not null,
        constraint fk_providers_main foreign key (main_id)
        references main (main_id)on delete cascade on update restrict,
        constraint pk_providers primary key (provider_id)
    )
    '''

    create_table_provider_contacts = '''
    create table provider_contacts (
        contact_id tinyint unsigned not null auto_increment,
        provider_id tinyint unsigned not null,
        f_name tinytext not null,
        l_name tinytext,
        phone varchar(30) not null,
        email varchar(50),
        responsibility tinytext not null,
        leader_id tinyint unsigned,
        constraint fk_provider_contacts_providers foreign key (provider_id)
        references providers (provider_id) on delete cascade on update restrict,
        constraint pk_provider_contacts primary key (contact_id)
    )
    '''

    create_table_products = '''
    create table products (
        product_id tinyint unsigned not null auto_increment,
        main_id tinyint unsigned not null,
        product tinytext not null,
        description tinytext,
        constraint fk_products_main foreign key (main_id)
        references main (main_id) on delete cascade on update restrict,
        constraint pk_products primary key (product_id)
    )
    '''

# execution sql scripts
    with connection.cursor() as cursor:
        # cursor.execute(create_pet_project_db)
        # cursor.execute(use_pet_project_db)
        # cursor.execute(create_table_main)
        # cursor.execute(create_table_branch)
        # cursor.execute(create_table_departments)
        # cursor.execute(create_table_staff)
        # cursor.execute(create_table_customers)
        # cursor.execute(create_table_customer_contacts)
        # cursor.execute(create_table_providers)
        # cursor.execute(create_table_provider_contacts)
        cursor.execute(create_table_products)
        # print(cursor.fetchall())
