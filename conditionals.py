# if else
age=25
if age >= 30:
    print('pass')
else:
    print('still young')
# ternary operator
temperature=30
read="It's warm today" if temperature >= 35 else "Wear light clothes"
print(read)
# if elif else
name='Katama'
if name=='Yvonne':
    print('my name')
elif name=='Katama':
    print("That's my sur name")
elif name=='Muelani':
    print("That's my nick name")
else:
    print("I do'nt know who that is")
# logical operators and chained conditionals
user='Student'
logged_in=False

if user=='Student' and logged_in == False:
    print('Student page')
else:
    print('Admin page,password required')

user='Student'
logged_in=True

if not logged_in:
    print('Please log in')
else:
    print('Key in user password')

user='Admin'
logged_in=True

if user=='Admin' or logged_in== True:
    print('Admin page')
else:
    print('Student page,password required')
    
