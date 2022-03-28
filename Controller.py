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

    def alterar_categoria(self, antigacategoria, novacategoria):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == antigacategoria, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == novacategoria, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categorias(novacategoria) if(x.categoria == antigacategoria) else(x), x))
                print('Categoria alterada.')
            else:
                print('A categoria para qual deseja alterar já existe.')
        else: 
            print('A categoria que deseja alterar não existe.')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrar_cateforia(self):
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

a = ControllerVenda()
a.cadastrar_venda("banana", 'joao', 'caio', 10)
#a.alterar_produto('banana', 'maca', '7', 'frutas', '20')
