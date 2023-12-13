# class Car:
#     color = 'oq'
    # model = 'GM'


# matiz = Car()
# class Cat:
#     name = 'Mosh'
#     age = 3
#     def set_car(self, x ,y):
#         self.x = x
#         self.y = y
#         print('SIz mushukka murojaat qildingiz')
#     def get_cat(self):
#         return (self.x, self.y)
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y


class Son():
    Min = 0
    Max = 100
    @classmethod
    def validation(cls, z):
        return cls.Min<=z<=cls.Max
    __instance = None
    def __new__(cls, *args, **kwargs):
        print('Behruz' + str(cls))
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
        # if 'x' in kwargs and kwargs['x']== 5:
        #     return None
        instance = super().__new__(cls)
        return instance
    def __init__(self, x=10 ,y=20):
        self.x = x
        self.y = y
    def set_son(self, x, y):
        self.x = x
        self.y = y
    def get(self):
        return (self.x, self.y)
    def __del__(self):
        Son.__instance = None


