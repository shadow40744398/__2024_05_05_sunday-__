import pyinputplus as pyip
from health import BMI

def main():
    try:
        name =  pyip.inputStr("請輸入你的名字:")
        height = pyip.inputFloat("請輸入你的身高(cm):",min=0,max=250)
        weight = pyip.inputFloat("請輸入你的體重(kg):",min=0,max=200)

        bmi = BMI(height, weight)
        status = BMI(object)

        print(f"{object.name}, 您的BMI值為 {object.bmi()}")
        print(f"您的體重為 {object.status()}")

    except Exception as e:
                print(f"EXCEPTION - {type(e)}")

if __name__ == "__main__":
    main()