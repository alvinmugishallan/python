

#Challenge 2: Total cost calculator 
def calculate_total_price(item_price,quantity):
    item_total =item_price*quantity
    tax_rate= 0.07
    tax_amount = item_total * tax_rate
    total_price=item_total + tax_amount
    return total_price
    discount = 0.1
    discounted_price= total_price-(total_price+discount)
    return discounted_price

item_price = 25.0
quantity=4

print("Total Price:",calculate_total_price(item_price,quantity))

#challenge 3
def classify_average(average):
    if average>=90:
        return"A"
    elif average>=80:
        return"B"
    elif average >= 70:
        return"C"
    elif average>=60:
        return"D"
    return "F"
student_scores= [95,88,72,65,79]
average_score=calculate_average(student_scores)
letter_grade=classify_average(average_score)
print("Average Score:",averwage_score)
print("Letter Gradse:",letter_grade)