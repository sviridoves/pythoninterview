import sqlite3

db_path = 'l_db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

cur.executescript(""" 
    create table if not exists categories( 
        category_name char(150) primary key not null, 
        category_description char(250) not null
    ); 
    create table if not exists units( 
        unit char(50) primary key not null
    ); 
    create table if not exists positions( 
        position char(150) primary key not null
    ); 
""")

cur.executescript(""" 
    create table if not exists goods( 
        good_id int primary key not null, 
        good_name char(250) not null,
        good_unit char(50),
        good_cat char(150),
        FOREIGN KEY(good_unit) REFERENCES units(unit),
        FOREIGN KEY(good_cat) REFERENCES categories(category_name)
    ); 
    create table if not exists employees( 
        employee_id int primary key not null, 
        employee_fio char(250) not null,
        employee_position char(50),
        FOREIGN KEY(employee_position) REFERENCES positions(position)
    ); 
    create table if not exists vendors( 
        vendor_id int primary key not null, 
        vendor_name char(250) not null,
        vendor_ownerchipform char(50),
        vendor_address char(250),
        vendor_phone char(20),
        vendor_email char(100)
    ); 
""")

conn.commit()
conn.close()
