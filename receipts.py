total=0
print("Menu")
print("FISH-10,000")
print("chips-15000")
print("rice and beans-19000")
for i in range(1,4):
    menu=int(input("select menu:"))
    if menu ==1:
        print("selected fish")
        total+=10000
    elif menu ==2:
        print("selected fish") 
        total +=15000
        break
    elif menu==3:
        print("selected rice and beans ")
        total+=19000
    else:
        print("Thank you")
print("receipt",total)