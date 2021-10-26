
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b



num1=int(input("첫번째 수를 입력하세요 : "))
op=str(input("연산자를 입력하세요 :"))
num2=int(input("두번째 수를 입력하세요 : "))
if (op == "+"):
    result=add(num1,num2)
elif (op=="-"):
    result=sub(num1,num2)
elif (op=='*'):
    result=mul(num1,num2)
elif (op=="/"):
    result=div(num1,num2)

print("계산 결과 : {} {} {} = {} ".format(num1,op,num2,result))

op=str(input("연산자를 입력하세요 :"))
num3=int(input("세번째 수를 입력하세요 : "))

if (op == "+"):
    result2=add(num3,result)
elif (op=="-"):
    result2=sub(num3,result)
elif (op=='*'):
    result2=mul(num3,result)
elif (op=="/"):
    result2=div(num3,result)

print("계산 결과 : {} {} {} = {} ".format(num3,op,result,result2))
