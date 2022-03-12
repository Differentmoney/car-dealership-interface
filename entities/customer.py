class Customer(object):
    def __init__(self, phone_number, address, email):
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.isBusiness = False
        self.isIndividual = False

class Business(Customer):
    def __init__(self,
                phone_number,
                address,
                email,
                taxID,
                business_name,
                primary_contact_name,
                primary_contact_title):
        super().__init__(phone_number, address, email)
        self.taxID = taxID
        self.business_name = business_name
        self.primary_contact_name = primary_contact_name
        self.primary_contact_title = primary_contact_title
        self.isBusiness = True
        self.isIndividual  = False

class Individual(Customer):
    def __init__(self,
                phone_number,
                address,
                email,
                driver_license,
                first_name,
                last_name):
        super().__init__(phone_number, address, email)
        self.driver_license = driver_license
        self.first_name = first_name
        self.last_name = last_name
        self.isBusiness = False
        self.isIndividual = True

