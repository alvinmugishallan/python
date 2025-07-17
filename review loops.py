total=0
for i in range(1,4):
    order=int(input("enter your order"))
    if order==1:
        print("Fish has been ordered")
        total+=15000   
    elif order==2:
        print(f"Cake has been ordered")
        total+=8000
    elif order==3:
        print("chips has been ordered")
        total+=7000
    elif order==4:
        print("thank you for ordering")
        break
