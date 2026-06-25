produtos = []
prox_id = 1

def criar_produto(nome_usuario,  preco_produto):
    global prox_id
    novo_produto = {
        "id": prox_id,
        "nome": nome_usuario,
        "preco": preco_produto
    }
    produtos.append(novo_produto)
    prox_id += 1
    print(f"Produto '{nome_usuario}' criado com sucesso!")


def ler_produtor():
    if not produtos:
        print(f"Nenhum produto cadastrado")
        return
        
    print(f"------Lista de Produtos------")
    for prod in produtos:
        print(f"ID: {prod['id']} | Nome: {prod['nome']} | Preço: R${prod['preco']:.2f}")

def buscar_produto(id_produto):
    for prod in produtos:
        if prod["id"] == id_produto:
            print(f"ID: {prod['id']} | Nome: {prod['nome']} | Preço: R${prod['preco']:.2f}")
            return
    print(f"Produto com ID {id_produto} não encontrado.")

def atualizar_produto(id_produto, novo_nome, novo_preco):
    for prod in produtos:
        if prod["id"] == id_produto:
            prod["nome"] = novo_nome
            prod["preco"] = novo_preco
            print(f"Produto com ID {id_produto} atualizado com sucesso!")
            return
    print(f"Produto com ID {id_produto} não encontrado.")


def deletar_produto(id_produto):
    for prod in produtos:
        if prod["id"] == id_produto:
            produtos.remove(prod)
            print(f"Produto com id {id_produto} deletado com sucesso!!!")
            return
    print(f"Produto com id {id_produto} não encontrado!!!")


def main():
    print("-------Criando Produto-------")
    nome_usuario = input("Digite o nome do produto:")
    preco_produto = float(input("Digite o preço do produto:"))
    criar_produto(nome_usuario, preco_produto)

    while True:
        print("------Menu de Produtos------")
        print("1. Listar Produtos")
        print("2. Buscar Produto")
        print("3. Atualizar Produto")
        print("4. Deletar Produto")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ler_produtor()
        elif opcao == "2":
            id_produto = int(input("Digite o ID do produto que deseja buscar:"))
            buscar_produto(id_produto)
        elif opcao == "3":
            id_produto = int(input("Digite o ID do produto que deseja atualizar:"))
            novo_nome = input("Digite o novo nome do produto:")
            novo_preco = float(input("Digite o novo preço do produto:"))
            atualizar_produto(id_produto, novo_nome, novo_preco)
        elif opcao == "4":
            id_produto = int(input("Digite o ID do produto que deseja deletar:"))
            deletar_produto(id_produto)
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
