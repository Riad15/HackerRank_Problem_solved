n =int(input(""))
if n % 4 ==0:
    print("True")
elif n % 100 == 0 and n % 400 == 0:
    print("True")
else:
    print("False")