nome = "Ebenezer"
idade =  21
profissao = "Desempregado"
linguagem = "Python"
saldo = 43.345
dados = {"nome": "Ebenezer", "idade": 21}

print("Nome: %s Idade: %s % (nome, idade")

print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {nome} Idade: {age} {nome} {age} {nome}".format(nome=nome, age=idade))

print(f"Nome: {nome} idade: {idade}")
print(f"Nome:{nome} Idade{idade} Saldo{saldo}")