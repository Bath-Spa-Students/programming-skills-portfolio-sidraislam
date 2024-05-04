def display_items():
    print ("Welcome to the vending machine!")
    print("1.snickers-AED 2")
    print("2.Twix-AED 2")
    print("3.Galaxy-AED 3")
    print("4.Bounty-AED 2")
    print("5.Kinder-AED 3")
    print("6.Oman chips-AED 1")
    print("7.Doritos-AED 3")
    print("8.Almarai mango juice-AED 1")
    print("9.Almarai apple juice-AED 1")
    print("10.Water-AED 1")
    print("11.Exit")


def purchase_item(item):
    print("selected item:",item)

    if item =="1" or item== "2" or item == "4":
        price= 2
        return price
    elif item=="3" or item=="5":
        price=3
        return price
    elif item=="6" or item== "10":
        price= 1
        return price
    elif item== "8" or item== "9":
        price= 1
        return price
    elif item== "11":
        return "Exit"
     
    
    else:
        return False




def run_vending_machine():
    while True:
        display_items()
        choice = str(input("enter your selection(1-11):"))
        if choice != "Exit":
            matchingitem = purchase_item(choice)
            if matchingitem == False:
                print("item not found")
            else:
                payment=int(input("Enter payment amount:"))
                if payment >= matchingitem:
                    remain = payment - matchingitem
                    print("Thankyou for purchasing Your remain amount:   ", remain)
                elif payment < matchingitem:
                    print("Payment not enough, Try again")
        elif choice == '11':
            
            print("Thank you for using the Vending Machine!")
            break

run_vending_machine()
