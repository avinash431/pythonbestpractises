class Sample:

    def __init__(self, var, y, z):
        self.name = var
        self.city = y
        self.ID = z

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, var):
        if var == "":
            raise ValueError("Name can't be empty")
        self.__name = var

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, y):
        if y == "":
            raise ValueError("City can't be empty")
        self.__city = y

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, z):
        if z < 0:
            raise ValueError("ID can't be -ve")
        self.__ID = z


s = Sample("aa", "bb", 10)
