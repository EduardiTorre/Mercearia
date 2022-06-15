from sqlalchemy import PrimaryKeyConstraint
from Models import *
from DAO import *


class ControllerCategoria:
    def cadastrar_categoria(self, novacategoria):
        existe = False
        
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novacategoria:
                existe = True

        if existe != True:
            DaoCategoria.salvar(novacategoria)
            print('Categoria cadastrada com sucesso.')
        else:
            print('A categoria cadastrada já existente.')
    
    def remover_categoria(self, removercategoria):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == removercategoria, x)) # rever lambda

        if len(cat) <= 0:
            print('A categoria que deseja remover não existe.')
        else:
            for i in range(len(x)):
                if x[i].categoria == removercategoria:
                    del x[i]
                    break
            with open('categoria.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')

            print('Categoria removida com sucesso.')

            estoque = DaoEstoque.ler()
            estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, "Sem categoria"), x.quantidade)
                      if(x.produto.categoria == removercategoria) else(x), estoque))
            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + '|' +
                                   i.produto.preco + '|' +
                                   i.produto.categoria + '|' +
                                   str(i.quantidade))
                    arq.writelines('\n')

    def alterar_categoria(self, antigacategoria, novacategoria):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == antigacategoria, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == novacategoria, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categorias(novacategoria) if(x.categoria == antigacategoria) else(x), x))
                print('Categoria alterada com sucesso.')
                
                estoque = DaoEstoque.ler()
                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, novacategoria), x.quantidade)
                      if(x.produto.categoria == antigacategoria) else(x), estoque))
                with open('estoque.txt', 'w') as arq:
                    for i in x:
                        arq.writelines(i.produto.nome + '|' +
                                       i.produto.preco + '|' +
                                       i.produto.categoria + '|' +
                                       str(i.quantidade))
                        arq.writelines('\n') 
            else:
                print('A categoria para qual deseja alterar já existe.')
        else: 
            print('A categoria que deseja alterar não existe.')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrar_categoria(self):
        categorias = DaoCategoria.ler()
        
        if len(categorias) == 0:
            print('Categorias vazias')
        else:
            for i in categorias:
                print(f'categorias: {i.categoria}')

class ControllerEstoque:
    def cadastrar_produto(self, nome, preco, categoria, quantidade):
        y = DaoCategoria.ler()
        cate = list(filter(lambda y: y.categoria == categoria, y))
        x = DaoEstoque.ler()
        esto = list(filter(lambda x: x.produto.nome == nome, x))
        
        if len(cate) > 0:
            if len(esto) == 0: 
                produto = Produtos(nome, preco, categoria)
                DaoEstoque.salvar(produto, quantidade)
                print('Produto adicionado ao estoque com sucesso.')
            else:
                print('Produto já existente nesse estoque.')
        else:
            print('Categoria inexistente.')

    def remover_produto(self, nome):
        x = DaoEstoque.ler()
        esto = list(filter(lambda x: x.produto.nome == nome, x))
        if len(esto) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    print('Produto removido.')
                    break
        else:
            print('Produto não existente no estoque.')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + '|' +
                               i.produto.preco + '|' +
                               i.produto.categoria + '|' +
                               str(i.quantidade))
                arq.writelines('\n')

    def alterar_produto(self, nomeantigo, novonome, novopreco, novacategoria, novaquantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        cate = list(filter(lambda x: x.categoria == novacategoria, y))

        if len(cate) > 0:
            esto = list(filter(lambda x: x.produto.nome == nomeantigo, x))
            if len(esto) > 0:
                esto = list(filter(lambda x: x.produto.nome == novonome, x))
                if len(esto) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novonome, novopreco, novacategoria), novaquantidade) if(x.produto.nome == nomeantigo) else(x), x))
                    print('Produto alterado com sucesso.')
                else:
                    print('O produto a ser cadastrado ja existe.')
            else:
                print('O produto que deseja alterar não existe.')

        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + '|' +
                               i.produto.preco + '|' +
                               i.produto.categoria + '|' +
                               str(i.quantidade))
                arq.writelines('\n')

    def mostrar_produto(self):
        esto = DaoEstoque.ler()
        if len(esto) == 0:
            print('Estoque vazio.')
        else:
            for i in esto:
                print('======= produto =======')
                print(f'Nome: {i.produto.nome}')
                print(f'Preço: {i.produto.preco}')
                print(f'Categoria: {i.produto.categoria}')
                print(f'Quantidade: {i.quantidade}')
                print('-------------------------')

