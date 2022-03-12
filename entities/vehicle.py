class Vehicle(object):
    def __init__(self, 
                vin = None,
                model = None,
                model_year = None,
                color = None,
                invoice_price = None,
                list_price=None,
                description = None,
                type = None,
                detail = None,
                manufacturerName = None,
                adddate = None):
        self.vin = vin or " "
        self.model = model or " "
        self.model_year = model_year or " "
        self.color = color or " "
        self.invoice_price = invoice_price or " "
        self.list_price = list_price or " "
        self.description = description or " "
        self.type = type or " "
        self.detail = detail or " "
        self.manufacturerName = manufacturerName or " "
        self.adddate = adddate or " "
