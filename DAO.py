from Models import *

class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines("\n")
    
    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()
        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = [] # mudar nome da lista
        for i in cls.categoria:
            cat.append(Categorias(i))

        return cat

class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itens_vendidos.nome + '|' +
                           venda.itens_vendidos.preco + '|' +
                           venda.itens_vendidos.categoria + '|' +
                           venda.vendedor + '|' +
                           venda.comprador + '|' +
                           str(venda.quantidade_vendida) + '|' +
                           venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        
        vend = [] # mudar nome da lista
        for i in cls.venda:
            vend.append(Venda(Produtos(i[0], i[1], i[2]), i[3], i[4], i[5], i[6]))
        
        return vend

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + '|' +
                           produto.preco + '|' +
                           produto.categoria + '|' +
                           str(quantidade))
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))

        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produtos(i[0], i[1], i[2]), i[3]))
        
        return est

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedores: Fornecedor):
        with open('fornecedores.txt', 'a') as arq:
            arq.writelines(fornecedores.nome + '|' +
                           fornecedores.cnpj + '|' +
                           fornecedores.telefone + '|' +
                           fornecedores.categoria)
            arq.writelines('\n')
            
    @classmethod
    def ler(cls):
        with open('fornecedores.txt', 'r') as arq:
            cls.fornecedores = arq.readlines()

        cls.fornecedores = list(map(lambda x: x.replace('\n', ''), cls.fornecedores))
        cls.fornecedores = list(map(lambda x: x.split('|'), cls.fornecedores))

        forn = []
        for i in cls.fornecedores:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        
        return forn

class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('clientes.txt', 'a') as arq:
            arq.writelines(pessoa.nome + '|' +
                           pessoa.email + '|' +
                           pessoa.telefone + '|' +
                           pessoa.cpf + '|' +
                           pessoa.endereco)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('clientes.txt', 'a') as arq:
            cls.clientes = arq.readlines()

        cls.clientes = list(map(lambda x: x.replace('\n', ''), cls.clientes))
        cls.clientes = list(map(lambda x: x.split('|'), cls.clientes))

        client = []
        for i in cls.clientes:
            client.append(Pessoa(i[0], i[1], i[2], i[3], i[4]))

        return client

class Daofuncionario:
    @classmethod
    def salvar(cls, funcionarios: Funcionario):
        with open('funcionarios.txt', 'a') as arq:
            arq.writelines(funcionarios.nome + '|' +
                           funcionarios.clt + '|' +
                           funcionarios.telefone + '|' +
                           funcionarios.email + '|' +
                           funcionarios.endereco + '|' +
                           funcionarios.cpf)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionarios.txt', 'r') as arq:
            cls.funcionarios = arq.readlines()

        cls.funcionarios = list(map(lambda x: x.replace('\n', ''), cls.funcionarios))
        cls.funcionarios = list(map(lambda x: x.split('|'), cls.funcionarios))

        funcio = []
        for i in cls.funcionarios:
            funcio.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

        return funcio
