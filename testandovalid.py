import os
from validacoes import *
import pickle
import turtle
import os
from time import sleep





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
    lista = []
    print('Programa para validação de dados')
    while True:
        nome = input('Digite o seu nome: ')
        if validstring(nome):
            break
        else:
            print('Nome inválido')

    while True:
        idade = input("Digite sua idade: ")
        if validnum(idade):
            break
        else:
            print("Idade inválida!")

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
                lista.append(nome, idade, gênero)
                dicidados[cpf] = lista
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

    if cadastrocpf(cpf):
        while True:
            if cpf in dicidados:
                print('CPF encontrado!')
                print(dicidados[cpf])
                break
            else: 
                print('CPF não encontrado!')
                continuar = input('Você quer conntinuar [S/N]: ')
                if continuar == 'S':
                    return cpf
                if continuar == 'N':
                    break
                

        input("Aperta qualquer tecla para sair!")
        menu()
    else:
        print("CPF inválido!")
        


def atuacont():
    os.system('cls')
    print('=='*30)
    print("Vamos atualizar seus dados!")
    print("=="*30)
    cpf = input("Digite seu cpf: ")
    if cadastrocpf(cpf):
        while True:
            cadastro = ' '
            cadastro = input('Digite a opção que você deseja alterar: ').upper().strip()
            if cadastro == 'nome'.upper():
                print("Okay, você deseja alterar seu nome...")
                nome_novo = input("Por favor, digite o novo nome: ").strip()
                if validstring(nome_novo):
                    dicidados[cpf][0] = nome_novo
                    print('Nome atualizado com sucesso!')
                    gravdados(dicidados)
                    continuar = input("Deseja continuar atualizando seus dados? [S/N]: ").upper().strip()
                    if continuar.startswith('S'):
                        return cadastro
                    if continuar.startswith('N'):
                        menu()
                    else:
                        print("Opção inválida!")
                else:
                    print("Nome inválido")
            if cadastro == 'idade'.upper():
                print("okay, você deseja altrar sua idade...")
                idade_nova = input("Por favor, digite sua nova idade: ").strip()
                if validnum(idade_nova):
                    dicidados[cpf][1] = idade_nova
                    print('Sua idade foi alterada com sucesso!')
                    print(f"Sua nova idade é {idade_nova}")
                    gravdados(dicidados)
                    continuar = input("Deseja continuar atualizando seus dados? [S/N]: ")
                    if continuar == 'S':
                        return cadastro
                    if continuar == 'N':
                        exit
                    else:
                        print("Opção inválida!")
                else:
                    print("Idade inválida!")
            if cadastro == 'genero'.upper():
                print("Okay, você deseja alterar seu gênero...")
                genero_novo = input("Por favor, digite seu novo gênero: ").strip()
                if validstring(genero_novo):
                    dicidados[cpf][2] = genero_novo
                    print("Gênero alterado com sucesso!")
                    print(f'Seu novo gênero é {genero_novo}')
                    gravdados(dicidados)
                    continuar = input("Deseja continuar atualizando seus dados? [S/N]: ")
                    if continuar == 'S':
                        return cadastro
                    if continuar == 'N':
                        break
                    else:
                        print("Opção inválida!")
                else:
                    print("Idade inválida!")
    else:
        print("CPF inválido!")
        sleep(1)
            


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












            

            
       
