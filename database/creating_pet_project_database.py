from getpass import getpass
from mysql.connector import connect

# connection establishing
with connect(
    host='127.0.0.1',
    user='root',
    password=getpass('Пароль:'),
    database='pet_project',
) as connection:
    
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
        country varchar(10),
        city varchar(20),
        constraint fk_branch_main foreign key (main_id) 
        references main (main_id) on delete cascade on update restrict,
        constraint pk_branch primary key (branch_id)
    )
    '''

    # tables creation
    with connection.cursor() as cursor:
        cursor.execute(create_table_main)
        cursor.execute(create_table_branch)
        # print(cursor.fetchall())