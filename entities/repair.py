class Part(object):
    def __init__(self,
                 vin,
                 customerID,
                 startdate,
                 partnumber,
                 quantity,
                 price,
                 vendorname):
        self.vin = vin
        self.customerID = customerID
        self.startdate = startdate
        self.partnumber = partnumber
        self.quantity = quantity
        self.price = price
        self.vendorname = vendorname

class Repair(object):
    def __init__(self, 
                 vin, 
                 customerID, 
                 startdate,
                 username, 
                 odometer, 
                 laborcharge,
                 description,
                 completedate,
                 parts=None):
        if parts is None:
            parts = []
        self.vin = vin
        self.customerID = customerID
        self.startdate = startdate
        self.username = username
        self.odometer = odometer
        self.laborcharge = laborcharge
        self.description = description
        self.completedate = completedate
        self.parts = parts