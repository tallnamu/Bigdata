
# num=input("네자리 이하로 정수를 입력하시오. ")
# sum=0   

# for i in num:
#     sum+=int((i))

# print(sum)


num = int(input("네자리 이하로 정수를 입력하시오."))
sum= num // 1000 + (num % 1000 - num % 100) // 100 + (num % 100 - num % 10) // 10 + num % 10
print("자리수의 합=", sum)
