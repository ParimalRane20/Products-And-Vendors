

class vendor:
    def __init__(self,vid,vnm,vadr):
        self.venid=vid
        self.vname=vnm
        self.vaddress=vadr

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'''\n {self.__dict__}\n'''