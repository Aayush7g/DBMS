CREATE DATABASE contact;
use contact;

CREATE TABLE sign_up (
    sr_no INT unique key NOT NULL auto_increment,
    name VARCHAR(25) NOT NULL,
    email_address VARCHAR(50) NOT NULL unique,
    password VARCHAR(10) NOT NULL,
    repeat_password VARCHAR(10) NOT NULL
);
select * from sign_up;

CREATE TABLE contacts (
   sr_no int primary key auto_increment not null,
   name varchar(1554) not null,
   email_address varchar(55),
   phone_number varchar(55), 
   message varchar(562)
);	

create table post(
title varchar(500) not null,
sr_no int primary key auto_increment not null,
post varchar(3222) not null,
post_date_time timestamp default current_timestamp not null
);

select * from contacts;
delete from contacts where sr_no = 1;

