def outer():
    message='outer function'
    print(message)

    def inner():
        #print('inner function')
        print(message)
        
    inner()
    
outer()
