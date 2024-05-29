import os
from time import sleep
os.system('cls')
pessoa = {}

print("-" * 10, "CADASTRO", "-" * 10)
print("Informe os dados do usuario.")
pessoa['nome'] = str(input("NOME: "))
pessoa['cpf'] = str(input("cpf: "))
pessoa['rg'] = str(input("rg: "))
pessoa['data_nasc'] = str(input("data de nascimento: "))
pessoa['genero'] = str(input("gênero: "))
pessoa['email'] = str(input("Email: "))
pessoa['telefone'] = str(input("Telefone: "))
pessoa['tipo_sangue'] = str(input("Tipo sanguineo: "))
pessoa['profissao'] = str(input("Profissão: "))
pessoa['empresa'] = str(input("Empresa: "))

os.system('cls')

print("A pessoa foi cadastrada com os seguintes atributos")
for atributo in pessoa:
    sleep(0.2)
    print(f"{atributo}: {pessoa.get(atributo)}")
