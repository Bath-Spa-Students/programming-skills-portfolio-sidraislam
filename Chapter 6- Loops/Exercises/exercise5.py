sandwhich_orders = ['pastrami','Egg mayo sandwhich','pastrami','Chicken sandwhich','pastrami','Tomato sandwhich']
finished_sandwhiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop() 
    print("f*I made your{current_sandwhich}.")
    finished_sandwhiches.append(current_sandwhich)

    print("\nSandwhiches that were made:")
    for sandwhich in finished_sandwhiches:
        print(sandwhich)