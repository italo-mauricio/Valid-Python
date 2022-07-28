import os
from validacoes import *
import pickle
from time import sleep


#============== Bem vindos ao meu programa básico de CRUD =================#
#==== Nele pretendo testar algumas funcionalidades de CRUD para python simples ========= #
#==== Irei implementar melhorias ao longo do tempo, e criar mais módulos ============ #
# ========================== Aproveitem! ================================= #


def menu():
    # ========== Menu Principal =========== #
    opcao = ' '
    while opcao != 0:
        os.system("cls")
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
        opcao = input('Digite a sua opção: ') # Acessa as funções totais do programa!
        if opcao == '1':
            regdados()
        elif opcao == '2':
            dadosvisu()
        elif opcao == '3':
            atuacont()
        elif opcao == '4':
            deletausu()
        elif opcao == '5':
            print("Finalizando...")
            break
        else:
            print('Opção inválida!')
            sleep(1)


def visudados(): # Listamento em arquivo binário
    try:
        dadoslist = open("dados.dat", "rb")
        dicidados = pickle.load(dadoslist)
        dadoslist.close()
    except:
        dadoslist = open("dados.dat", "wb")
        dadoslist.close() 
    return dicidados

def gravdados(dicidados): # Salvamento em arquivo binário
    dadoslist = open("dados.dat", "wb")
    pickle.dump(dicidados, dadoslist)
    dadoslist.close()

dicidados = visudados() # Dicionário já criado e já salvando em arquivo!

# =============== Função para o registro de clientes! =================== #

def regdados():
    os.system('cls')
    lista = []
    print("=="*30)
    print('Programa para validação de dados')
    print("=="*30)
    #========== Teste de verificação de nome ==========#
    while True:
        nome = input('Digite o seu nome: ')
        if validstring(nome):
            lista.append(nome)
            break
        else:
            print('Nome inválido')
    #========== Teste de verificação de idade ==========#
    while True:
        idade = input("Digite sua idade: ")
        if validnum(idade):
            lista.append(idade)
            break
        else:
            print("Idade inválida!")
    #========== Teste de verificação de gênero ==========#
    while True:
        gênero = input("Digite seu gênero [M/F/O]: ").strip().upper()
        if validstring(gênero):
            if gênero == 'M':
                print('Gênero masculino registrado com sucesso!')
                lista.append(gênero)
                break
            elif gênero == 'F':
                print('Gênero feminino registrado!')
                lista.append(gênero)
                break
            elif gênero == 'O':
                print("Outros gêneros registrados!")
                lista.append(gênero)
                break
            else:
                print('Opção inválida!')
        else:
            print('Opção contém números, tente novamente!')
                
     #========== Teste de verificação de CPF ==========#           
    while True:
        cpf = input('Digite seu cpf: ')
        if cadastrocpf(cpf):
            if cpf not in dicidados:
                dicidados[cpf] = lista
                print('Dados salvos com sucesso!') # Após o teste de verificação, ele guarda as informações na chave CPF
                gravdados(dicidados)
                continuar = input('Você quer conntinuar [S/N]: ').upper().strip() # Pergunta se o usuário quer continuar
                if validstring(continuar):
                    if continuar.startswith('S'):
                        regdados()

                    if continuar.startswith('N'):
                        menu()
                    else:
                        print('Opção inválida!')
            else:
                print('Gênero já está no dicionario')
    input('Aperte alguma tecla para continuar!')
    menu()
      
# =============== Função para o visualização de clientes! =================== #

def dadosvisu():
    os.system('cls')
    print('=='*30)
    print('Vamos visualizar seus dados!')
    print('=='*30)
   
    while True:
        cpf = input("Digite seu cpf: ") # Usa o CPF como base para achar o usuário!
        if cadastrocpf(cpf):
            if cpf in dicidados:
                print('CPF encontrado!')
                print(dicidados[cpf])
                continuar = input('Você quer conntinuar [S/N]: ').upper().strip() # Pergunta se o usuário quer continuar
                if validstring(continuar): # Faz a verificação se é string ou não
                    if continuar.startswith('S'):
                        dadosvisu()
                    if continuar.startswith('N'):
                        menu()
                    else:
                        print('Opção inválida!')

                else:
                    print("Opção inválida!")
                
            else: 
                print('CPF não encontrado!')
            
        else:
            print("CPF inválido!")
            continuar = input('Você quer conntinuar [S/N]: ').upper().strip() 
            if validstring(continuar):
                    if continuar.startswith('S'):
                        dadosvisu()
                    if continuar.startswith('N'):
                        menu()
                    else:
                        print('Opção inválida!')

            else:
                print("Opção inválida!")
            
            
            
# =============== Função para atualizar o registro de clientes! =================== #

def atuacont():
    os.system('cls')
    print('=='*30)
    print("Vamos atualizar seus dados!")
    print("=="*30)
    while True:
        cpf = input("Digite seu cpf: ") # Usuário digita a chave que é o seu cpf
        if cadastrocpf(cpf):
            while True:
                cadastro = ' '
                cadastro = input('Digite a opção que você deseja alterar: ').upper().strip() # Usuário digita qual tipo de informação ele quer alterar

