from getpass import getpass
import mysql.connector
import warnings
warnings.filterwarnings('ignore')

# connection establishment
cnx = mysql.connector.connect(user=input('User:'),
                              password=getpass('Password:'),
                              host='localhost',
                              allow_local_infile=True)

cursor = cnx.cursor(buffered=True)
            
# creation logistics database
create_logistics_db = '''
create database if not exists logistics_db character set utf8
'''

# use logistics database
use_logistics_db = '''
use logistics_db
'''

# creation tables
create_table_branch = '''
create table if not exists branch (
    branch_id smallint unsigned not null auto_increment,
    country varchar(20) not null,
    zip varchar(20) not null,
    city varchar(20) not null,
    street varchar(30) not null,
    building varchar(20) not null,
    constraint pk_branch primary key (branch_id)
)
'''

create_table_departments = '''
create table if not exists departments (
    dept_id smallint unsigned not null auto_increment,
    department varchar(30),
    constraint pk_departments primary key (dept_id)
)
'''

create_table_staff = '''
create table if not exists staff (
    staff_id smallint unsigned not null auto_increment,
    f_name varchar(20),
    l_name varchar(20),
    gender enum('М', 'Ж') not null,
    phone varchar(30),
    email varchar(50),
    responsibility varchar(50) not null,
    leader_id smallint unsigned,
    branch_id smallint unsigned not null,
    dept_id smallint unsigned not null,
    constraint fk_staff_staff foreign key (leader_id)
    references staff (staff_id) on delete cascade on update restrict,
    constraint fk_staff_branch foreign key (branch_id)
    references branch (branch_id) on delete cascade on update restrict,
    constraint fk_staff_departments foreign key (dept_id)
    references departments (dept_id) on delete cascade on update restrict,
    constraint pk_staff primary key (staff_id)
)
'''

create_table_customers = '''
create table if not exists customers (
    customer_id smallint unsigned not null auto_increment,
    customer_name varchar(50) not null,
    country varchar(20) not null,
    zip varchar(20),
    city varchar(20) not null,
    street varchar(30) not null,
    building varchar(10) not null,
    work_start time not null,
    work_end time not null,
    staff_id smallint unsigned not null,
    constraint fk_customers_staff foreign key (staff_id)
    references staff (staff_id) on delete cascade on update restrict,
    constraint pk_customers primary key (customer_id)
)
'''

create_table_customer_contacts = '''
create table if not exists customer_contacts (
    contact_id smallint unsigned not null auto_increment,
    f_name varchar(20) not null,
    l_name varchar(20),
    gender enum('М', 'Ж') not null,
    phone varchar(30) not null,
    email varchar(50),
    responsibility varchar(50),
    customer_id smallint unsigned not null,
    constraint fk_customer_contacts_customers foreign key (customer_id)
    references customers (customer_id) on delete cascade on update restrict,
    constraint pk_customer_contacts primary key (contact_id)
)
'''

create_table_providers = '''
create table if not exists providers (
    provider_id smallint unsigned not null auto_increment,
    provider_name varchar(50) not null,
    country varchar(20) not null,
    zip varchar(20),
    city varchar(20) not null,
    street varchar(30) not null,
    building varchar(10) not null,
    responsibility varchar(50) not null,
    constraint pk_providers primary key (provider_id)
)
'''

create_table_provider_contacts = '''
create table if not exists provider_contacts (
    contact_id smallint unsigned not null auto_increment,
    f_name varchar(20) not null,
    l_name varchar(20),
    gender enum('М', 'Ж') not null,
    phone varchar(30) not null,
    email varchar(50),
    responsibility varchar(50) not null,
    leader_id smallint unsigned,
    provider_id smallint unsigned not null,
    constraint fk_provider_contacts_provider_contacts foreign key (leader_id)
    references provider_contacts (contact_id) on delete cascade on update restrict,
    constraint fk_provider_contacts_providers foreign key (provider_id)
    references providers (provider_id) on delete cascade on update restrict,
    constraint pk_provider_contacts primary key (contact_id)
)
'''

