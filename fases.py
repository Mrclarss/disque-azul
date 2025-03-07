from base import Fase
from util import JogoUtil

print("=-"*15, "ÍNICIO DO JOGO", "-="*15)

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao ='''Você acorda com seu celular lotado de notificações em um grupo com pessoas desconhecidas, quando você abre seu grupo de mensagens, há dezenas de marcações de pessoas que você nunca nem ouviu falar que estavam a te questionar quem diabos era você e por que justamente VOCÊ tinha que entrar naquele grupo. Você se pergunta o porquê de estar ali, e o que estava acontecendo; um dos membros do grupo diz que na cidade deles, cujo nome era "Kuromins" tinha um sequestrador que ultimamente anda levando muitas pessoas de lá, eles também se explicaram dizendo que todos ali são um grupo de detetives, onde cada um tem uma função, e lhe contaram que 'alguém' deu seu número a eles. Você, após ouvir o depoimento deles, recebe uma ligação estranha... O que você faz?

        '''
        self.__opcoes = ["Atende o telefone", "Desliga o telefonema e  sai do grupo"]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte2()
        else:
            return Parte3()
        
class Parte2(Fase):
    def __init(self):
        self.__descricao = '''Parte 2Você atente o telefone e você consegue ouvir a voz do 'Fantasma', se era assim que ele preferia ser chamado. Você nota que ele, o fantasma fala isso para tentar impedir que você sofra o mesmo destino que aquelas pessoas. Tirando as vozes abafadas das pessoas você ouve o 'Fantasma' dizendo um endereço de um cidade próxima-'''
        self.__opcoes = ["Ir para o endereço", "Mencionar no grupo"]
    
    def executar(self):
        print("Parte 2")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha =  JogoUtil.fazer_escolha(self.__opcoes)



class Parte3(Fase):