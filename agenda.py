def verifica_indice(agenda, indice):
    indice_ajustado = indice - 1
    if indice_ajustado >= 0 and indice_ajustado < len(agenda):
        return True
    else:
        print("\nÍndice de agenda inválido!")
        return False


def adicionar_contato(agenda, nome, telefone):
    contato = {"nome": nome, "telefone": telefone, "favorito": False}
    agenda.append(contato)
    print(f"\nContato {nome} adicionado com sucesso!")
    return


def listar_contatos(agenda):
    print("\n Lista de contatos:")
    for indice, contato in enumerate(agenda, start=1):
        favorito = "★" if contato["favorito"] else "☆"
        print(f"{indice}. {favorito} {
              contato["nome"]} - {contato["telefone"]}")
    return


def editar_contato(agenda, indice_contato, novo_nome, novo_telefone):
    if verifica_indice(agenda, indice_contato):
        agenda[indice_contato - 1]["nome"] = novo_nome
        agenda[indice_contato - 1]["telefone"] = novo_telefone

        print(f"Contato {indice_contato} atualizado para {
            novo_nome} - {novo_telefone}")
    return


def favoritar_contato(agenda, indice_contato):
    if verifica_indice(agenda, indice_contato):
        agenda[indice_contato - 1]["favorito"] = True
        print(f"Contato {indice_contato} favoritado")
    return


def listar_favoritos(agenda):
    print("\n Lista de contatos favoritos:")
    for indice, contato in enumerate(agenda, start=1):
        if contato["favorito"]:
            print(f"{indice}. ★ {contato["nome"]} - {contato["telefone"]}")
    return


def apagar_contato(agenda, indice_contato):
    if verifica_indice(agenda, indice_contato):
        agenda.pop(indice_contato - 1)
        print(f"Contato {indice_contato} foi apagado")
    return


agenda = []

while True:
    print("\n Menu Agenda")
    print("\n1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Adicionar contato ao favoritos")
    print("5. Listar favoritos")
    print("6. Apagar contato")
    print("0. Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome_contato = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(agenda, nome_contato, telefone)

    elif opcao == "2":
        listar_contatos(agenda)

    elif opcao == "3":
        listar_contatos(agenda)
        indice_contato = int(
            input("Digite o número do contato que deseja editar: ")
        )
        novo_nome = input("Digite o novo nome para o contato: ")
        novo_telefone = input("Digite o novo telefone para o contato: ")
        editar_contato(agenda, indice_contato, novo_nome, novo_telefone)

    elif opcao == "4":
        listar_contatos(agenda)
        indice_contato = int(
            input("Digite o número do contato que deseja favoritar: "))
        favoritar_contato(agenda, indice_contato)

    elif opcao == "5":
        listar_favoritos(agenda)

    elif opcao == "6":
        listar_contatos(agenda)
        indice_contato = int(
            input("Digite o número do contato que deseja apagar: "))
        apagar_contato(agenda, indice_contato)

    elif opcao == "0":
        break
    else:
        print("\nOpção não encontrada!")

print("Fim de execução")
