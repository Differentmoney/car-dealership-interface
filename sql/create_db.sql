-- CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
CREATE USER IF NOT EXISTS gatechUser@localhost IDENTIFIED BY 'gatech123';

DROP DATABASE IF EXISTS `cs6400_fall21_team005`;
SET default_storage_engine=InnoDB;
SET NAMES utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE DATABASE IF NOT EXISTS cs6400_fall21_team005
   DEFAULT CHARACTER SET utf8mb4
   DEFAULT COLLATE utf8mb4_unicode_ci;
USE cs6400_fall21_team005;

GRANT SELECT, INSERT, UPDATE, DELETE, FILE ON *.* TO 'gatechUser'@'localhost';
GRANT ALL PRIVILEGES ON `gatechuser`.* TO 'gatechUser'@'localhost';
GRANT ALL PRIVILEGES ON `cs6400_fall21_team005`.* TO 'gatechUser'@'localhost';
FLUSH PRIVILEGES;

-- Tables

CREATE TABLE User(
 username varchar(25) NOT NULL,  
 password varchar(25) NOT NULL,
 firstname varchar(25) NOT NULL,
 lastname varchar(25) NOT NULL,
 role varchar(25) NOT NULL,
 PRIMARY KEY (username)
);

CREATE TABLE Customer(
 customerID int(10) NOT NULL AUTO_INCREMENT,
 phonenumber varchar(10) NOT NULL,
 address varchar(50) NOT NULL,
 email varchar(25) NULL,
 PRIMARY KEY (customerID)
);

CREATE TABLE Individual(
 driverlicensenumber varchar(25) NOT NULL,  
 customerID int(10) NOT NULL,
 firstname varchar(25) NOT NULL,
 lastname varchar(25) NOT NULL,
 PRIMARY KEY (driverlicensenumber),
 UNIQUE KEY customerID (customerID)
);

CREATE TABLE Business(
 taxID varchar(25) NOT NULL,
 customerID int(10) NOT NULL,
 businessname varchar(25) NOT NULL,
 primarycontactname varchar(50) NOT NULL,
 primarycontacttitle varchar(25) Not NULL,
 PRIMARY KEY (taxID),
 UNIQUE KEY customerID (customerID)
);

CREATE TABLE Vehicle(
 vin varchar(17) NOT NULL,
 model varchar(25) NOT NULL,
 modelyear varchar(5) NOT NULL,
 Listprice double(10, 2) NOT NULL,
 Invoiceprice double(10, 2) NOT NULL,
 description varchar(250) NULL, 
 username varchar(25) NOT NULL,
 adddate date NOT NULL,
 vehicletypenumber int(10) NOT NULL,
 manufacturerID int(5) NOT NULL,
 PRIMARY KEY (vin)
);

CREATE TABLE Manufacturer(
 manufacturerID int(5),
 manufacturername varchar(25) NOT NULL,
 PRIMARY KEY (manufacturerID)
);

CREATE TABLE VehicleType(
 vehicletypenumber int(10) NOT NULL AUTO_INCREMENT,
 vehicletype varchar(100) NOT NULL,
 vehicledetail varchar(100) NOT NULL,
 PRIMARY KEY (vehicletypenumber)
);

CREATE TABLE VehicleColor(
 vin varchar(17) NOT NULL,
 colorID int(5) NOT NULL,
 PRIMARY KEY (vin, colorID)
);

CREATE TABLE Color(
 colorID int(5) NOT NULL,
 color varchar(9) NOT NULL,
 PRIMARY KEY (colorID)
);


CREATE TABLE Repair(
 vin varchar(17) NOT NULL,
 customerID int(10) NOT NULL,  
 startdate Date NOT NULL,
 username varchar(25) NOT NULL,
 odometer int(6) NOT NULL,
 laborcharge double(10, 2) NULL,
 description varchar(250) NOT NULL,
 completedate Date NULL,
 PRIMARY KEY (vin, customerID, startdate)
);

CREATE TABLE Part(
 vin varchar(17) NOT NULL,
 customerID int(10) NOT NULL,
 startdate Date NOT NULL,
 partnumber varchar(25) NOT NULL,
 quantity int(5) NOT NULL,  
 price double(10, 2) NOT NULL,
 vendorname varchar(25) NOT NULL,
 PRIMARY KEY (vin, customerID, startdate, partnumber)
);

