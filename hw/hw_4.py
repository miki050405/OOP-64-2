print('Домашнее задание №4')
rates =  {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def convert_to_kgs(self):
        if self.currency != "KGS":
            self.amount = self.amount * rates[self.currency]
            self.currency = "KGS"
        else:
            pass

    def __add__(self, other):
        if self.currency != other.currency:
            if self.currency != "KGS":
                self.convert_to_kgs()
            if other.currency != "KGS":
                other.convert_to_kgs()
        return Money(self.amount + other.amount, self.currency)
        

    def __sub__(self, other):
        if self.currency != other.currency:
            if self.currency != "KGS":
                self.convert_to_kgs()
            if other.currency != "KGS":
                other.convert_to_kgs()
        return Money(self.amount - other.amount, self.currency)
    
    def __mul__(self, other):
        return Money(self.amount * other, self.currency)
    
    def __truediv__(self, other):
        return Money(self.amount / other, self.currency)
    
    def __str__(self):
        return f"{self.amount} {self.currency}"

money1 = Money(100, "USD")
print(money1)
money2 = Money(5000, "EUR") 
print(money2)
result = money1 + money2
print(result)
print(money1 - money2)
print(money1 * 3)
print(money1 / 2)
