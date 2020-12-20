class Company:
    def __init__(self, **data):
        self.symbol = data.get('symbol', 'SYMBOL')
        self.graphicURL = data.get('graphicURL', 'www.example.com')
        self.headerURL = data.get('headerURL', 'www.example.com')
        self.companyProfileURL = data.get('companyProfileURL', 'www.example.com')
