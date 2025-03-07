from base import Fase
from util import JogoUtil

print("=-"*15, "ÍNICIO DO JOGO", "-="*15)

class Mochila(Fase):
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, nome, quantidade):
        if nome in self.itens:
            self.itens[nome] += quantidade
        else:
            self.itens[nome] = quantidade
        print(f"Adicionando {quantidade}x {nome} a mochila")
    def remover_item(self, nome, quantidade):
        if nome in self.itens:
            if self.itens[nome] >= quantidade:
                self.itens[nome] -= quantidade
                print(f"Removendo {quantidade}x {nome} da mochila")
                if self.itens[nome] == 0:
                    del self.itens[nome]
            else:
                print("Quantidade insufiente para remover")
        else:
            print("Item não encontrado no invetário")

    def lista_itens(self):
        if self.itens:
            print("\n Inventário vazio")
            for item, quanidade in self.itens.item():
                print(f"{item}: {quanidade}")

        else:
            print("\n Inventário")


class FaseInicial(Fase):
    def __init__(self):
        self.__descricao ='''Você acorda com seu celular lotado de notificações em um grupo com pessoas desconhecidas, quando você abre seu grupo de mensagens, há dezenas de marcações de pessoas que você nunca nem ouviu falar que estavam a te questionar quem diabos era você e por que justamente VOCÊ tinha que entrar naquele grupo. Você se pergunta o porquê de estar ali, e o que estava acontecendo; um dos membros do grupo diz que na cidade deles, cujo nome era "Kuromins" tinha um sequestrador que ultimamente anda levando muitas pessoas de lá, eles também se explicaram dizendo que todos ali são um grupo de detetives, onde cada um tem uma função, e lhe contaram que 'alguém' deu seu número a eles. Você, após ouvir o depoimento deles, recebe uma ligação estranha... O que você faz?

        '''
        self.__opcoes = ["Atende o telefone", "Desliga o telefonema e  sai do grupo", ]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha =  JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte2()
        else:
            return Parte3()
        
class Parte2(Fase):
    def __init__(self):
        self.__descricao = '''Você atente o telefone e você consegue ouvir a voz do 'Fantasma', se era assim que ele preferia ser chamado. Você nota que ele, o fantasma fala isso para tentar impedir que você sofra o mesmo destino que aquelas pessoas. Tirando as vozes abafadas das pessoas você ouve o 'Fantasma' dizendo um endereço de um cidade próxima-'''
        self.__opcoes = ["Ir para o endereço", "Mencionar no grupo"]
    
    def executar(self):
        print("Parte 2")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha =  JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte4()
        else:
            return Parte5()


class Parte3(Fase):
    def __int__(self):
        self.__descricao = '''Você digita "Mas o que diabos está acontecendo?" e sai do grupo, porém eles te colocam de novo e pedem para você dar uma chance a eles, dizendo que só você poderia ajudar eles nessa missão'''
        self.__opcoes = ["Ajudar elas","Sair mesmo assim"]

    def executar(self):
        print("Parte 3")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte6()
        else:
            return Parte7()
        
class Parte4(Fase):
    def __init__(self):
        self.__descricao = '''o endereço mencionado te leva até um covil não muito distante de onde você mora, o covil era simples por fora, tinha apenas uma porta, uma câmera e uma campainha. Você estava dentro de seu carro , com sua mochila nas costas e seu celular no bolso, o que você faz agora?'''
        self.__opcoes = ["Sair do carro","Olhar a mochila","Olhar o celular"]