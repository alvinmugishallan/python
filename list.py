#user input
numbers = []
print("Enter 5 numbers")
for i in range (5):
    num= int(input())
    numbers.append(num)

#step 2: Displays the result 
print("Numbers:",numbers)
print("Maximum:",max(numbers))
print("Minium:",min(numbers))
print("Average:",sum(numbers)/
len(numbers))
print("sorted:",sorted(numbers))