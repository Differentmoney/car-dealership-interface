class Repairform(object):
    def __init__(self, 
                vin = '0000', 
                customerID = 'Honda', 
                start_date = '2021', 
                username = '40000',
                odometer = '50000',
                labor_charge = 'no description',
                description = 'mike',
                complete_date = '11/04/2021'):
        self.vin = vin
        self.customerID = customerID
        self.start_date = start_date
        self.username = username
        self.odometer = odometer
        self.labor_charge = labor_charge
        self.description = description
        self.complete_date = complete_date