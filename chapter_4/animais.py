animais=["cachorro", "gato", "ramster", "coelho", "macaco"]

for animal in animais:
    print("Um " + animal.title() + " seria um ótimo animal de estimação.\n")

print("Qualquer um desses animais seria um ótimo animal de estimação !")

# fatias
print("Os 3 primeiros animais são: ")
print(animais[:3])
print("Os 3 animais do meio são: ")
print(animais[1:-1])
print("Os 3 ultimos animais são: ")
print(animais[2:5])
