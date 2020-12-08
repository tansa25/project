class Company:
    def __init__(self, price=None, valueChange=None, percentageChange=None, history=None):
        self.price = price
        self.valueChange = valueChange
        self.percentageChange = percentageChange
        self.history = history

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def valueChange(self):
        return self._valueChange

    @valueChange.setter
    def valueChange(self, value):
        self._valueChange = value

    @property
    def percentageChange(self):
        return self._percentageChange

    @percentageChange.setter
    def percentageChange(self, value):
        self._percentageChange = value

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        self._history = value
