# names={'Eunice','Yvonne','Mercy','Nelly'}
# print('Nelly' in names)
# names.add('Becky')
# print(names)
# surnames={'Atieno','Katama','Birungi','Mweni'}
# names.update(surnames)
# print(names)
# print(names|surnames)
# surnames.discard('Katama')
# print(surnames)
# names.pop()
# print(names)

# for name in names:
#     print(name)
# fruits = {"apple", "banana", "cherry"}
# companies = {"google", "microsoft", "apple"}
# fruits.intersection_update(companies)
# print(fruits)

# a=fruits.intersection(companies)
# print(fruits)
# fruits.symmetric_difference_update(companies)
# print(fruits)
# fruits.symmetric_difference(companies)



s1={10,20,30,40,50,60}
s2={11,60,13,20,15,16}
print(s1.difference(s2))
print(s1.union(s2))
print(s1^s2)
print(s1.symmetric_difference(s2))
print(20 in s1)
print(16 not in s2)

A=frozenset(['Anna','Bella','Paul'])
B=frozenset([1,2,3,4,5])
print(A.isdisjoint(B))
print(A|B)