CREATE TABLE SellVehicle(
 vin varchar(17) NOT NULL,
 customerID int(10) NOT NULL,
 username varchar(25) NOT NULL,
 soldprice double(10, 2) NOT NULL,
 solddate Date NOT NULL,  
 PRIMARY KEY (vin, customerID, username)
);


-- Constraints	Foreign Keys: FK_ChildTable_childColumn_ParentTable_parentColumn

ALTER TABLE Individual
 ADD CONSTRAINT fk_Individual_customerID_Customer_customerID FOREIGN KEY 
(customerID) REFERENCES Customer (customerID);

ALTER TABLE Business
 ADD CONSTRAINT fk_Business_customerID_Customer_customerID FOREIGN KEY 
(customerID) REFERENCES Customer (customerID);

ALTER TABLE Vehicle
 ADD CONSTRAINT fk_Vehicle_manufacturername_Manufacturer_manufacturername 
FOREIGN KEY (manufacturerID) REFERENCES Manufacturer (manufacturerID);
ALTER TABLE Vehicle
 ADD CONSTRAINT fk_Vehicle_typename_VehicleType_typename FOREIGN KEY 
(vehicletypenumber) REFERENCES VehicleType (vehicletypenumber);

ALTER TABLE Vehicle
 ADD CONSTRAINT fk_Vehicle_username_User_username FOREIGN KEY 
(username) REFERENCES User (username);

ALTER TABLE VehicleColor
 ADD CONSTRAINT fk_VehicleColor_vin_Vehicle_vin FOREIGN KEY (vin) REFERENCES 
Vehicle (vin);

ALTER TABLE VehicleColor
 ADD CONSTRAINT fk_VehicleColor_colorID_Color_colorID FOREIGN KEY 
(colorID) REFERENCES Color (colorID);

ALTER TABLE Repair
 ADD CONSTRAINT fk_Repair_vin_Vehicle_vin FOREIGN KEY (vin) REFERENCES 
Vehicle (vin);
ALTER TABLE Repair
 ADD CONSTRAINT fk_Repair_customerID_Customer_customerID FOREIGN KEY 
(customerID) REFERENCES Customer (customerID);
ALTER TABLE Repair
 ADD CONSTRAINT fk_Repair_username_User_username FOREIGN KEY 
(username) REFERENCES User (username);


ALTER TABLE Part
 ADD CONSTRAINT fk_Part_RepairNum_Repairs_RepairNum
FOREIGN KEY (vin, customerID, startdate) REFERENCES Repair 
(vin, customerID, startdate);

ALTER TABLE SellVehicle
 ADD CONSTRAINT fk_SellVehicle_vin_Vehicle_vin FOREIGN KEY (vin) REFERENCES 
Vehicle (vin);

ALTER TABLE SellVehicle
 ADD CONSTRAINT fk_SellVehicle_username_User_username FOREIGN KEY 
(username) REFERENCES User (username);

ALTER TABLE SellVehicle
 ADD CONSTRAINT fk_SellVehicle_customerID_Customer_customerID FOREIGN KEY 
(customerID) REFERENCES Customer (customerID);

USE cs6400_fall21_team005;

-- AddManufacturer
insert into manufacturer(manufacturerid, manufacturername)
values('1','Acura'),('2','Alfa Romeo'),('3','Aston Martin'),('4','Audi'),('5','Bently'),('6','BMW'),('7','Buick'),('8','Cadillac'),('9','Chevrolet'),
('10','Chrysler'),('11','Dodge'),('12','Ferrari'),('13','FIAT'),('14','Ford'),('15','Freightliner'),('16','Genesis'),('17','GMC'),('18','Honda'),('19','Hyundai'),
('20','INFINITY'),('21','Jaguar'),('22','Jeep'),('23','Kia'),('24','Lamborghini'),('25','Land Rover'),('26','Lexus'),('27','Lincoln'),('28','Lotus'),
('29','Maserati'),('30','MAZDA'),('31','McLaren'),('32','Mercedes-Benz'),('33','MINI'),('34','Mitsubishi'),('35','Nissan'),('36','Porsche'),('37','Ram'),
('38','Rolls-Royce'),('39','SAAB'),('40','smart'),('41','Subaru'),('42','Tesla'),('43','Toyota'),('44','Vauxhall'),('45','Volkswagen'),('46','Volvo');


-- AddVehicleType
insert into vehicletype(vehicletypenumber, vehicletype, vehicledetail)
values
('1', 'car', 'N/A'),
('2', 'truck', 'N/A'),
('3', 'minivan', 'N/A'),
('4', 'SUV', 'N/A'),
('5', 'sedan', 'N/A');

