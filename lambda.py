add=lambda a,b:a+b
print(add(10,10))

# Program to square each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x ** 2 , my_list))

print(new_list)

# Program to filter out only the odd items from a list usingirth filter
my_list = [2, 5, 10, 15, 0, 125, 45, 12]

new_list = list(filter(lambda x: (x%5 == 0) , my_list))

print(new_list)

names_list=['Eunice','Mike','Paul','Popo','Yvonne','Lavline']
new_list=list(filter(lambda y: (y%2==0),names_list))

print(new_list)