create_table_products = '''
create table if not exists products (
    product_id smallint unsigned not null auto_increment,
    product varchar(10) not null,
    description varchar(50) not null,
    constraint pk_products primary key (product_id)
)
'''

create_table_labeling = '''
create table if not exists labeling (
    labeling_id smallint unsigned not null auto_increment,
    packaging_lbl_drawing varchar(20),
    item_lbl_drawing varchar(20),
    ean_13_barcode varchar(20),
    product_id smallint unsigned not null,
    constraint UQ_ean_13_barcode unique (ean_13_barcode),
    constraint fk_labeling_product foreign key (product_id)
    references products (product_id) on delete cascade on update restrict,
    constraint pk_labeling primary key (labeling_id)
)
'''

create_table_packaging = '''
create table if not exists packaging (
    packaging_id smallint unsigned not null auto_increment,
    packaging_drawing varchar(20) not null,
    length_m float(5, 2) unsigned,
    width_m float(5, 2) unsigned,
    height_m float(5, 2) unsigned,
    volume_m3 float(5, 2) unsigned,
    weight_kg float(5, 2) unsigned,
    labeling_id smallint unsigned not null,
    constraint UQ_packaging_drawing unique (packaging_drawing),
    constraint fk_packaging_labeling foreign key (labeling_id)
    references labeling (labeling_id) on delete cascade on update restrict,
    constraint pk_packaging primary key (packaging_id)
)
'''

create_table_assortment = '''
create table if not exists assortment (
    item_id smallint unsigned not null auto_increment,
    factory_code varchar(30) not null,
    item_model varchar(10),
    description varchar(200) not null,
    series varchar(20),
    net_weight_kg float(5, 2) unsigned,
    gross_weight_kg float(5, 2) unsigned,
    labeling_id smallint unsigned not null,
    packaging_id smallint unsigned not null,
    product_id smallint unsigned not null,
    constraint UQ_factory_code unique (factory_code),
    constraint fk_assortment_labeling foreign key (labeling_id)
    references labeling (labeling_id) on delete cascade on update restrict,
    constraint fk_assortment_packaging foreign key (packaging_id)
    references packaging (packaging_id) on delete cascade on update restrict,
    constraint fk_assortment_products foreign key (product_id)
    references products (product_id) on delete cascade on update restrict,
    constraint pk_assortment primary key (item_id)
)
'''

create_table_shipment_from_china = '''
create table if not exists shipment_from_china (
    shipment_id smallint unsigned not null auto_increment,
    container_num_short varchar(10) not null,
    container_num_long varchar(11) not null,
    departure_date date not null,
    eta date not null,
    arrival_date date not null,
    station varchar(20),
    ci_number varchar(20),
    arrival_status enum('прибыл', 'в пути') not null default 'в пути',
    custom_clearance enum('растаможен', 'не растаможен') not null default 'не растаможен',
    gtd varchar(23),
    item_quantity int unsigned not null,
    item_id smallint unsigned not null,
    constraint fk_shipment_from_china_assortment foreign key (item_id)
    references assortment (item_id) on delete cascade on update restrict,
    constraint pk_shipment_from_china primary key (shipment_id)
)
'''

create_table_warehouses = '''
create table if not exists warehouses (
    wh_id smallint unsigned not null auto_increment,
    wh_name varchar(50) not null,
    country varchar(20) not null,
    zip varchar(20),
    city varchar(20) not null,
    street varchar(30) not null,
    building varchar(10) not null,
    staff_id smallint unsigned not null,
    customer_id smallint unsigned not null,
    provider_id smallint unsigned not null,
    constraint fk_warehouses_staff foreign key (staff_id)
    references staff (staff_id) on delete cascade on update restrict,
    constraint fk_warehouses_customers foreign key (customer_id)
    references customers (customer_id) on delete cascade on update restrict,
    constraint fk_warehouses_providers foreign key (provider_id)
    references providers (provider_id) on delete cascade on update restrict,
    constraint pk_warehouses primary key (wh_id)
)
'''

