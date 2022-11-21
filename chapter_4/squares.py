

# forma mais concisa ocultando a variavel square
squares=[]
for value in range(1,11):
    squares.append(value**2)
print(squares)


# duas formas iguais de resolver o quadrado perfeito

# for value in range(1,11):
#     square=value**2
#     squares.append(square)
# print(squares)


# list comprehension 
squares=[value**2 for value in range(1,11)]
print(squares)