import os
from validacoes import *
import pickle

def menu():
    print("=="*30)
    print('''
    |============== Menu Inicial ==================|
    |:\ \ \  Bem vindo a validação dados / / / / /:|
    |:    |...... Cadastrar dados! [1] ......|    :|
    |:    |...... Visualizar dados![2] ......|    :|
    |:    |...... Atualizar dados! [3] ......|    :|
    |:    |...... Deletar dados!   [4] ......|    :|
    |:    |...... Sair             [5] ......|    :|
    |:=============================================|
    ''')
    print("=="*30)
    opcao = ' '
    opcao = input('Digite a sua opção: ')
    while opcao != '0':
        if opcao == '1':
            regdados()
        elif opcao == '2':
            dadosvisu()
        elif opcao == '3':
            atuacont()
        elif opcao == '4':
            deletausu()
        else:
            print('Opção inválida!')
            break

def visudados():
    try:
        dadoslist = open("dados.dat", "rb")
        dicidados = pickle.load(dadoslist)
        dadoslist.close()
    except:
        dadoslist = open("dados.dat", "wb")
        dadoslist.close() 
    return dicidados

def gravdados(dicidados):
    dadoslist = open("dados.dat", "wb")
    pickle.dump(dicidados, dadoslist)
    dadoslist.close()

dicidados = visudados()
def regdados():
    print('Programa para validação de dados')
    while True:
        nome = input('Digite o seu nome: ')
        if validstring(nome):
            break
        else:
            print('Nome inválido')
            return False
    while True:
        idade = input("Digite sua idade: ")
        if validnum(idade):
            break
        else:
            print("Idade inválida!")
            return False
    while True:
        
        gênero = input("Digite seu gênero [M/F/O]: ").strip().upper()
        if validstring(gênero):
            if gênero == 'M':
                print('Gênero masculino registrado com sucesso!')
                break
            elif gênero == 'F':
                print('Gênero feminino registrado!')
                break
            elif gênero == 'O':
                print("Outros gêneros registrados!")
                break
            else:
                print('Opção inválida!')
                return False
    while True:
        cpf = input('Digite seu cpf: ')
        if cadastrocpf(cpf):
            if cpf not in dicidados:
                dicidados[cpf] = [nome, idade, gênero]
                print('Dados salvos com sucesso!')
                gravdados(dicidados)
                break
            else:
                print('Gênero já está no dicionario')
    menu()
      

def dadosvisu():
    os.system('cls')
    print('=='*30)
    print('Vamos visualizar seus dados!')
    print('=='*30)
    cpf = input("Digite seu cpf: ")
    while True:
        if cpf not in dicidados:
            print('CPF não encontrado!')
            cpf = input("Digite seu cpf: ")
        else:
            print('CPF encontrado!')
            print(dicidados[cpf])
            break
        input("Aperte qualquer tecla para continuar!: ")
    menu()

def atuacont():
    print('=='*30)
    print("Vamos atualizar seus dados!")
    print("=="*30)
    cpf = input("Digite seu cpf: ")
    while True:
        if cadastrocpf(cpf):
            cadastro = ' '
            cadastro = input('Digite a opção que você deseja alterar: ').upper()
            if cadastro == 'nome'.upper():
                print("Okay, você deseja alterar seu nome...")
                nome_novo = input("Por favor, digite o novo nome: ")
                if validstring(nome_novo):
                    dicidados[cpf][1] = nome_novo
                    print('Nome atualizado com sucesso!')
                    gravdados(dicidados)
                    break
                else:
                    print("Nome inválido")
        else:
            print("CPF inválido!")
            return False
    menu()


def deletausu():
    print('=='*30)
    print('Vamos deletar o usuário!')
    print('=='*30)
    cpf = input('Digite o cpf que você quer deletar: ')
    while True:
        if cpf not in dicidados:
            print("CPF não encontrado!")
            cpf = input('Digite o cpf que você quer deletar: ')
        else:
            print("CPF encontrado!")
            del dicidados[cpf]
            print("CPF deletado!")
            gravdados(dicidados)
            break
    menu()

         



        
menu()












            

            
       
