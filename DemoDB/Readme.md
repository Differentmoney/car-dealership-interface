# JJDATA 
Contains the csv files with the provided demo data converted to support our current db schema. The Schema creation file is called JJDB which will create the tables but not populate them. The data in these CSVs can be imported into the respective tables via MySQL workbench. 
- Click Schema tab in upper left area
- Select cs6400_fall21_team005 database
- Open tables tab
- Right-click on the table and select Table Data Import Wizard.
- Follow the steps to import data
The order they files are to be imported is as follows:

Manufacturer
Color
User
Customer
Individual
Business
VehicleType
Vehicle
VehicleColor
SellVehicle
Repair
Parts

# Dump File
Alternatively, the Dump folder contains the sql creation script for each tables. Similar to the order mentioned above, after JJDB sql script is run, these scripts can be run to recreate and populate your tables with the data.

The order they files are to be imported is as follows:
Manufacturer
Color
User
Customer
Individual
Business
VehicleType
Vehicle
VehicleColor
SellVehicle
Repair
Parts

