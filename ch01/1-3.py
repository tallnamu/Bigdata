num = []
num.append(int(input("숫자 입력 : ")))
num.append(int(input("숫자 입력 : ")))
num.append(int(input("숫자 입력 : ")))
num.append(int(input("숫자 입력 : ")))
sum=0
for i in range (len(num)):
    sum+=num[i]


print(sum/len(num))
