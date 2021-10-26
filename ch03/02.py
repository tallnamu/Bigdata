import cals

print("종료하려면 0입력")
while(True):

    num1=int(input("첫번째 수 입력 :"))
    if num1==0:
        print("종료")
        break
    op=str(input("연산자 입력 : "))
    num2=int(input("두번째 수 입력 : "))
    if (op == "+"):
        cals.add(num1,num2)
    elif (op=="-"):
        cals.sub(num1,num2)
    elif (op=='*'):
        cals.mul(num1,num2)
    elif (op=="/"):
        cals.div(num1,num2)
 
