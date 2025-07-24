n=int(input("Enter number:",))
print(n+1)
def  is_prime(n):
        if n <= 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n %i ==0:
                return False
        return True  
#ask the user for input   
number=int(input("Enter a number to check if its a prime"))
#calling the function and showing result 
if is_prime(number):
     print(f"{number}is a prime number")
else:
     print("f{number}is not a  prime number")
         