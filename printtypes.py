#PRINT STATEMENT TYPES

# 1. USING SEPERATORS
    # SEPERATORS IS USED FOR VARIABLES
'''
a=4
b=5
print(a,b)         #normal representation
print(a,b,sep=',')   #using special character seperator comma(,)
print(a,b,sep='&')   #using special character seperator ampersand(&)
print(a,b,sep='\n')   #using escape-sequece character (\n)
'''

#2. USE OF ESCAPE SEQUENCE CHARACTERS LIKE (\n),(\t).
    #syntax: 
    # ESCAPE SEQUECNE IS USED FOR STRINGS
    #for instance consider two print statements, namely
'''
print('Hello',end='\n')
print('Dear')
'''
    #SINGLE SPACE() AND MULTIPLE SPACES FOR INSTANCE 5 RESEMBLES TAB FUCNTIONALITY.
    # WHEN NO SPACE IS GIVEN INSIDE THE BRACES.

    #WRITE EXAMPLES FOR THIS 

#3.PRINT("STRING", VARIBALE LIST) STATEMENTS
        #ONLY USE COMMA IN THIS CASE OTHER CHARACTERS WILL NOT WORK IN BELOW CASE
'''
a=2
print(a,"is even number")
print("you typed", a, "as input")
'''

#4. print(formatted string)statement

    # syntax: print("formatted string" %(varible list))
    #since we are declaring the format of the string in the statment we call it a formatted string. 
    #THERE'S NO NEED OF USING COMMA(,)WHEN USING %WHILE CALLING THE VALUES IN THE END.
    #In formatted string we use
        # %i (or) %d for integer
        # %f for float
        # %s for strings.
        # %.f to round off ; %.2f to rounding off integers by two values
        # %10s for giving 10 spaces after priting string ; %20s for giving 20 spaces after printing the string.

'''
x,y,z=10,12,15
print(x,y,z,sep=',')
print('x=%d,y=%f,z=%d'%%(x,y,z))
'''

'''
name='codegnan'
print('Hi %s' %name)
print('Hi %20s' %name)
#print('Hi %s,%s' %(name[0],name[0]))
print('Hi %s' %(name[0:3]))
'''


'''
num=123.4567
print("The value is %d"%num)
print("The value is :%.2f"%num)
'''

#5. print('format string with replacement fields'.format(values))
    #always inside replacement field  denoted by Curly Braces{}.

#In below case the index will be pointing to the declares variables but not to the defined variables.
        #Expected Result: number1= a, number2=b
        #Obtained Result: number1=b, number2=a

'''
n1,n2,n3='a','b','c'
print(n1,n2,n3)
print('number1={0},number2={1}'.format(n2,n1))


name,place='saketh','karimnagar'
print('Hello{0} your place is {1}'.format(name,place))
'''



#6. Sample Input Statements
    #When input() fuction is used it expects string but we can give any data type
    #When int(input()) function

'''
c= input("Enter a Character:")
print("You entered: "+c)

str=input('enter a number:')
x=int(str)
print(x)
'''


#7. To accept two numbers and find their sum

#Taking single Input.
'''
x=int(input("Enter first Number:"))
y=int(input("Enter second Number:"))
print('Sum of {} and {} is {}'.format(x,y,x+y))
'''

#Taking Inputs and performing operations in same line.
'''
x,y,z=(int(x) for x in input("Enter three numbers:").split(',')
'''
#eval() function takes a string and evaluates the result.
'''
a,b=10,5
result=eval("a+b-5")
print(result)
'''

#to find area of circle: 
import numpy 







