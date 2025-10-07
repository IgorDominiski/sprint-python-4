import json


jogadoras = {
    "nome": ["Marta", "Cristiane", "Formiga", "Bia Zaneratto"],
    "posição": ["Atacante", "Atacante", "Meio-campo", "Atacante"],
    "idade": [37, 38, 43, 30],
    "time": ["Orlando Pride", "Santos", "São Paulo", "Palmeiras"],
    "gols": [115, 98, 35, 56]
}

def salvar_json():
    with open("jogadoras.json", "w") as arquivo:
        json.dump(jogadoras, arquivo, indent=4)
    print("\n💾 Dados salvos com sucesso!")


def carregar_json():
    global jogadoras
    try:
        with open("jogadoras.json", "r") as arquivo:
            jogadoras = json.load(arquivo)
        print("\n📁 Dados carregados com sucesso!")
    except FileNotFoundError:
        print("\n⚙️ Nenhum arquivo encontrado, usando base padrão.")

def achar_indice(lista, elemento):
    for i in range(len(lista)):
        if lista[i].lower() == elemento.lower():
            return i
    return None


def indice_maior(lista):
    maior = 0
    for i in range(len(lista)):
        if lista[i] > lista[maior]:
            maior = i
    return maior


def indice_menor(lista):
    menor = 0
    for i in range(len(lista)):
        if lista[i] < lista[menor]:
            menor = i
    return menor

def cadastrar():
    try:
        nome = input("Nome da jogadora: ")
        posicao = input("Posição: ")
        idade = int(input("Idade: "))
        time = input("Time atual: ")
        gols = int(input("Quantidade de gols: "))

        jogadoras["nome"].append(nome)
        jogadoras["posição"].append(posicao)
        jogadoras["idade"].append(idade)
        jogadoras["time"].append(time)
        jogadoras["gols"].append(gols)

        print("\n⚽ Jogadora cadastrada com sucesso!")
    except Exception as erro:
        print(f"\n🚫 Erro ao cadastrar: {erro}")


def remover():
    nome = input("Qual jogadora deseja remover? ")
    i = achar_indice(jogadoras["nome"], nome)
    if i is not None:
        for chave in jogadoras:
            jogadoras[chave].pop(i)
        print("\n🗑️ Jogadora removida com sucesso!")
    else:
        print("\n🚫 Jogadora não encontrada!")


def atualizar():
    nome = input("Qual jogadora deseja atualizar? ")
    i = achar_indice(jogadoras["nome"], nome)
    if i is not None:
        for chave in jogadoras:
            novo = input(f"Novo valor para {chave} (atual: {jogadoras[chave][i]}): ")
            if novo != "":
                try:
                    if chave in ["idade", "gols"]:
                        jogadoras[chave][i] = int(novo)
                    else:
                        jogadoras[chave][i] = novo
                except:
                    print(f"Erro ao atualizar {chave}!")
        print("\n✅ Atualização concluída!")
    else:
        print("\n🚫 Jogadora não encontrada!")


def exibir_todas():
    print("\n📋 LISTA DE JOGADORAS")
    print("=====================")
    for i in range(len(jogadoras["nome"])):
        for chave in jogadoras:
            print(f"{chave}: {jogadoras[chave][i]}")
        print("---------------------")


def exibir_maior_menor():
    escolha = input("Ver [1] mais gols ou [2] menos gols? ")
    if escolha == "1":
        i = indice_maior(jogadoras["gols"])
        print("\n🏆 Jogadora com mais gols:")
    elif escolha == "2":
        i = indice_menor(jogadoras["gols"])
        print("\n🥈 Jogadora com menos gols:")
    else:
        print("Opção inválida!")
        return

    for chave in jogadoras:
        print(f"{chave}: {jogadoras[chave][i]}")

carregar_json()

while True:
    print("""
⚙️  MENU - PASSA A BOLA ⚙️
1 - Cadastrar nova jogadora
2 - Remover jogadora
3 - Atualizar jogadora
4 - Exibir todas as jogadoras
5 - Exibir jogadora com mais/menos gols
6 - Salvar e sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        remover()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        exibir_todas()
    elif opcao == "5":
        exibir_maior_menor()
    elif opcao == "6":
        salvar_json()
        print("\n👋 Tchau tchau! Viva o futebol feminino!")
        break
    else:
        print("\n🚫 Opção inválida! Tente novamente.")
