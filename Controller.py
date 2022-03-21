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




a = ControllerEstoque()
a.cadastrar_produto('banana', '5', 'frutas', 20)
