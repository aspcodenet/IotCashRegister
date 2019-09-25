from datetime import datetime

class Product:
    def __init__(self, productId, price, name):
        self._productId = productId
        self._price = price
        self._name = name


class Receipt:
    def __init__(self, cashNo):
        self._cashNo = cashNo
        self._rows = []
        self.date = datetime.now()

    def Total(self):
        sum = 0
        for row in self._rows:
            sum += row._perPrice * row._count
        return sum

    def AddRow(self, productId, perPrice, count, productName):
        for row in self._rows:
            if row.GetProductId() == productId:
                row.AddCount(count)
                return
        self._rows.append( ReceiptRow(productId, perPrice, count, productName) )

class ReceiptRow:
    def __init__(self, productId, perPrice, count, productName):
        self._productId = productId
        self._perPrice = perPrice
        self._count = count
        self._productName = productName

    def GetProductId(self):
        return self._productId

    def AddCount(self, count):
        self._count += count



r = Receipt("1")
r.AddRow("123",12,2,"banan")
r.AddRow("123",12,1,"banan")
print(r.Total())

