a=1
def myfunction():
    global a #this is global var
    print('global a=',a)
    a=2
    print('modified a=',a)
myfunction()
print('global a=',a)  #display modified value
