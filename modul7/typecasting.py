# # # # age = 25
# # # # print(type(age))
# # # # age_as_str=str(age)
# # # # print (age_as_str,"type is ",type(age_as_str))
# # # x=5
# # # y=4.5
# # # result=x+y
# # # print(type(result))
# # # age=25
# # # message="i am "+ str(age) + " years old"
# # # print(message)
# # #
# # # a=5
# # # b="3"
# # # print(type(b))
# # # b1=int(b)
# # # result2=a+int(b)
# # # print(type(b))
# # # print(result2)
# # name=input("enter your name:")
# # print(f"Hello,{name}")
# #
# # age=input("enter you age:")
# # print(type(age))
# #
# # num1=int(input("enter 1st num:"))
# # num2=int(input("enter 2nd num:"))
# # result=num1+num2
# # print(result)
# try:
#     result=10/2
#     print(result)
# except ZeroDivisionError:
#     print("Opps! tried to divide to zero")
#     fruits={
#         "apple":6,
#         "orange":7
#     }
# try:
#     print(fruits["orange"])
# except KeyError:
#     print("The key does not exist")
try:
    result=10/2
    print(result)
except ZeroDivisionError:
    print("Opps! tried to divide to zero")
finally:
    print("finally bloxk excecuted")

def divide_num(a,b):
    try:
        result=a/b
        print(result)
    except ZeroDivisionError:
        print("cant divide by 0")
    except TypeError:
        print("Wrong Type")
    except Exception as e:
        print({e})

divide_num(10,2)
divide_num(10,0)
divide_num(10,'2')
