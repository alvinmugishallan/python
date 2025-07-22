print("--MENU--")
print("APPLE")
print("ORANGE")
print("PINEAPPLE")
print(int(input("Enter friut:")))
total=0

for menu in range(1,3):
    total=+1
    if menu==1:
        print("APPLE",12000)
        total+=12000
    elif menu==2:
        print("ORANGE",10000)
        total+=10000
        break
    elif menu==3:
        print("PINEAPPLE",15000)
        total+=15000
    else:
        print("INVALID CHOICE")
print("menu")
print("recipt",total)