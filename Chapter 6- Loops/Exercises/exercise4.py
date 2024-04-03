sandwhich_orders = ['Egg mayo sandwhich','chicken sandwhich','Tomato Sandwhich']
finished_sandwhiches=[]

while sandwhich_orders:
    current_sandwhich = sandwhich_orders.pop()
    print("f*I made your{current_sandwhich}.")
    finished_sandwhiches.append(current_sandwhich)

    print("\nSandwhiches that were made:")
    for sandwhich in finished_sandwhiches:
        print(sandwhich)
