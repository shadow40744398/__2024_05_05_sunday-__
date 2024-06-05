#內建的變數__name__
#print(__name__)
#print(type(__name__))
import pyinputplus as pyip
from health import BMI

def main():

    try:
        name =  pyip.inputStr("請輸入你的名字:")
        height = pyip.inputFloat("請輸入你的身高(cm):",min=0,max=250)
        weight = pyip.inputFloat("請輸入你的體重(kg):",min=0,max=200)

        data = BMI(name, height, weight)
                
        print(f"{data.name}, 您的BMI值為 {data.bmi()}")
        print(f"您的體重為 {data.status()}")

    except Exception as e:
        print(f"EXCEPTION - {type(e)}")

if __name__ == '__main__':
    main()