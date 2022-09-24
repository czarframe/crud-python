aluno = dict()
lista = list()


def bem_vindo():
    print("############################################")
    print("########## SEJA BEM VINDO AO CRUD ##########")
    print("############################################")

def adeus():
    print("#################################")
    print("########## FINALIZADO! ##########")
    print("#################################")

def menu():
    while True:
        try:
            print("\n1 - Cadastrar")
            print("2 - Atualizar")
            print("3 - Deletar")
            print("4 - Listar")
            print("5 - Fechar")
            opcao = int(input("Digite uma opção: "))
            if opcao == 1:
                cadastrar_aluno()
            elif opcao == 2:
                atualizar_aluno()
            elif opcao == 3:
                deletar_aluno()
            elif opcao == 4:
                listar_alunos()
            elif opcao == 5:
                adeus()
                break
            else:
                print("\nDigite uma opção válida!")
        except ValueError:
            print("\nDigite uma opção válida!")


def set_id(aluno):
    while True:
        try:
            aluno["id"] = int(input("\nDigite o ID: "))
            if aluno.get("id") > 0:
                for i in lista:
                    if i.get("id") == aluno.get("id"):
                        print("ID já existente!")
                        set_id(aluno)
                        break
                break
            else:
                print("\nDigite uma ID válida!\n")
        except ValueError:
            print("Digite uma ID válida!")


def set_all(aluno):
    set_nome(aluno)
    set_idade(aluno)
    set_curso(aluno)
    set_cpf(aluno)


def set_idade(aluno):
    while True:
        try:
            aluno['idade'] = int(input("Digite a idade: "))
            if aluno.get("idade") <= 0 or aluno.get("idade") >= 115:
                print("\nDigite uma idade válida!\n")
            else:
                break
        except ValueError:
            print('Digite uma idade válida!')


def set_nome(aluno):
    while True:
        aluno["nome"] = str(input("Digite o nome: ")).title()
        if len(aluno.get("nome")) >= 3:
            break
        else:
            print("\nDigite um nome válido!\n")


def set_cpf(aluno):
    while True:
        try:
            aluno["cpf"] = int(input("Digite o CPF: "))
            aluno["cpf"] = str(aluno.get("cpf"))
            if len(aluno.get("cpf")) == 11:
                aluno["cpf"] = aluno.get("cpf").zfill(11)
                aluno["cpf"] = '{}.{}.{}-{}'.format(aluno.get("cpf")[:3], aluno.get("cpf")[3:6], aluno.get("cpf")[6:9],
                                                    aluno.get("cpf")[9:])
                for i in lista:
                    if i.get("cpf") == aluno.get("cpf") and i != aluno:
                        print("\nCPF já cadastrado!\n")
                        set_cpf(aluno)
                        break
                break
            else:
                print("\nDigite um CPF válido!\n")
        except ValueError:
            print("\nDigite um CPF válido!\n")


def set_curso(aluno):
    while True:
        aluno["curso"] = input("Digite o curso: ").title()
        if len(aluno.get("curso")) >= 2:
            break
        else:
            print("\nDigite um curso válido!\n")


def cadastrar_aluno():
    while True:
        set_id(aluno)
        set_all(aluno)
        lista.append(aluno.copy())
        aluno.clear()
        print("\nAluno cadastrado com sucesso!\n")

        while True:
            resp = str(input("Efetuar novo cadastro? S/N\n")).upper()[0]
            if resp in "S/N":
                break
            else:
                print("\nDigite uma opção válida!\n")

        if resp == "N":
            break


