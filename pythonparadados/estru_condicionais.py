MAIOR_IDADE = 18

idade = int(input("Informa sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")


if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.") 