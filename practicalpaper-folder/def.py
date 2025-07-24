def function1(x):
    return 8*x
n=function1(3)
print(n)

def function3(x,y):
    return x+y
a=function3 (9,10)
print(a)

name1="John"
height_m1=2
weight_kg=75
name2="Mercy"
height_m2=5
weight_kg=80
name3= "tev"
height_m3=7
weight_kg=100
def bou_calculator(name,height_m,weight_kg):
    bm1=weight_kg/(height_m **2)
    print(bm1)
    if bm1<10:
        return name + "not_overweight"
    else:
        return name +"is_overweight"
result1=bou_calculator(name1,height_m1,weight_kg)
result2=bou_calculator(name2,height_m2,weight_kg)
result3=bou_calculator(name3,height_m3,weight_kg)
print(result1)
print(result2)
print(result3)
