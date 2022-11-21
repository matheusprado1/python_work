odd_numbers=list(range(1,21,2))
print(odd_numbers)
for value in odd_numbers:
    print(value)

multiples_of_three=list(range(3,31,3))
print(multiples_of_three)
for value in multiples_of_three:
    print(value)

cubes=[]
for value in range(1,11):
    cubes.append(value**3)
print(cubes)

# list comprehension
cubes=[value**3 for value in range(1,11)]
print(cubes)
