num=[]
for i in range(3):
    a=int(input("숫자를 입력하세요 :"))
    num.append(a)
if a<60:
    print("과락입니다.")
else:
    print("평균:",sum(num)/len(num))