create_table_transport = '''
create table if not exists transport (
    transport_id smallint unsigned not null auto_increment,
    transport_model varchar(15) not null,
    load_capacity smallint unsigned not null,
    car_plate varchar(10) not null,
    constraint pk_transport primary key (transport_id)
)
'''

create_table_delivery_to_customers = '''
create table if not exists delivery_to_customers (
    delivery_id smallint unsigned not null auto_increment,
    item_quantity int unsigned not null,
    gtd varchar(23),
    departure_date date not null,
    arrival_date date not null,
    shipping_wh_id smallint unsigned not null,
    customer_id smallint unsigned not null,
    item_id smallint unsigned not null,
    staff_id smallint unsigned not null,
    provider_id smallint unsigned not null,
    transport_id smallint unsigned not null,
    constraint fk_delivery_to_customers_warehouses foreign key (shipping_wh_id)
    references warehouses (wh_id) on delete cascade on update restrict,
    constraint fk_delivery_to_customers_providers foreign key (provider_id)
    references providers (provider_id) on delete cascade on update restrict,
    constraint fk_delivery_to_customers_transport foreign key (transport_id)
    references transport (transport_id) on delete cascade on update restrict,
    constraint pk_delivery_to_customers primary key (delivery_id)
)
'''

create_table_moving_around_warehouses = '''
create table if not exists moving_around_warehouses (
    moving_id smallint unsigned not null auto_increment,
    item_quantity int unsigned not null,
    gtd varchar(23),
    departure_date date not null,
    arrival_date date not null,
    shipping_wh_id smallint unsigned not null,
    recieving_wh_id smallint unsigned not null,
    item_id smallint unsigned not null,
    staff_id smallint unsigned not null,
    provider_id smallint unsigned not null,
    constraint fk_moving_around_warehouses_shipping_warehouses foreign key (shipping_wh_id)
    references warehouses (wh_id) on delete cascade on update restrict,
    constraint fk_moving_around_warehouses_recieving_warehouses foreign key (recieving_wh_id)
    references warehouses (wh_id) on delete cascade on update restrict,
    constraint fk_moving_around_warehouses_assortment foreign key (item_id)
    references assortment (item_id) on delete cascade on update restrict,
    constraint fk_moving_around_warehouses_staff foreign key (staff_id)
    references staff (staff_id) on delete cascade on update restrict,
    constraint fk_moving_around_warehouses_providers foreign key (provider_id)
    references providers (provider_id) on delete cascade on update restrict,
    constraint pk_moving_around_warehouses primary key (moving_id)
)
'''

# # uploading branch data
# branch_data = '''
# load data local infile './branch.csv'
# into table branch
# fields terminated by ';' 
# lines terminated by '\n' 
# ignore 1 rows
# (branch_id, country, city);
# '''

# execution sql scripts
cursor.execute(create_logistics_db)
cursor.execute(use_logistics_db)
cursor.execute(create_table_branch)
cursor.execute(create_table_departments)
cursor.execute(create_table_staff)
cursor.execute(create_table_customers)
cursor.execute(create_table_customer_contacts)
cursor.execute(create_table_providers)
cursor.execute(create_table_provider_contacts)
cursor.execute(create_table_products)
cursor.execute(create_table_labeling)
cursor.execute(create_table_packaging)
cursor.execute(create_table_assortment)
cursor.execute(create_table_shipment_from_china)
cursor.execute(create_table_warehouses)
cursor.execute(create_table_transport)
cursor.execute(create_table_delivery_to_customers)
cursor.execute(create_table_moving_around_warehouses)
cnx.commit()

if cnx.is_connected():
    cursor.close()
    cnx.close()