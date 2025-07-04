def menu():
    print("1.lunch")
    print("2.breakfast")

def handle_selection(selected_value):
    if selected_value==1:
        print("you have selected breakfast")
        print("BREAKFAST MENU")
        print("milk tea and muffins UGX20,000")
    elif selected_value==2:
        print("you selected lunch")
    else:
        print("please enter correct selection")

def main():
    menu()
    selected_value=int(input("please make a choice"))
    handle_selection(selected_value)
main()