def atualizar_aluno():
    verificador = True
    try:
        if len(lista) > 0:
            id = int(input("Digite a ID do aluno a ser atualizado: "))
            for i in lista:
                if i.get("id") == id:
                    verificador = True
                    print("\n1 - Alterar nome")
                    print("2 - Alterar idade")
                    print("3 - Alterar CPF")
                    print("4 - Alterar curso")
                    print("5 - Alterar tudo")
                    print("6 - Fechar")
                    try:
                        opcao = int(input("Digite uma opção: "))
                        if opcao == 1:
                            set_nome(i)
                            print("\nNome atualizado com sucesso!")
                            aluno.clear()
                            break
                        elif opcao == 2:
                            set_idade(i)
                            print("\nIdade atualizado com sucesso!")
                            aluno.clear()
                            break
                        elif opcao == 3:
                            set_cpf(i)
                            print("\nCPF atualizado com sucesso!")
                            aluno.clear()
                            break
                        elif opcao == 4:
                            set_curso(i)
                            print("\nCurso atualizado com sucesso!")
                            aluno.clear()
                            break
                        elif opcao == 5:
                            set_all(i)
                            print("\nTodos os dados foram atualizados com sucesso!")
                            aluno.clear()
                            break
                        elif opcao == 6:
                            aluno.clear()
                            break
                        else:
                            print("\nDigite uma opção válida!\n")
                    except ValueError:
                        print("\nDigite uma opção válida!\n")
                else:
                    verificador = False
        else:
            print("\nA lista está vazia!\n")
        if not verificador:
            print("\nO aluno não foi encontrado!")
    except ValueError:
        print("\nDigite uma ID válida!\n")


def listar_alunos():
    verificador = True
    if len(lista) > 0:
        while True:
            try:
                print("\n1 - Listar tudo")
                print("2 - Listar aluno")
                print("3 - Fechar")
                opcao = int(input("Digite uma opção: "))

                if opcao == 1:
                    for i in lista:
                        print("\nId: {}".format(i.get("id")))
                        print("Nome: {}".format(i.get("nome")))
                        print("Idade: {}".format(i.get("idade")))
                        print("CPF: {}".format(i.get("cpf")))
                        print("Curso: {}".format(i.get("curso")))

                elif opcao == 2:
                    try:
                        id = int(input("\nDigite o ID do aluno a ser listado: "))
                        for i in lista:
                            if i.get("id") == id:
                                print("\nId: {}".format(i.get("id")))
                                print("Nome: {}".format(i.get("nome")))
                                print("Idade: {}".format(i.get("idade")))
                                print("CPF: {}".format(i.get("cpf")))
                                print("Curso: {}".format(i.get("curso")))
                                verificador = True
                                break
                            else:
                                verificador = False
                    except ValueError:
                        print("\nDigite uma ID válida!")
                elif opcao == 3:
                    break
                else:
                    print("\nDigite uma opção válida!\n")
                if not verificador:
                    print("\nO aluno não foi encontrado!")
            except ValueError:
                print("\nDigite uma opção válida!")
    else:
        print("\nA lista está vazia!")


def deletar_aluno():
    verificador = True
    if len(lista) > 0:
        while True:
            try:
                print("\n1 - Deletar aluno")
                print("2 - Deletar tudo")
                print("3 - Fechar")
                opcao = int(input("Digite uma opção: "))
                if opcao == 1:
                    try:
                        id = int(input("\nID do aluno a ser deletado: "))
                        for i in lista:
                            if i.get("id") == id:
                                lista.remove(i)
                                print("\nO aluno foi removido com sucesso!")
                                verificador = True
                                break
                            else:
                                verificador = False
                    except ValueError:
                        print("\nDigite uma ID válida!")
                elif opcao == 2:
                    for i in lista:
                        lista.remove(i)
                    print("\nTodos os alunos foram removidos com sucesso!")
                elif opcao == 3:
                    break
                else:
                    print("\nDigite uma opção válida!\n")
                if not verificador:
                    print("\nO aluno não foi encontrado!")
            except ValueError:
                print("\nDigite uma opção válida!\n")
    else:
        print("\nA lista está vazia!")


if __name__ == "__main__":
    bem_vindo()
    menu()