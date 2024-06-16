class BMI():
    def __init__(self, n=str, h= float, w= float):
        self.__name = n
        self.__height = h / 100
        self.__weight = w

    @property
    def name(self)->str:
        return self.__name
    
    @property
    def height(self)->float:
        return self.__height
    
    @property
    def weight(self)->float:
        return self.__weight
    
    
    def bmi(self)->float:
        return round(self.weight / self.height ** 2, 2)
    
    def status(self)->str:
        if self.bmi() < 18.5:
            rate = "過輕"
        elif self.bmi() < 24:
            rate = "正常"
        elif self.bmi() < 27:
            rate = "過重"
        elif self.bmi() < 30:
            rate = "輕度肥胖"
        elif self.bmi() < 35:
            rate = "中度肥胖"
        else:
            rate = "重度肥胖"
        
        return rate