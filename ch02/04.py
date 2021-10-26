num=[]
i=1
while i<=4:
    a=int(input("숫자를 입력하세요: "))
    num.append(a)
    i+=i
if a<60:
    print("과락입니다.")
else:
    print("평균:",sum(num)/len(num))