class ControllerVenda:
    def cadastrar_venda(self, nome, vendedor, comprador, quantidade):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quant = False

        for i in x:
            if existe == False:
                if i.produto.nome == nome:
                    existe = True
                    if i.quantidade >= quantidade:
                        quant = True
                        i.quantidade = int(i.quantidade) - int(quantidade)

                        vendido = Venda(Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidade)

                        print('item add a venda.')

                        valor_comprado = int(quantidade) * int(i.produto.preco)

                        DaoVenda.salvar(vendido)
            
            temp.append([Produtos(i.produto.nome, i.produto.preco, i.produto.categoria), i.quantidade])

        arq = open('estoque.txt', 'w')
        arq.write('')

        for i in temp:
            with open('estoque.txt', 'a') as arq:
                arq.writelines(i[0].nome + '|' +
                               i[0].preco + '|' +
                               i[0].categoria + '|' +
                               str(i[1]))
                arq.writelines('\n')

        if existe == False:
            print('O produto não existe.')
            return None
        elif not quant:
            print('A quantidade vendida não contem no estoque.')
        else:
            return valor_comprado

    def relatorio_produtos(self):
        vendas = DaoVenda.ler()
        produtos = []
        for i in vendas:
            nome = i.itens_vendidos.nome
            quantidade = i.quantidade_vendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)} if (x['produto'] == nome) else(x), produtos)) 
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})
            
        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse =True)

        print("Esses sao os itens mais vendidos\n")
        
        for i in ordenado:
            print(f"produto: {i['produto']}")
            print(f"quantidade: {i['quantidade']}\n")

    def mostra_venda(self, datainicial, datafinal):
        venda = DaoVenda.ler()
        datainicial1 = datetime.strptime(datainicial, '%d/%m/%Y')
        datafinal1 = datetime.strptime(datafinal, '%d/%m/%Y')

        vendasselecionada = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= datainicial1 
                                        and datetime.strptime(x.data, '%d/%m/%Y') <= datafinal1, venda))
        total = 0
        print('==========vendas==========')
        for i in vendasselecionada:
            print(f"Nome: {i.itens_vendidos.nome}\n"
                  f"Categoria: {i.itens_vendidos.categoria}\n"
                  f"Data: {i.data}\n"
                  f"quantidade: {i.quantidade_vendida}\n"
                  f"Cliente: {i.comprador}\n"
                  f"Vendedor: {i.vendedor}\n")
            total += int(i.itens_vendidos.preco) * int(i.quantidade_vendida)
        print(f"total vendido: {total}")

