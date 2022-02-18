

class Product:
    def __init__(self,pid,pnm,pric,pqty,pven,pcat):
        self.prodid=pid
        self.prodname=pnm
        self.prodprice=pric
        self.prodqty=pqty
        self.vendor=pven
        self.prodcat=pcat

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n {self.__dict__}\n'''