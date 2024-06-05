class BMI():
    def __init__(self,n, h, w): #自訂的init
        self.__name = n
        self.__height = h
        self.__weight = w

    @property
    def name(self):
        return self.__name
    
    @property
    def height(self) -> float:
        return self.__height
    
    @property
    def weight(self) -> float:
        return self.__weight
    
    def bmi(self)->float:
        return round(self.weight /self.height ** 2,2)
    
    def  status(self) -> str:
        if self.bmi() < 18.5:
            status = "過輕"
        elif self.bmi() < 24:
            status = "正常"
        elif self.bmi() < 27:
            status = "過重"
        elif self.bmi() < 30:
            status = "輕度肥胖"
        elif self.bmi() < 35:
            status = "中度肥胖"
        else:
            status = "重度肥胖"
        return status
    
