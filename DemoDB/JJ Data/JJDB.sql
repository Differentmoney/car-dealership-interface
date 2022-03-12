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
 username varchar(50) NOT NULL,  
 password varchar(50) NOT NULL,
 firstname varchar(50) NOT NULL,
 lastname varchar(50) NOT NULL,
 role varchar(50) NOT NULL,
 PRIMARY KEY (username)
);

CREATE TABLE Customer(
 customerID int(10) NOT NULL AUTO_INCREMENT,
 phonenumber varchar(10) NOT NULL,
 address varchar(100) NOT NULL,
 email varchar(50) NULL,
 PRIMARY KEY (customerID)
);

CREATE TABLE Individual(
 driverlicensenumber varchar(50) NOT NULL,  
 customerID int(10) NOT NULL,
 firstname varchar(50) NOT NULL,
 lastname varchar(50) NOT NULL,
 PRIMARY KEY (driverlicensenumber),
 UNIQUE KEY customerID (customerID)
);

CREATE TABLE Business(
 taxID varchar(50) NOT NULL,
 customerID int(10) NOT NULL,
 businessname varchar(50) NOT NULL,
 primarycontactname varchar(50) NOT NULL,
 primarycontacttitle varchar(50) Not NULL,
 PRIMARY KEY (taxID),
 UNIQUE KEY customerID (customerID)
);

CREATE TABLE Vehicle(
 vin varchar(50) NOT NULL,
 model varchar(50) NOT NULL,
 modelyear varchar(5) NOT NULL,
 Listprice double(10, 2) NOT NULL,
 Invoiceprice double(10, 2) NOT NULL,
 description varchar(500) NULL, 
 username varchar(50) NOT NULL,
 adddate date NOT NULL,
 vehicletypenumber int(10) NOT NULL,
 manufacturerID int(5) NOT NULL,
 PRIMARY KEY (vin)
);

CREATE TABLE Manufacturer(
 manufacturerID int(5),
 manufacturername varchar(50) NOT NULL,
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
 username varchar(50) NOT NULL,
 odometer int(6) NOT NULL,
 laborcharge double(10, 2) NULL,
 description varchar(500) NOT NULL,
 completedate Date NULL,
 PRIMARY KEY (vin, customerID, startdate)
);

CREATE TABLE Part(
 vin varchar(17) NOT NULL,
 customerID int(10) NOT NULL,
 startdate Date NOT NULL,
 partnumber varchar(50) NOT NULL,
 quantity int(5) NOT NULL,  
 price double(10, 2) NOT NULL,
 vendorname varchar(50) NOT NULL,
 PRIMARY KEY (vin, customerID, startdate, partnumber)
);

CREATE TABLE SellVehicle(
 vin varchar(50) NOT NULL,
 customerID int(10) NOT NULL,
 username varchar(50) NOT NULL,
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


-- USE cs6400_fall21_team005;

-- AddManufacturer
-- insert into manufacturer(manufacturerid, manufacturername)
-- values('1','Acura'),('2','Alfa Romeo'),('3','Aston Martin'),('4','Audi'),('5','Bentley'),('6','BMW'),('7','Buick'),('8','Cadillac'),('9','Chevrolet'),
-- ('10','Chrysler'),('11','Dodge'),('12','Ferrari'),('13','FIAT'),('14','Ford'),('15','Freightliner'),('16','Genesis'),('17','GMC'),('18','Honda'),('19','Hyundai'),
-- ('20','INFINI'),('21','Jaguar'),('22','Jeep'),('23','Kia'),('24','Lamborghini'),('25','Land Rover'),('26','Lexus'),('27','Lincoln'),('28','Lotus'),
-- ('29','Maserati'),('30','MAZDA'),('31','McLaren'),('32','Mercedes-Benz'),('33','MINI'),('34','Mitsubishi'),('35','Nissan'),('36','Porsche'),('37','Ram'),
-- ('38','Rolls-Royce'),('39','SAAB'),('40','smart'),('41','Subaru'),('42','Tesla'),('43','Toyota'),('44','Vauxhall'),('45','Volkswagen'),('46','Volvo');

-- Color
-- insert into color(colorid, color)
-- values ('1', 'Aluminum'),('2','beige'),('3','Black'),('4','Blue'),('5','Brown'),('6','Bronze'),('7','Claret'),('8','Copper'),('9','Cream'),('10','Gold'),
-- ('11','Gray'),('12','Green'),('13','Maroon'),('14','Metallic'),('15','Navy'),('16','Orange'),('17','Pink'),('18','Purple'),('19','Red'),('20','Rose'),
-- ('21','Rust'),('22','Silver'),('23','Tan'),('24','Turquoise'),('25','White'),('26','Yellow');
