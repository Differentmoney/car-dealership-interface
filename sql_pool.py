import db_config as config
import connect as con
import os
import entities.vehicle as ev
import entities.repair as er
from datetime import date

class Repair:
    def searchVehicle(vin):
        conn = con.getConnection()
        sql = "SELECT vf.vin, vf.model, vf.modelyear, vf.description, vf.vehiclecolor, vt.vehicletype, vt.vehicledetail, m.manufacturername FROM VehicleType AS vt, Manufacturer AS m, (SELECT v.vin, v.model, v.modelyear, v.description, v.vehicletypenumber, v.manufacturerID, CONCAT(GROUP_CONCAT(vcc.color SEPARATOR ', ')) 'vehiclecolor' FROM vehicle AS v LEFT JOIN (SELECT vc.vin, c.color FROM Vehiclecolor as vc, color as c WHERE vc.colorID = c.colorID) as vcc ON v.vin = vcc.vin GROUP BY v.vin) as vf WHERE vf.vehicletypenumber = vt.vehicletypenumber AND vf.manufacturerID = m.manufacturerID AND vf.vin = '%s';"
        cur = conn[1].cursor(buffered=True)
        cur.execute(sql, (vin))
        result = cur.fetchall()
        if cur.rowcount == 1:
            return True
        else:
            return False


    def create_repair(vin, CId, username, Des, Odo, Labo):
        conn = con.getConnection()
        allNull = True
        if(len(Des) == 0):
            Des = "N/A"
        sql = "INSERT INTO Repair (vin, customerID, startdate, username, description, odometer, laborcharge) VALUES ('" + vin + "' , '" + CId + "' , date(curdate()) , '" + username +"' , '" + Des + "' , '" + Odo + "' , '" + Labo + "') ;"
        print(sql)
        cur = conn[1].cursor()
        cur.execute(sql)
        conn[1].commit()
        return vin
    
    def add_part ( vin, CId, PartNumber, Quantity , Price ,VendorName):
        conn = con.getConnection()
        sql = "INSERT INTO Part (vin, customerID, startdate, partnumber, quantity, price, vendorname) VALUES ('" + vin + "' , '" + CId + "' , date(curdate()) , '" + PartNumber + "' , '" + Quantity + "' , '" + Price + "' , '" +  VendorName + "');"
        cur = conn[1].cursor()
        cur.execute(sql)
        conn[1].commit()
        return vin

class login:
    #Checks if the user is in the database and returns user role
    def validation(usr, pwd):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            cur.execute("SELECT role FROM User WHERE username = %s AND password = %s", (usr, pwd))
            result = cur.fetchall()
            if cur.rowcount == 1:
                return result[0][0]
            else:
                return False
         
class Customer():
    # Add Individual 
    def addIndivudal(phonenumber, address, email, driverlicensenumber, firstname, lastname):
        conn = con.getConnection()
        if conn[0]:   

            cur = conn[1].cursor()
            #Insert into Customer Table
            add_customer = (phonenumber, address, email)
            sql = "INSERT INTO Customer (phonenumber, address, email) VALUES (%s, %s, %s)"
            cur.execute(sql, add_customer)
            conn[1].commit()      

            #Insert into Indivudal table
            id = cur.lastrowid
            add_individual = (driverlicensenumber,id, firstname, lastname)
            sql = "INSERT INTO Individual (driverlicensenumber, customerID, firstname, lastname) VALUES (%s, %s, %s, %s)"
            cur.execute(sql, add_individual)
            conn[1].commit()

            return id
    
    # Add Busness
    def addBuisness(phonenumber, address, email, taxID, bn, pcn, pct):
         conn = con.getConnection()
         if conn[0]:
            cur = conn[1].cursor()
            #Insert into Cutomer Table
            add_customer = (phonenumber, address, email)
            sql = "INSERT INTO Customer ( phonenumber, address, email) VALUES (%s, %s, %s)"
            cur.execute(sql, add_customer)
            conn[1].commit()
            
            #Insert into Buisness Table
            id = cur.lastrowid
            add_buisness = (taxID, id, bn, pcn, pct)
            sql = "INSERT INTO Business (taxID, customerID, businessname, primarycontactname, primarycontacttitle) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sql, add_buisness)
            conn[1].commit()

            return id
    
    def check_driverslicense (driverlicensenumber):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            cur.execute("SELECT driverlicensenumber FROM Individual WHERE driverlicensenumber = '%s'" % driverlicensenumber)
            row = cur.fetchall()
            if cur.rowcount == 1:
                return True
            else:
                return False
    
    def check_taxid (taxID):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            cur.execute("SELECT taxID FROM Business WHERE taxID = '%s'" % taxID)
            row = cur.fetchall()
            if cur.rowcount == 1:
                return True
            else:
                return False


