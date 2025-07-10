n=int(input("Enter number:"))
sum_of_evens=0 
print("Even Numbers from 1")
for number in range(1,101):
    if number %2 ==0:
            print("Even numbers are:",number)
            sum_of_evens += n
print("sum of even numbers:",sum_of_evens)