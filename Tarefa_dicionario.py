meu_dicionario = {}

while True:

    print(meu_dicionario)
    op = input("(1) adicionar tarefa \n(2) apagar tarefa \n(3) editar status \n(4) sair : ")

    if op == "1":
        Tarefa = input("Qual a tarefa: ")
        status = input("(1) para concluido\n(2) para pendente: ")

        if status == "1":
            meu_dicionario[Tarefa] = "concluido"
            print("lista atualizada")
         
        elif status == "2":
            meu_dicionario[Tarefa] = "pendente"
            print("lista atualizada")    

    elif op == "2":
        delete = input("qual tarefa voce quer apagar: ")
        if delete in meu_dicionario:
            del meu_dicionario[delete]
        else:
            print("tarefa não encontrada")
        
    elif op == "3":
        edit = input("qual tarefa trocar os status: ")
        stat = input("(1) concluida \n(2) pendente")
        if stat == "1":
            meu_dicionario[edit] = "concluido"
            print("lista atualizada")

        elif stat == "2":
            meu_dicionario[edit] = "pendente"
            print(meu_dicionario)
            print("lista atualizada")
    
    elif op == "4":
        break