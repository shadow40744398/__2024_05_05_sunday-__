import pyinputplus as pyip

def cal_bmi(height:int,weight:int) -> float:
    return(round(weight / ((height/100)**2),ndigits=2))
def get_status(bmi:float)->str:
        if bmi < 18.5:
            status = "過輕"
        elif bmi < 24:
            status = "正常"
        elif bmi < 27:
            status = "過重"
        elif bmi < 30:
            status = "輕度肥胖"
        elif bmi < 35:
            status = "中度肥胖"
        else:
            status = "重度肥胖"
        return status
try:
        name =  pyip.inputStr("請輸入你的名字:")
        height = pyip.inputFloat("請輸入你的身高(cm):",min=0,max=250)
        weight = pyip.inputFloat("請輸入你的體重(kg):",min=0,max=200)

        bmi = cal_bmi(height, weight)
        status = get_status(bmi)

        print(f"\n{name} - ,\n身高: {height}cm,\n體重: {weight}Kg")
        print(f"BMI: {round(bmi, 2)}  你屬於{status}範圍")
except Exception as e:
	    print(f"EXCEPTION - {type(e)}")