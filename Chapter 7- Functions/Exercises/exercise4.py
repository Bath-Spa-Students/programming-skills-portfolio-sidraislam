def make_shirt(size='large',message='I love python'):
    """"Summarize the shirt that was made"""
    print("\nI made a "+ size +"t-shirt.")
    print("It printed"+ message+"on the front.")

    make_shirt()
    make_shirt(size='medium')
    make_shirt('small','python is cool')