# ============================================ NOME ===============================================================#
# =================================================================================================================#      
                if cadastro == 'nome'.upper(): # Se o usuário digitar nome ele entra
                    print("Okay, você deseja alterar seu nome...")
                    nome_novo = input("Por favor, digite o novo nome: ").strip() # Pergunta ao usuário o novo nome
                    if validstring(nome_novo): # Passa pela validação!
                        dicidados[cpf][0] = nome_novo
                        print('Nome atualizado com sucesso!') # Adiciona o nome novo ao dicionário
                        gravdados(dicidados)
                        continuar = input("Deseja continuar atualizando seus dados? [S/N]: ").upper().strip() # Pergunta se quer continuar
                        if continuar.startswith('S'):
                            print('Tudo bem, vamos novamente...')
                            sleep(2)
                            atuacont()
                        if continuar.startswith('N'):
                            print("Obrigado, volte sempre!")
                            sleep(2)
                            menu()
                        else:
                            print("Opção inválida!")
                    else:
                        print("Nome inválido") # A validação aceita somente letras

# ============================================ IDADE ==============================================================# 
# =================================================================================================================#          
                if cadastro == 'idade'.upper(): # Se o usuário digitar idade ele entra
                    print("okay, você deseja altrar sua idade...")
                    idade_nova = input("Por favor, digite sua nova idade: ").strip()
                    if validnum(idade_nova): # Veirifica se é um número
                        dicidados[cpf][1] = idade_nova
                        print('Sua idade foi alterada com sucesso!') # Adiciona a nova idade ao dicionário
                        print(f"Sua nova idade é {idade_nova}")
                        gravdados(dicidados)
                        continuar = ' '
                        continuar = input("Deseja continuar atualizando seus dados? [S/N]: ").upper().strip()
                        if continuar.startswith('S'):
                            print("Tudo bem, vamos novamente...")
                            sleep(2)
                            atuacont()
                            
                        elif continuar.startswith('N'):
                            print("Obrigado, volte sempre!")
                            menu()
                        else:
                            print('Opção inválida')
                        
                    else:
                        print("Idade inválida!")

# ============================================ GÊNERO ==============================================================# 
# ==================================================================================================================#     
                if cadastro == 'genero'.upper(): # Se o usuário digitar genero, ele entra
                    print("Okay, você deseja alterar seu gênero...")
                    genero_novo = input("Por favor, digite seu novo gênero: ").strip()
                    if validstring(genero_novo): # Verifica se é uma string
                        dicidados[cpf][2] = genero_novo
                        print("Gênero alterado com sucesso!") # Adiciona o novo gênero ao dicionário
                        print(f'Seu novo gênero é {genero_novo}') 
                        gravdados(dicidados)
                        continuar = input("Deseja continuar atualizando seus dados? [S/N]: ").upper().strip()
                        if continuar.startswith('S'):
                            print("Tudo bem, vamos novamente...")
                            sleep(2)
                            atuacont()
                        if continuar.startswith('N'):
                            print("Obrigado, volte sempre!")
                            sleep(2)
                            menu()
                        else:
                            print("Opção inválida!")
                    else:
                        print("Idade inválida!")
                else:
                    print('Opção inválida!')
        else:
            print("CPF inválido!")
            continuar = input('Você quer conntinuar [S/N]: ').upper().strip()
            if validstring(continuar):
                    if continuar.startswith('S'):
                        atuacont()

                    if continuar.startswith('N'):
                        menu()
                    else:
                        print('Opção inválida!')
            else:
                print('Opção inválida!')
                
# =============== Função para deletar o registro de clientes! =================== #

def deletausu():
    os.system("cls")
    print('=='*30)
    print('Vamos deletar o usuário!')
    print('=='*30)
    while True:
        cpf = input('Digite o cpf que você quer deletar: ') # Deleta o usuário a partir da chave
        if cadastrocpf(cpf):
            if cpf not in dicidados:
                print("CPF não encontrado!")
                continuar = input('Você quer conntinuar [S/N]: ').upper().strip()
                if validstring(continuar):
                    if continuar.startswith('S'):
                        deletausu()

                    if continuar.startswith('N'):
                        menu()
                    else:
                        print('Opção inválida!')
                
            else:
                print("CPF encontrado!") # Se ele achar, ele deleta a chave de acesso (CPF)
                del dicidados[cpf]
                print("CPF deletado!")
                gravdados(dicidados)
                continuar = input('Você quer conntinuar [S/N]: ').upper().strip()
                if validstring(continuar):
                    if continuar.startswith('S'):
                        deletausu()

                    if continuar.startswith('N'):
                        menu()
                    else:
                        print('Opção inválida!')
                
        else:
            print('Digite um CPF válido!')
            
    

         

# ============= Chamamento da função menu =============== #
menu()

        













            

            
       
