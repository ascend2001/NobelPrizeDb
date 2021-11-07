drop table if exists PersonName, OrgName, NobelPrize, Affiliations;
create table Affiliations(name varchar(200),city varchar(100), country varchar(100), awardYear int, category varchar(100), sortOrder int, id int, primary key (name, awardYear, category, sortOrder, id));
create table NobelPrize(awardYear int, category varchar(500), sortOrder int, id int, primary key(awardYear, category, sortOrder));
create table OrgName(id INT PRIMARY KEY, OrgName varchar(500), DateFounded date, City varchar(500), Country varchar(500));
create table PersonName(id INT PRIMARY KEY, givenName varchar(500), familyName varchar(500), DOB date, gender varchar(10), city varchar(500), country varchar(500));
load data local infile './PersonName.del' into table Movie fields terminated by ',' optionally enclosed by '"';
load data local infile './OrgName.del' into table Actor fields terminated by ',' optionally enclosed by '"';
load data local infile './NobelPrize.del' into table Actor fields terminated by ',' optionally enclosed by '"';
load data local infile './Affiliations.del' into table Actor fields terminated by ',' optionally enclosed by '"';