class SearchCustomer:
    # search customer by Driverslicensenumber
    def search_by_driverlicensenumber(number):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            sql = "SELECT Customer.email, Customer.address, Customer.phonenumber, Individual.driverlicensenumber, Individual.firstname, Individual.lastname, Individual.customerID FROM Individual INNER JOIN Customer ON Customer.customerID = Individual.customerID WHERE Individual.driverlicensenumber='"
            sql = sql + number + "'"
            cur.execute(sql) 
            result = cur.fetchall()
            return result


    # search customer by TaxID
    def search_by_TaxID (taxid):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            sql = "SELECT Customer.email, Customer.address, Customer.phonenumber, Business.taxID, Business.businessname, Business.primarycontactname, Business.primarycontacttitle, Business.customerID FROM Business INNER JOIN Customer ON Customer.customerID = Business.customerID WHERE Business.taxID='"
            sql = sql + taxid + "'"
            cur.execute(sql)
            result = cur.fetchall()
            return result

            
class Report:
    # generate report for sales by color
    def sales_by_color():
        conn = con.getConnection()
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        if conn[0]:
            cur = conn[1].cursor()
            filename = absolute_path + '/sql/color_report.sql'
        with open(filename) as f:
            cur.execute(f.read())
        result = cur.fetchall()
        #col_names = cur.description
        return result

    # generate report for sales by type
    def sales_by_type():
        conn = con.getConnection()
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        if conn[0]:
            cur = conn[1].cursor()
            filename = absolute_path + '/sql/type_report.sql'
        with open(filename) as f:
            cur.execute(f.read())
        result = cur.fetchall()
        return result

    # generate report for sales by manufacturer
    def sales_by_manufacturer():
        conn = con.getConnection()
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        if conn[0]:
            cur = conn[1].cursor()
            filename = absolute_path + '/sql/manufacturer_report.sql'
        with open(filename) as f:
            cur.execute(f.read())
        result = cur.fetchall()
        return result

    # generate report for below cost sales
    def below_cost_sales():
        conn = con.getConnection()
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        if conn[0]:
            cur = conn[1].cursor()
            filename = absolute_path + '/sql/below_cost_sales.sql'
        with open(filename) as f:
            cur.execute(f.read())
        result = cur.fetchall()
        return result

    # generate report for avg time in inventory
    def avg_time_in_inventory():
        conn = con.getConnection()
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        if conn[0]:
            cur = conn[1].cursor()
            filename = absolute_path + '/sql/avg_time.sql'
        with open(filename) as f:
            cur.execute(f.read())
        result = cur.fetchall()
        return result
    
    # generate report for part statistics
    def part_statistics():
        conn = con.getConnection()
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        if conn[0]:
            cur = conn[1].cursor()
            filename = absolute_path + '/sql/part_stat.sql'
        with open(filename) as f:
            cur.execute(f.read())
        result = cur.fetchall()
        return result

    # generate report for gross customer income
    def gross_customer_income():
        conn = con.getConnection()
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        if conn[0]:
            cur = conn[1].cursor()
            filename = absolute_path + '/sql/gross_income.sql'
        with open(filename) as f:
            cur.execute(f.read())
        result = cur.fetchall()
        return result

    # gross customer drilldown 1
    def gross_drill1(CID):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            sql = 'SELECT soldDate, soldPrice, S.VIN, ModelYear, M.ManufacturerName, Model, CONCAT(U.FirstName, " ", U.LastName) name FROM Vehicle V, SellVehicle S, User U, Manufacturer M WHERE S.Username = U.Username AND V.Vin = S.Vin AND V.manufacturerID = M.manufacturerID AND S.CustomerID=%s ORDER BY soldDate DESC, VIN ASC'
            cur.execute(sql, (CID,))
        result = cur.fetchall()
        return result

    # gross customer drilldown 2
    def gross_drill2(CID):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            sql = 'SELECT R.StartDate, R.CompleteDate, R.Vin, Odometer, PartCost, LaborCharge, (PartCost+LaborCharge) Total, CONCAT(U.FirstName, " ", U.LastName) name FROM Repair R, User U, (SELECT P.Vin, P.CustomerID, P.StartDate, SUM(Price*Quantity) AS PartCost FROM Part P GROUP BY P.Vin, P.CustomerID, P.StartDate) AS PC WHERE PC.Vin=R.Vin AND  PC.CustomerID=R.CustomerID AND PC.StartDate=R.StartDate AND U.Username = R.Username AND R.CustomerID=%s ORDER BY StartDate DESC, CompleteDate DESC, R.Vin ASC'
            cur.execute(sql, (CID,))
        result = cur.fetchall()
        return result

    # generate report for repairs
    def repair_by():
        conn = con.getConnection()
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        if conn[0]:
            cur = conn[1].cursor()
            filename = absolute_path + '/sql/repairs_by.sql'
        with open(filename) as f:
            cur.execute(f.read())
        result = cur.fetchall()
        return result    

    # repair drill down 1
    def repair_drill_1(manufacturer):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            sql = 'SELECT vehicletype, Count(*), SUM(Price * Quantity), SUM(LaborCharge), SUM(Price*Quantity + LaborCharge) FROM Vehicle AS V INNER JOIN Repair AS R ON V.Vin=R.Vin INNER JOIN Part AS P ON R.Vin=P.Vin AND R.CustomerID=P.CustomerID AND R.StartDate=P.StartDate INNER JOIN Manufacturer AS M ON V.ManufacturerID = M.ManufacturerID INNER JOIN VehicleType AS VT ON V.vehicletypenumber = VT.vehicletypenumber WHERE ManufacturerName =%s GROUP BY vehicletype ORDER BY Count(*) DESC'
            cur.execute(sql, (manufacturer,))
        result = cur.fetchall()
        return result

    # repair drill down 2
    def repair_drill_2(manufacturer, vehicletype):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            sql = 'SELECT Model, Count(*), SUM(Price * Quantity), SUM(LaborCharge), SUM(Price*Quantity + LaborCharge) FROM Vehicle AS V INNER JOIN Repair AS R ON V.Vin=R.Vin INNER JOIN Part AS P ON R.Vin=P.Vin AND R.CustomerID=P.CustomerID AND R.StartDate=P.StartDate INNER JOIN Manufacturer AS M ON V.ManufacturerID = M.ManufacturerID INNER JOIN VehicleType AS VT ON V.vehicletypenumber = VT.vehicletypenumber WHERE ManufacturerName = %s AND VehicleType = %s GROUP BY V.vehicletypenumber, Model ORDER BY Count(*) DESC'
            cur.execute(sql, (manufacturer, vehicletype))
        result = cur.fetchall()
        return result


    # generate monthly report
    def monthly_report():
        conn = con.getConnection()
        absolute_path = os.path.dirname(os.path.abspath(__file__))
        if conn[0]:
            cur = conn[1].cursor()
            filename = absolute_path + '/sql/monthly_report.sql'
        with open(filename) as f:
            cur.execute(f.read())
        result = cur.fetchall()
        return result

    # monthly report drill down
    def monthly_report_drilldown(year, month):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            sql = 'SELECT U.FirstName, U.LastName, Count(SoldDate) AS numSold, SUM(SoldPrice) AS TotalSales FROM SellVehicle AS S, User AS U WHERE U.Username=S.Username AND YEAR(SoldDate)=%s AND MONTH(SoldDate)=%s GROUP BY S.Username ORDER BY numSold DESC, TotalSales DESC'
            cur.execute(sql, (year, month))
        result = cur.fetchall()
        return result


