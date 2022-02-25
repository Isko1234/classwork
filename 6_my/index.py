# def Name_my(name):
#     return 'Hello '+name
# имя = input('Введите имя: ')
# print(Name_my(имя))
# def summa_for_num(num1,num2):
#     print(num1+num2)
# number = int(input("Введите число: "))
# number2 = int(input("Введите число : "))
# summa_for_num(number,number2)

def absolute_value(num1,num2):
    # if num1<0:
    #     print(num1*(-1))
    # else:
    #     print(num1)
    a = 1
    while(a<=num2):
        num1 = num1*num1
        a+=1
    print(num1)
    
num = int(input('Введите число : '))
num2 = int(input('Введите число : '))
absolute_value(num,num2)