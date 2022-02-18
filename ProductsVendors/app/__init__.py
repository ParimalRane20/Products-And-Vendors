class phone:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.modelname=model_name
        self.price=price

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n {self.__dict__}\n'''


class smartphone(phone):

    def __init__(self,sbrand,smodel_name,sprice,camera):
        phone().__init__(brand,model_name,price)
        self.camera=camera


    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n {self.__dict__}\n'''
