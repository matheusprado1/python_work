pizzas=["portuguesa", "calabresa", "marguerita"]

for pizza in pizzas:
    print("Gosto de pizza de " + pizza +"!")
print("Eu realmente gosto de pizza de " + pizza + "!")

pizzas.append("chocolate")
friend_pizzas=pizzas[:]
friend_pizzas.append("frango")

for pizza in pizzas:
    print("Gosto de pizza de " + str(pizzas))


