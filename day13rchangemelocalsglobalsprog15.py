x=5;y=7
def changeme(mylist_var):
    "this function demonstrates local and global variables"
    p=99
    global x,y
    x=y+2
    mylist=[1,2,3,4]
    
    print("values inside the function:",mylist)
    print("local variable are:",locals())
    print("global variable are:",globals())
    return
mylist_var=[10,20,30]
changeme(mylist_var)
print("value outside the funcion:",mylist_var)
