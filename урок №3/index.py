# a = 23
# b = a%10
# s = a//10
# print(b+s)
# f = 123
# g = f%10
# h = (f//10)%10
# j = f//100
# k = g+h+j
# print(k)

# l= 8765
# z = l%10
# x = (l//10)%10
# c = l//100%10
# v = (l //1000)
# b = x+c+v+z
# print(b)
# n = "GHbdtn"
# print(n)
# gu = " 23*4 "*55
# name = 'Iskandar'
# lastname = 'Kasymov'
# age =  14
# gjl = 'male'
# print('Hello my name is '+ name+' '+' ' + lastname + '! I am  ' +   str (age) + " " + gjl)
# v1= 70
# v2 = 100
# t = 2
# s = v1*t + v2*t
# print(str(s)+' km')
a = int(input("часы:"))
b = int(input("минуты"))
c = int(input("разница"))

if(a+c>=24):
            d = (a+c)%24
else :
            d = a+c
if(a+c<0):
    d = 24 + (a+c)
if(d<0 and b<10):
    print('0'+str(d)+':'+'0'+str(b))
if(d<0 and b>10):
        print('0'+str(d)+':'+str(b))
if(d>10 and b<10):
    print(str(d)+':'+'0'+str(b))
if(d>24 and b <10):
    if(d>10):
       print(str(d%24)+':'+'0'+str(b))
if(d<10):
           print('0'+str(d%24)+':'+'0'+str(b))
elif(d>10 and b>10):
    print(str(d)+':'+str(b))


    


