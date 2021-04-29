user='Admin'
logged_in =True,


if user=='Student' and logged_in== False:
    print('Student page')
elif user=='Admin' or logged_in== True:
    user_input=input("Enter password:")
else:
    print('user unrecognized')

# user='Student'
# logged_in=True

# if not logged_in:
#     print('Please log in')
# else:
#     print('Key in user password')



# user='Admin'
# logged_in=True

# if user=='Admin' or logged_in== True:
#     print('Admin page')
# else:
#     print('Student page,password required')
    