insert into user(username, password, firstname, lastname, role)
values('Raround', 'pwd', 'Roland', 'Around', 'Owner'),
      ('Sstone', 'pwd', 'Sam', 'Stone', 'Salesperson'),
      ('Ssmith', 'pwd', 'Sarah', 'Smith', 'Salesperson'),
      ('Ssmallcomb', 'pwd', 'Sierra', 'Smallcomb', 'Salesperson'),
      ('Ikelley', 'pwd', 'Ines', 'Kelley', 'Inventory Clerk'),
      ('Ilannister', 'pwd', 'Imp', 'Lannister', 'Inventory Clerk'),
      ('Mstone', 'pwd', 'Michael', 'Stone', 'Manager'),
      ('Mmiller', 'pwd', 'Marlen', 'Miller', 'Manager'),
      ('Mdavis', 'pwd', 'Maria', 'Davis', 'Manager'),
      ('Wlopez', 'pwd', 'White', 'Lopez', 'Service Writer'),
      ('Wjones', 'pwd', 'William', 'Jones', 'Service Writer');

-- Customer (Since CutomberID is an auto increment primary key in Customer table, I think we have to decide if it is an individual or a business first. 
-- Then we need to capture the customerID and input it into either Individual table or Business Table. Insert two rows at a time. 
-- If we dump all customer data in at once, we'll lose track of the customerID. Feel free ro revise if there are efficient ways to do this.

-- Customers who are Individual

insert into customer(customerid, phonenumber, address, email)
values (DEFAULT, '5980869980', '5 Marie Ave, Atlanta GA', 'fwxcfchvj@gatech.edu');

insert into individual(driverlicensenumber, customerid, firstname, lastname)
values('S108686902',LAST_INSERT_ID(), 'Bob', 'Sponge');

insert into customer(customerid, phonenumber, address, email)
values (DEFAULT,'4837064567', '12 Main Street, Boston MA', '1ggj@yahoo.com');

insert into individual(driverlicensenumber, customerid, firstname, lastname)
 values ('S802055763',LAST_INSERT_ID(), 'Will', 'Lee');
 
insert into customer(customerid, phonenumber, address, email)
values (DEFAULT,'6837564567', '23 Massachusetts Ave, Brighton MA', 'Jmoth@gmail.com');

insert into individual(driverlicensenumber, customerid, firstname, lastname)
values ('S424422222',LAST_INSERT_ID(), 'Leo', 'White');

insert into customer(customerid, phonenumber, address, email)
values (DEFAULT,'7837064562', '20 Guest Street, Boston MA', 'owen24@yahoo.com');

insert into individual(driverlicensenumber, customerid, firstname, lastname)
values ('S157965333',LAST_INSERT_ID(), 'Steve', 'Perez');

insert into customer(customerid, phonenumber, address, email)
values (DEFAULT,'9837264564', '90 Sugarhill Street, Boston MA', 'fwegj@outlook.com');

insert into individual(driverlicensenumber, customerid, firstname, lastname)
 values ('S104223888',LAST_INSERT_ID(), 'Taylor', 'Smith');

-- Customers who are Business        
        
insert into customer(customerid, phonenumber, address, email)
values (DEFAULT,'4837064544', '1 Main Street, Lowell MA', 'klhbi92@yahoo.com');

insert into business(taxID, customerid, businessname, primarycontactname, primarycontacttitle)
values ('T37067433', LAST_INSERT_ID(),'WEE', 'Stephen Lee','Manager');
		
insert into customer(customerid, phonenumber, address, email)
values (DEFAULT,'3583706452', '66 Ames Street, Sharon MA', 'mohg921@gatech.edu');

insert into business(taxID, customerid, businessname, primarycontactname, primarycontacttitle)
values ('T68657655', LAST_INSERT_ID(),'Hah', 'Jeffery Lopez','Principle');

insert into customer(customerid, phonenumber, address, email)
values (DEFAULT,'1830064564', '781 Main Street, Boston MA', 'pwn812@yahoo.com');

insert into business(taxID, customerid, businessname, primarycontactname, primarycontacttitle)
values ('T86857522', LAST_INSERT_ID(),'GoGo', 'James Albany','Sales');

insert into customer(customerid, phonenumber, address, email)
values (DEFAULT,'1897679302', '21 Candy Hill Road, Lexington MA','y8686@gmail.com');

insert into business(taxID, customerid, businessname, primarycontactname, primarycontacttitle)
values ('T03855522', LAST_INSERT_ID(),'Hulala', 'Jimmy Wu','Secretary');
 

-- AddVehicle
insert into vehicle(vin, model, modelyear, invoiceprice, listprice, description, username, adddate, vehicletypenumber,manufacturerid)
values
('111', 'M1','2000','2000','2500','N/A','Ikelley','2002-03-04','1','1'),
('112', 'M1','2001','2000','2500','N/A','Ikelley','2002-03-04','2','2'),
('113', 'M1','2001','2000','2500','N/A','Ikelley','2002-03-04','3','3'),
('114', 'M1','2001','2000','2500','N/A','Ilannister','2002-03-04','4','4'),
('115', 'M1','2003','2000','2500','N/A','Ilannister','2002-03-04','5','5'),
('116', 'M1','2002','1750','2500','N/A','Ilannister','2004-01-22','1','1'),
('117', 'M1','2002','1850','2500','N/A','Ikelley','2020-10-22','2','2'),
('118', 'M1','2002','2000','2500','N/A','Ilannister','2020-10-22','3','3'),
('119', 'M2','2002','2000','2500','N/A','Ilannister','2020-10-22','4','4'),
('120', 'M2','2002','2000','2500','N/A','Ikelley','2019-02-13','1','1'),
('121', 'M2','2004','2000','2500','N/A','Ikelley','2021-02-13','2','2'),
('122', 'M2','2004','2200','2500','N/A','Ikelley','2021-06-13','4','4'),
('130', 'M2','2005','2000','2500','N/A','Ilannister','2002-03-04','2','2'),
('131', 'M2','2009','2000','2500','N/A','Raround','2020-03-04','3','3'),
('132', 'M2','2011','2000','2500','N/A','Raround','2012-03-04','4','4'),
('133', 'M2','2020','2000','2500','N/A','Raround','2021-03-04','5','5');


-- SellVehicle
insert into sellvehicle(vin, customerid,username, soldprice, solddate)
values 
('111', '1', 'Sstone', '2000', '2004-01-22'),
('112', '2', 'Ssmith', '3000', '2004-01-22'),
('113', '1', 'Sstone', '2123', '2004-01-22'),
('114', '2', 'Ssmith', '1800', '2004-01-22');

-- Color
insert into color(colorid, color)
values ('1', 'Aluminum'),('2','beige'),('3','Black'),('4','Blue'),('5','Brown'),('6','Bronze'),('7','Claret'),('8','Copper'),('9','Cream'),('10','Gold'),
('11','Gray'),('12','Green'),('13','Maroon'),('14','Metallic'),('15','Navy'),('16','Orange'),('17','Pink'),('18','Purple'),('19','Red'),('20','Rose'),
('21','Rust'),('22','Silver'),('23','Tan'),('24','Turquoise'),('25','White'),('26','Yellow');


-- VehicleColor
insert into vehiclecolor(vin, colorid)
values
('111', '1'),
('111', '2'),
('112', '3'),
('113', '3'),
('114', '5'),
('115', '4'),
('116', '4'),
('117', '2'),
('117', '4'),
('118', '2'),
('118', '4'),
('122', '5');

-- Repair
insert into repair(vin, customerid, startdate, username, odometer, laborcharge, description, completedate)
values('111', '1', '2004-01-22', 'Wlopez', '12344', '230' , 'N/A', '2004-04-22'),
	('112', '2', '2004-01-22', 'Wlopez', '12344', '230' , 'N/A', '2004-04-22'),
    ('113', '1', '2004-01-22', 'Wlopez', '12344', '230' , 'N/A', '2004-04-22'),
    ('114', '2', '2004-01-22', 'Wjones', '12344', '230' , 'N/A', '2004-04-22'),
    ('115', '1', '2004-01-22', 'Wjones', '12344', '230' , 'N/A', '2004-04-22'),
    ('116', '2', '2004-01-22', 'Wjones', '12344', '230' , 'N/A', '2004-04-22');
       


-- Parts
insert into part(vin, customerid, startdate, partnumber, quantity, price, vendorname)
values('111','1','2004-01-22', '1', '2','23', 'aa'), 
	  ('111','1','2004-01-22', '2', '3','40', 'aa'), 
      ('111','1','2004-01-22', '3', '2','23', 'aa');
      




      





