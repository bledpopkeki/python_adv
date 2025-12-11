def add(x,y):
    return x+y
def conc(x,y):
    return str(x)+str(y)

def operate(operation,x,y):
    return operation(x,y)

result=operate(add,3,4)
print("return of sum:",result)
result_2=operate(conc,"Hello ","world"):
print("result is:",result_2)