class SearchVehicle:
    @staticmethod
    def viewOneSell(vin):
        conn = con.getConnection()
        sql = "SELECT * FROM SellVehicle WHERE "
        sql += "vin = '" + vin + "' "
        sql += "ORDER BY vin;"
        #print(sql)
        result = ""
        cur = conn[1].cursor(buffered=True)
        cur.execute(sql)
        result = cur.fetchall()
        return result
    
    def searchIndividual(Cid):
        conn = con.getConnection()
        sql = "SELECT CONCAT(firstName, '  ',lastName) AS name, phonenumber, email FROM Individual NATURAL JOIN Customer WHERE "
        sql += "customerID = '" + str(Cid) + "' "
        sql += "ORDER BY customerID;"
        #print(sql)
        result = ""
        cur = conn[1].cursor(buffered=True)
        cur.execute(sql)
        result = cur.fetchall()
        return result

    def searchBusiness(Cid):
        conn = con.getConnection()
        sql = "SELECT businessname as name, phonenumber, email FROM Business NATURAL JOIN Customer WHERE "
        sql += "customerID = '" + str(Cid) + "' "
        sql += "ORDER BY customerID;"
        #print(sql)
        result = ""
        cur = conn[1].cursor(buffered=True)
        cur.execute(sql)
        result = cur.fetchall()
        return result
    
    def getUserName(username):
        conn = con.getConnection()
        sql = "SELECT CONCAT(firstName, '  ',lastName) AS name FROM User WHERE username = '%s'"
        cur = conn[1].cursor(buffered=True)
        cur.execute(sql % username)
        result = cur.fetchall()
        return result[0][0]

    def searchUserName(vin):
        conn = con.getConnection()
        sql = "SELECT username FROM Vehicle WHERE vin = '%s'"
        cur = conn[1].cursor(buffered=True)
        cur.execute(sql % vin)
        result = cur.fetchall()
        return result[0][0]

    def viewOneAvaliable(vin):
        conn = con.getConnection()
        sql = "SELECT DISTINCT vf.vin, vf.model, vf.modelyear, vf.Invoiceprice, vf.Listprice, vf.description, vf.username, vf.adddate,vf.vehiclecolor, vt.vehicletype, vt.vehicledetail, m.manufacturername FROM vehicletype AS vt, Manufacturer AS m, SellVehicle AS sv, (SELECT v.vin, v.model, v.modelyear, v.invoiceprice, v.Listprice, v.username, v.adddate, v.description, v.vehicletypenumber, v.manufacturerID, CONCAT(GROUP_CONCAT(vcc.color SEPARATOR ',')) 'vehiclecolor' FROM Vehicle AS v left join (SELECT vc.vin, c.color FROM Vehiclecolor AS vc, color AS c WHERE vc.colorID = c.colorID) AS vcc ON v.vin = vcc.vin GROUP BY v.vin) AS vf WHERE vf.vehicletypenumber = vt.vehicletypenumber and vf.manufacturerID = m.manufacturerID "
        sql += "AND vf.vin = '" + vin + "' "
        sql += "ORDER BY vf.vin;"
        #print(sql)
        result = ""
        cur = conn[1].cursor(buffered=True)
        cur.execute(sql)
        result = cur.fetchall()
        return result


    def viewAvaliable():
        conn = con.getConnection()
        sql = "SELECT DISTINCT vf.vin, vf.model, vf.modelyear, vf.Invoiceprice, vf.Listprice, vf.description, vf.username, vf.adddate,vf.vehiclecolor, vt.vehicletype, vt.vehicledetail, m.manufacturername FROM vehicletype AS vt, Manufacturer AS m, SellVehicle AS sv, (SELECT v.vin, v.model, v.modelyear, v.invoiceprice, v.Listprice, v.username, v.adddate, v.description, v.vehicletypenumber, v.manufacturerID, CONCAT(GROUP_CONCAT(vcc.color SEPARATOR ',')) 'vehiclecolor' FROM Vehicle AS v left join (SELECT vc.vin, c.color FROM Vehiclecolor AS vc, color AS c WHERE vc.colorID = c.colorID) AS vcc ON v.vin = vcc.vin GROUP BY v.vin) AS vf WHERE vf.vehicletypenumber = vt.vehicletypenumber and vf.manufacturerID = m.manufacturerID ORDER BY vf.vin;"
        #print(sql)
        result = ""
        cur = conn[1].cursor(buffered=True)
        cur.execute(sql)
        result = cur.fetchall()
        return result

    def avaliable_car_num():
        conn = con.getConnection()
        sql = "SELECT DISTINCT vf.vin, vf.model, vf.modelyear, vf.Listprice, vf.description, vf.vehiclecolor, vt.vehicletype, vt. vehicledetail, m.manufacturername FROM vehicletype AS vt, Manufacturer AS m, SellVehicle AS sv, (SELECT v.vin, v.model, v.modelyear, v.invoiceprice, v.Listprice, v.description, v.vehicletypenumber, v.manufacturerID, CONCAT(GROUP_CONCAT(vcc.color SEPARATOR ',')) 'vehiclecolor' FROM Vehicle AS v left join (SELECT vc.vin, c.color FROM Vehiclecolor AS vc, color AS c WHERE vc.colorID = c.colorID) AS vcc ON v.vin = vcc.vin GROUP BY v.vin) AS vf WHERE vf.vin NOT IN  (SELECT sv.vin FROM SellVehicle AS sv) AND vf.vehicletypenumber = vt.vehicletypenumber and vf.manufacturerID = m.manufacturerID "
        sql += "ORDER BY vf.vin ;"
        #print(sql)
        result = ""
        cur = conn[1].cursor(buffered=True)
        cur.execute(sql)
        result = cur.fetchall()
        return len(result)

    def search(c, vin, type, manufacturer, year, color, list_price_greater,list_price_less, keywords):
        conn = con.getConnection()
        allNull = True
        sql = ""
        if(c == "unsold vehicles"):  
            sql = "SELECT DISTINCT vf.vin, vf.model, vf.modelyear, vf.Listprice, vf. Invoiceprice, vf.description, vf.vehiclecolor, vt.vehicletype, vt. vehicledetail, m.manufacturername, vf.adddate FROM vehicletype AS vt, Manufacturer AS m, SellVehicle AS sv, (SELECT v.vin, v.model, v.adddate, v.modelyear, v.invoiceprice, v.Listprice, v.description, v.vehicletypenumber, v.manufacturerID, CONCAT(GROUP_CONCAT(vcc.color SEPARATOR ',')) 'vehiclecolor' FROM Vehicle AS v left join (SELECT vc.vin, c.color FROM Vehiclecolor AS vc, color AS c WHERE vc.colorID = c.colorID) AS vcc ON v.vin = vcc.vin GROUP BY v.vin) AS vf WHERE vf.vin NOT IN  (SELECT sv.vin FROM SellVehicle AS sv) AND vf.vehicletypenumber = vt.vehicletypenumber and vf.manufacturerID = m.manufacturerID "
        elif(c == "sold vehicles"):
            sql = "SELECT DISTINCT vf.vin, vf.model, vf.modelyear, vf.Listprice, vf. Invoiceprice, vf.description, vf.vehiclecolor, vt.vehicletype, vt. vehicledetail, m.manufacturername,vf.adddate FROM vehicletype AS vt, Manufacturer AS m, SellVehicle AS sv, (SELECT v.vin, v.model, v.adddate, v.modelyear, v.invoiceprice, v.Listprice, v.description, v.vehicletypenumber, v.manufacturerID, CONCAT(GROUP_CONCAT(vcc.color SEPARATOR ',')) 'vehiclecolor' FROM Vehicle AS v left join (SELECT vc.vin, c.color FROM Vehiclecolor AS vc, color AS c WHERE vc.colorID = c.colorID) AS vcc ON v.vin = vcc.vin GROUP BY v.vin) AS vf WHERE vf.vin IN  (SELECT sv.vin FROM SellVehicle AS sv) AND vf.vehicletypenumber = vt.vehicletypenumber and vf.manufacturerID = m.manufacturerID "
        elif(c == "all vehicles"):
            sql = "SELECT DISTINCT vf.vin, vf.model, vf.modelyear, vf.Listprice, vf. Invoiceprice, vf.description, vf.vehiclecolor, vt.vehicletype, vt. vehicledetail, m.manufacturername,vf.adddate FROM vehicletype AS vt, Manufacturer AS m, SellVehicle AS sv, (SELECT v.vin, v.model, v.adddate, v.modelyear, v.invoiceprice, v.Listprice, v.description, v.vehicletypenumber, v.manufacturerID, CONCAT(GROUP_CONCAT(vcc.color SEPARATOR ',')) 'vehiclecolor' FROM Vehicle AS v left join (SELECT vc.vin, c.color FROM Vehiclecolor AS vc, color AS c WHERE vc.colorID = c.colorID) AS vcc ON v.vin = vcc.vin GROUP BY v.vin) AS vf WHERE vf.vehicletypenumber = vt.vehicletypenumber and vf.manufacturerID = m.manufacturerID " 
       
        if (len(vin) > 0):
            allNull = False
            sql += "AND vf.vin = '" + vin + "' "
        if(len(type) > 0):
            allNull = False
            sql += "AND vt.vehicletype = '" + type +"' "
        if(len(manufacturer) > 0):
            allNull = False
            sql += "AND m.manufacturername  = '" + manufacturer +"' "
        if(len(year) > 0):
            allNull = False
            sql += "AND vf.modelyear = '" + year +"' "
        if(len(color) > 0):
            allNull = False
            sql += "AND vf.vehiclecolor LIKE '%" + color +"%' "
        if(len(list_price_greater) > 0):
            allNull = False
            sql += "AND vf.Listprice >= " + list_price_greater +" "
        if(len(list_price_less) > 0):
            allNull = False
            sql += "AND vf.Listprice <= " + list_price_less +" "
        if(len(keywords) > 0):
            allNull = False
            sql += "AND (m.manufacturername LIKE '%" +keywords +"%' OR vf.modelyear LIKE '%" +keywords +"%' OR vf.model LIKE '%" +keywords +"%' OR vf.description LIKE '%" +keywords +"%')"
        sql += "ORDER BY vf.vin ;"
        #print(sql)
        result = ""
        if(not allNull):
            cur = conn[1].cursor(buffered=True)
            cur.execute(sql)
            result = cur.fetchall()
        return result


