import Controller
import os.path

def criar_arquivos(*nomes):
    for i in nomes:
        if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")

criar_arquivos("categoria.txt", "estoque.txt", "clientes.txt", "fornecedores.txt", "funcionarios.txt", "venda.txt")

if __name__ == "__main__":
    while True:
        local = int(input("Digite 1 para acessar categorias\n"
                          "Digite 2 para acessar estoque\n"
                          "Digite 3 para acessar fornecedor\n"
                          "Digite 4 para acessar clientes\n"
                          "Digite 5 para acessar funcionarios\n"
                          "Digite 6 para acessar vendas\n"
                          "Digite 7 para ver os produtos mais vendidos\n"
                          "Digite 8 para sair\n"))
        
        # categoria
        if local == 1:
            cat = Controller.ControllerCategoria()
            while True:
                escolha = int(input("Digite 1 para cadastrar uma categoria\n"
                                 "Digite 2 para remover uma categoria\n"
                                 "Digite 3 para alterar uma categoria\n"
                                 "Digite 4 para mostrar as categorias cadastradas\n"
                                 "Digite 5 para sair\n"))
                # cadastrar categoria
                if escolha == 1:
                    categoria = input("Digite a categoria a ser cadastrada: ")
                    cat.cadastrar_categoria(categoria)
                # remover categoria
                if escolha == 2:
                    categoria = input("Digite a categoria que deseja remover: ")
                    cat.remover_categoria(categoria)
                # alterar categoria
                if escolha == 3:
                    antigacategoria = input("Digite a categoria que deseja alterar: ")
                    novacategoria = input("Digite o nome da categoria que substituirá a antiga: ")
                    cat.alterar_categoria(antigacategoria, novacategoria)
                # mostrar categorias
                if escolha == 4:
                    cat.mostrar_categoria()
                if escolha == 5:
                    break
        # estoque
        if local == 2:
            est = Controller.ControllerEstoque()
            while True:
                escolha = int(input("Digite 1 para cadastrar um produto no estoque\n"
                                    "Digite 2 para remover um produto do estoque\n"
                                    "Digite 3 para alterar um produto do estoque\n"
                                    "Digite 4 para mostrar os produtos do estoque\n"
                                    "Digite 5 para sair\n"))
                # cadastrar estoque
                if escolha == 1:
                    nome = input("Digite o nome do novo produto: ")
                    preco = input("Digite o preço do produto: ")
                    categoria = input("Digite a categoria do produto: ")
                    quant = input("Digite a quantidade do produto: ")
                    est.cadastrar_produto(nome, preco, categoria, int(quant))
                # remover estoque
                if escolha == 2:
                    nome = input("Digite o nome do produto que deseja remover: ")
                    est.remover_produto(nome)
                # alterar estoque
                if escolha == 3:
                    nomeantigo = input("Digite o nome do produto que deseja alterar: ")
                    nome = input("Digite o novo nome do produto: ")
                    preco = input("Digite o novo preço do produto: ")
                    categoria = input("Digite a nova categoria do produto: ")
                    quant = input("Digite a nova quantidade do produto: ")
                    est.alterar_produto(nomeantigo, nome, preco, categoria, int(quant))
                # mostrar estoque
                if escolha == 4:
                    est.mostrar_produto()
                # sair
                if escolha == 5:
                    break
        # fornecedor
        if local == 3:
            forn = Controller.ControllerFornecedor()
            while True:
                escolha = int(input("Digite 1 para cadastrar um fornecedor\n"
                                    "Digite 2 para remover um fornecedor\n"
                                    "Digite 3 para alterar um fornecedor\n"
                                    "Digite 4 para mostrar os fornecedores\n"
                                    "Digite 5 para sair\n"))
                # cadastrar fornecedor
                if escolha == 1:
                    nome = input("Digite o nome do fornecedor: ")
                    cnpj = input("Digite o cnpj do fornecedor: ")
                    telefone = input("Digite o telefone do fornecedor: ")
                    categoria = input("Digite a categoria do fornecedor: ")
                    forn.cadastrar_fornecedor(nome, cnpj, telefone, categoria)
                # remover fornecedor
                if escolha == 2:
                    nome = input("Digite o nome do fornecedor que deseja remover: ")
                    forn.remover_fornecedor(nome)
                # alterar fornecedor
                if escolha == 3:
                    nomeantigo = input("Digite o nome do fornecedor que deseja alterar: ")
                    nome = input("Digite o novo nome do fornecedor: ")
                    cnpj = input("Digite o novo cnpj do fornecedor: ")
                    telefone = input("Digite o novo telefone do fornecedor: ")
                    categoria = input("Digite a nova categoria do fornecedor: ")
                    forn.alterar_fornecedor(nomeantigo, nome, cnpj, telefone, categoria)
                # mostrar fornecedor
                if escolha == 4:
                    forn.mostrar_fornecedores()
                # sair
                if escolha == 5:
                    break
        # clientes
        if local == 4:
            clie = Controller.ControllerClientes()
            while True:
                escolha = int(input("Digite 1 para cadastrar um cliente\n"
                                    "Digite 2 para remover um cliente\n"
                                    "Digite 3 para alterar um cliente\n"
                                    "Digite 4 para mostrar os clientes\n"
                                    "Digite 5 para sair\n"))
                # cadastrar clientes
                if escolha == 1:
                    nome = input("Digite o nome do cliente: ")
                    telefone = input("Digite o telefone do cliente: ")
                    cpf = input("Digite o cpf do cliente: ")
                    email = input("Digite o email do cliente: ")
                    endereco = input("Digite o endereço do cliente: ")
                    clie.cadastrar_cliente(nome, telefone, cpf, email, endereco)
                # remover clientes
                if escolha == 2:
                    nome = input("Digite o nome do cliente que deseja remover: ")
                    clie.remover_cliente(nome)
                # alterar clientes
                if escolha == 3:
                    antigonome = input("Digite o nome do cliente q deseja alterar: ")
                    nome = input("Digite o novo nome do cliente: ")
                    telefone = input("Digite o novo telefone do cliente: ")
                    cpf = input("Digite o novo cpf do cliente: ")
                    email = input("Digite o novo email do cliente: ")
                    endereco = input("Digite o novo endereço do cliente: ")
                    clie.alterar_cliente(antigonome, nome, telefone, cpf, email, endereco)
                # mostrar clientes
                if escolha == 4:
                    clie.mostrar_clientes()
                # sair
                if escolha == 5:
                    break
        # funcionarios
        if local == 5:
            func = Controller.ControllerFuncionarios()
            while True:
                escolha = int(input("Digite 1 para cadastrar um funcionário\n"
                                    "Digite 2 para remover um funcionário\n"
                                    "Digite 3 para alterar um funcionário\n"
                                    "Digite 4 para mostrar os funcionários\n"
                                    "Digite 5 para sair\n"))
                # cadastrar funcionarios
                if escolha == 1:
                    nome = input("Digite o nome do funcionário: ")
                    clt = input("Digite a contratação clt do funcionário: ")
                    telefone = input("Digite o telefone do funcionario: ")
                    cpf = input("Digite o cpf do funcionário: ")
                    email = input("Digite o email do funcionário: ")
                    endereco = input("Digite o endereço do funcionário: ")
                    func.cadastrar_funcionario(clt, nome, telefone, cpf, email, endereco)
                # remover funcionarios
                if escolha == 2:
                    nome = input("Digite o nome do funcionário que deseja remover: ")
                    func.remover_funcionario(nome)
                # alterar funcionarios
                if escolha == 3:
                    nomeantigo = input("Digite o nome do funcionário que deseja alterar: ")
                    nome = input("Digite o novo nome do funcionário: ")
                    clt = input("Digite a nova contratação clt do funcionário: ")
                    telefone = input("Digite o novo telefone do funcionario: ")
                    cpf = input("Digite o novo cpf do funcionário: ")
                    email = input("Digite o novo email do funcionário: ")
                    endereco = input("Digite o novo endereço do funcionário: ")
                    func.alterar_funcionario(nomeantigo, clt, nome, telefone, cpf, email, endereco)
                # mostrar funcionarios
                if escolha == 4:
                    func.mostrar_funcionarios()
                # sair
                if escolha == 5:
                    break
        # vendas
        if local == 6:
            vend = Controller.ControllerVenda()
            while True:
                escolha = int(input("Digite 1 para cadastrar uma venda\n"
                                    "Digite 2 para mostrar as vendas\n"
                                    "Digite 3 para sair\n"))
                 # cadastrar venda
                if escolha == 1:
                    nome = input("Digite o nome do produto vendido: ")
                    vendedor = input("Digite o nome do vendedor: ")
                    comprador = input("Digite o nome do comprador: ")
                    quantidade = input("Digite a quantidade vendida: ")
                    vend.cadastrar_venda(nome, vendedor, comprador, quantidade)
                # mostrar vendas
                if escolha == 2:
                    data_inicial = input("Digite a data inicial a se verificar as vendas(formato: dia/mes/ano): ")
                    data_final = input("Digite a data final a se verificar as vendas(formato: dia/mes/ano): ")
                    vend.mostra_venda(data_inicial, data_final)
                # sair
                if escolha == 3:
                    break
        #produtos mais vendidos
        if local == 7:
            a = Controller.ControllerVenda()
            print("==== Relatório dos produtos ====")
            a.relatorio_produtos()
        # sair do programa
        if local == 8:
            break
            