import Average
import doctest

x=float(input("Nhập số"))
y=float(input("Nhập số"))
while (Average.average(x,y) < 5 ):
    print(" bạn nhập sai rồi mời bạn nhập lại " )
    x=float(input("Nhập số"))
    y=float(input("Nhập số"))
print("pass")