class AddVehicle:
    @staticmethod
    def retrieveColor():
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            cur.execute("SELECT color FROM color")
            rows = cur.fetchall()
            colors = []
            for i in range(len(rows)):
                colors.append(rows[i][0])
            return colors

    @staticmethod
    def retrieveManufacturer():
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            cur.execute("SELECT manufacturername FROM manufacturer")
            rows = cur.fetchall()
            manufacturers = []
            for i in range(len(rows)):
                manufacturers.append(rows[i][0])
            return manufacturers

    def checkVin(vin):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            cur.execute("SELECT vin FROM Vehicle WHERE vin = '%s'" % vin)
            row = cur.fetchall()
            if cur.rowcount == 1:
                return True
            else:
                return False

    def addVehicleType(vehicletype, vehicledetail):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            add_vehicletype = (vehicletype, vehicledetail)
            sql = "INSERT INTO Vehicletype (vehicletype, vehicledetail) VALUES (%s, %s)"
            cur.execute(sql, add_vehicletype)
            conn[1].commit()

    def addVehicle(vin, model, modelYear, invoicePrice, description, username, manufacturerID, adddate):
        conn = con.getConnection()
        # today = date.today()
        listPrice = float(invoicePrice)*1.25
        if conn[0]:
            cur = conn[1].cursor()
            cur.execute("SELECT MAX(VehicleTypeNumber) FROM Vehicletype")
            row = cur.fetchall()
            VehicleTypeNumber = row[0][0]
            # self.vin.get(), self.model.get(), self.model_year.get(), self.list_price.get(),
            #                                      self.description.get(), lg.LoginPage.userID, manufacturerID
            add_vehicle = (vin, model, modelYear, listPrice, invoicePrice, description, username, adddate,
                               VehicleTypeNumber, manufacturerID)
            sql2 = ("INSERT INTO Vehicle (VIN, Model, ModelYear, listPrice, InvoicePrice, Description, username, "
                    "addDate, VehicleTypeNumber, ManufacturerID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
            cur.execute(sql2, add_vehicle)
            conn[1].commit()

    def addVehicleColorList(vin, colorList):
        conn = con.getConnection()
        print(colorList)
        if conn[0]:
            cur = conn[1].cursor()
            for x in colorList:
                sql1 = "SELECT colorID FROM color WHERE color = '%s'"
                cur.execute(sql1 % x)
                row = cur.fetchall()
                AddVehicle.addVehicleColor(vin, row[0][0])

    def addVehicleColor(vin, colorID):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            add_vehiclecolor = (vin, colorID)
            sql = "INSERT INTO Vehiclecolor (vin, colorID) VALUES (%s, %s)"
            cur.execute(sql, add_vehiclecolor)
            conn[1].commit()

    def getManufacturerID(manufacturer):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            cur.execute("SELECT manufacturerID FROM manufacturer where manufacturername = '%s'" % manufacturer)
            row = cur.fetchall()
            return row[0][0]
    
class AddSalesTransaction(object):
    def getCustomerID(phone_number, address, email):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            sql = "SELECT customerID FROM Customer where phonenumber = '" + phone_number +"'"\
                " AND address = '" + address + "'"\
                " AND email = '" + email + "';"
            print("sql :"+sql)
            cur.execute(sql)
            result = cur.fetchall()
            return result[0][0]

    def addSalesTransaction(vin, customerID, username, sold_price, sold_date):
        conn = con.getConnection()
        if (conn[0]):
            cur = conn[1].cursor()
            add_sales_transaction = (vin, customerID, username, sold_price, sold_date)
            sql = "INSERT INTO SellVehicle (vin, customerID, username, soldprice, solddate) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(sql, add_sales_transaction)
            conn[1].commit()

class SearchRepair:
    def checkVin(vin):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            cur.execute("SELECT vin FROM sellvehicle WHERE vin = '%s'" % vin)
            row = cur.fetchall()
            if cur.rowcount == 1:
                return False
            else:
                return True

    def getVheicle(vin):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            sql = ("SELECT vf.vin, vf.model, vf.modelyear, vf.vehiclecolor, vf.invoiceprice, vf.Listprice, vf.description, "
                   "vt.vehicletype, vt. vehicledetail, m.manufacturername FROM vehicletype AS vt, Manufacturer AS m, "
                   "(SELECT v.vin, v.model, v.modelyear, v.invoiceprice, v.Listprice, v.description, "
                   "v.vehicletypenumber, v.manufacturerID, CONCAT(GROUP_CONCAT(vcc.color SEPARATOR ',')) 'vehiclecolor' "
                   "FROM Vehicle AS v left join (SELECT vc.vin, c.color FROM Vehiclecolor AS vc, color AS c "
                   "WHERE vc.colorID = c.colorID) AS vcc ON v.vin = vcc.vin GROUP BY v.vin) AS vf "
                   "WHERE vf.vehicletypenumber = vt.vehicletypenumber and vf.manufacturerID = m.manufacturerID "
                   "AND vin = '%s'")
            cur.execute(sql % vin)
            row = cur.fetchall()
            vehicle = ev.Vehicle(row[0][0], row[0][1], row[0][2], row[0][3], row[0][4], row[0][5], row[0][6], row[0][7], row[0][8], row[0][9])
        return vehicle

    def getRepairList(vin):
        closeList = []
        openList = []
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            cur.execute("SELECT * FROM Repair WHERE vin = '%s'" % vin)
            rows = cur.fetchall()
            for i in range(cur.rowcount):
                # vin, customerID, startdate, odermeter, laborcharge, description, completedate
                partList = SearchRepair.getPartList(rows[i][0], rows[i][1], str(rows[i][2]))
                repair = er.Repair(rows[i][0], rows[i][1], str(rows[i][2]), rows[i][3], rows[i][4], rows[i][5],
                                   rows[i][6], str(rows[i][7]), partList)
                if repair.completedate == "None":
                    openList.append(repair)
                else:
                    closeList.append(repair)
        return closeList, openList

    def getPartList(vin, customerID, startdate):
        partList = []
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            cur.execute("SELECT * FROM Part WHERE vin = %s AND customerID = %s AND startdate = %s",
                        (vin, customerID, startdate))
            rows = cur.fetchall()
            for i in range(cur.rowcount):
                part = er.Part(rows[i][0], rows[i][1], str(rows[i][2]), rows[i][3], rows[i][4],rows[i][5], rows[i][6])
                partList.append(part)
        return partList

    def updateLaborCharge(vin, customerID, startdate, laborCharge):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            update_laborcharge = (laborCharge, vin, customerID, startdate)
            sql = "UPDATE Repair SET laborcharge = %f WHERE vin = '%s' AND customerID = %s AND startdate = '%s'"
            cur.execute(sql % update_laborcharge)
            conn[1].commit()

    def addNewParts(vin, customerID, startdate, partList):
        conn = con.getConnection()
        if conn[0]:
            cur = conn[1].cursor()
            for i in range(len(partList)):
                add_newparts = (vin, customerID, startdate, partList[i][0], partList[i][1], partList[i][2], partList[i][3])
                sql = "INSERT INTO Part (vin, customerID, startdate, partnumber, quantity, price, vendorname) VALUES ('%s', %s, '%s', %s, %s, %s, '%s')"
                cur.execute(sql % add_newparts)
                conn[1].commit()

    def completeRepair(vin, customerID, startdate):
        conn = con.getConnection()
        today = date.today()
        if conn[0]:
            cur = conn[1].cursor()
            complete_repair = (today, vin, customerID, startdate)
            sql = "UPDATE Repair SET completedate = '%s' WHERE vin = '%s' AND customerID = %s AND startdate = '%s'"
            cur.execute(sql % complete_repair)
            conn[1].commit()