class ControlleFornecedor:
    def cadastrar_fornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.cnpj == cnpj, x))
        if len(listaCnpj) > 0:
            print("Cnpj já existe.")
        elif len(listaTelefone) > 0:
            print("o teleforne já existe")
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
    
    def alterar_fornecedor(self, nomealterar, novonome, novocnpj, novotelefone, novacategoria):
        x = DaoFornecedor.ler()
        
        est = list(filter(lambda x: x.nome == nomealterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novocnpj, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(novonome, novocnpj, novotelefone, novacategoria) if(x.nome == nomealterar) else(x), x))
            else:
                print("Cnpj já existe.")
        else:
            print("O fornecedor que deseja alterar não existe.")

        with open("fornecedores.txt", "w") as arq:
            for i in x:
                arq.writelines(i.nome + '|' +
                               i.cnpj + '|' +
                               i.telefone + '|' +
                               str(i.categoria) )
                arq.writelines('\n')
            print("Fornecedor alterado com sucesso.")
        
    def remover_fornecedor(self, nome):
        x = DaoFornecedor.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("Fornecedor que deseja remover nao existe.")
            return None
        
        with open("fornecedores.txt", "w") as arq:
            for i in x:
                arq.writelines(i.nome + '|' +
                               i.cnpj + '|' +
                               i.telefone + '|' +
                               str(i.categoria) )
                arq.writelines('\n')
            print("Fornecedor removido com sucesso.")
    
    def mostrar_fornecedores(self):
        forne = DaoFornecedor.ler()
        if len(forne) == 0:
            print("lista de fornecedores vazias.")
        
        for i in forne:
            print(f"=== Fornecedor ===")
            print(f"Categoria fornecida: {i.categoria}\n"
                  f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Cnpj: {i.cnpj}" )

class ControllerClientes:
    def cadastrar_cliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()

        verif_cpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(verif_cpf) > 0:
            print("Cpf já existente.")
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print("Cliente cadastrado com sucesso.")
            else: 
                print('Digite um cpf ou telefone válido.')
        
    def alterar_cliente(self, nomealterar, novonome, novotelefone, novocpf, novoemail, novoendereco):
        x = DaoPessoa.ler()

        verif_nome = list(filter(lambda x: x.nome == nomealterar, x))
        if len(verif_nome) > 0:
            x = list(map(lambda x: Pessoa(novonome, novotelefone, novocpf, novoemail, novoendereco) if(x.nome == nomealterar) else(x), x))
        else:
            print("O cliente que deseja alterar não existe.")

        with open("clientes.txt", "w") as arq:
            for i in x:
                arq.writelines(i.nome + '|' +
                               i.telefone + '|' +
                               i.cpf + '|' +
                               i.email + '|' +
                               i.endereco)
                arq.writelines('\n')
            print("Cliente alterado com sucesso.")
    
    def remover_cliente(self, nome):
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("Cliente que deseja remover nao existe.")
            return None
        
        with open("fornecedores.txt", "w") as arq:
            for i in x:
                arq.writelines(i.nome + '|' +
                               i.telefone + '|' +
                               i.cpf + '|' +
                               i.email + '|' +
                               i.endereco)
                arq.writelines('\n')
            print("Cliente removido com sucesso.")
        
    def mostrar_clientes(self):
        clien = DaoFornecedor.ler()
        if len(clien) == 0:
            print("Lista de clientes vazias.")
        
        for i in clien:
            print(f"=== Cliente ===")
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Endereço: {i.endereco}\n"
                  f"Email: {i.email}\n"
                  f"Cpf: {i.cpf}" )
    
class ControllerFuncionarios:
    def cadastrar_funcionario(self, clt, nome, telefone, cpf, email, endereco):
        x = Daofuncionario.ler()

        verif_cpf = list(filter(lambda x: x.cpf == cpf, x))
        #verif_clt = list(filter(lambda x: x.clt == clt, x)) # pensar no uso
        if len(verif_cpf) > 0:
            print("Cpf de funcionário já cadastrado.")
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <= 11:
                Daofuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print("Funcionário cadastrado com sucesso.")
            else: 
                print('Digite um cpf ou telefone válido.')

    def alterar_funcionario(self, nomealterar, novoclt, novonome, novotelefone, novocpf, novoemail, novoendereco):
        x = Daofuncionario.ler()

        verif_nome = list(filter(lambda x: x.nome == nomealterar, x))
        if len(verif_nome) > 0:
            x = list(map(lambda x: Funcionario(novoclt, novonome, novotelefone, novocpf, novoemail, novoendereco) if(x.nome == nomealterar) else(x), x))
        else:
            print("O funcionário que deseja alterar não existe.")

        with open("funcionarios.txt", "w") as arq:
            for i in x:
                arq.writelines(i.clt + '|' +
                               i.nome + '|' +
                               i.telefone + '|' +
                               i.cpf + '|' +
                               i.email + '|' +
                               i.endereco)
                arq.writelines('\n')
            print("Funcionário alterado com sucesso.")

    def remover_funcionario(self, nome):
        x = Daofuncionario.ler()
        verif_nome = list(filter(lambda x: x.nome == nome, x))
        if len(verif_nome) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("Funcionário que deseja remover não existe.")
            return None
        
        with open("funcionarios.txt", "w") as arq:
            for i in x:
                arq.writelines(i.clt + '|' + 
                               i.nome + '|' +
                               i.telefone + '|' +
                               i.cpf + '|' +
                               i.email + '|' +
                               i.endereco)
                arq.writelines('\n')
            print("Funcionário removido com sucesso.")

    def mostrar_funcionarios(self):
        funcio = Daofuncionario.ler()
        if len(funcio) == 0:
            print("Lista de Funcionários vazias.")
        
        for i in funcio:
            print(f"=== Funcionario ===")
            print(f"Nome: {i.nome}\n"
                  f"Clt: {i.clt}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Endereço: {i.endereco}\n"
                  f"Email: {i.email}\n"
                  f"Cpf: {i.cpf}" )
        
