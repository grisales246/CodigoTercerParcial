from datetime import date

from numpy import double, void


class User:

    UserId : int
    Password : str
    RegisterDate : date
    
    def Login(self):
        void


class Administrator(User):

    User : User
    Name : str
    Email : str

    def UpdateProductos(self):
        void


class Customer(User):
    Name : str
    Address : str
    CustomerId: int
    AccountBalance: double
    def Register(self):
        void
    def Purchase(self):
        void
class Order:
    OrderId : int
    Date : date
    CustomerName : str
    CustomerId : int
    #Metodos
    def UpdateProductos(self):
        void

class OrderDetails:

    OrderId : int
    ProductId : int
    ProductName : str
    Quantity : int
    UnitCost : double
    Total : double
    def __init__(self, order: Order):
        self.Order = order
    
    def CalculateTotal(self):
        int




