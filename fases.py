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
    
    def executar(self):
        print("Parte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha =  JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte8()
        elif escolha == 1:
            return Parte9()
        else:
            return Parte10()
        
class Parte5(Fase):
    def __int__(self):
        self.__descricao = '''Você fala la no grupo: 
VOCÊ:  Humm galera...Eu recebi uma ligação estranha

uma pessoa com o perfil feminino de nome Liia fala:

-- OQUÊ?!?

Outra pessoa com perfil feminino de nome Maju fala:

-- E o que disseram?

VOCÊ: Me disseram um endereço
endereço: rua complexadas número 7891

LIIA:  É O NOSSO ENDEREÇO!!

VOCÊ: será que essa pessoa que me ligou queria que eu me encontrasse com vocês?

MAJU: Possível'''
        self.__opcoes = ["Ir para o endereço","Trabalhar a distância"]

    def executar(self):
        print("Parte 5")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte13()
        else:
            return Parte14()

class Parte6(Fase):
    def __int__(self):
        self.__descricao = '''Você aceita trabalhar com elas, mas ainda está um pouco desconfiado, você resolve perguntar quem são elas, não daria pra trabalhar com alguém que você nem sabe quem é.

VOCÊ: Blz, eu vou ajudar vcs, mas podem ao menos se apresentar?

CLARA: Vdd kksks, nem nos apresentamos, prazer me chamo Clara e eu sou graduada em perícia criminal

MAJU:Somos mt mal educadas kkkkkk
 Eu sou Maria Julianne, mas pode me  chamar de Maju mesmo, e eu sou doutora em matemática e curso perícia

SARICURINHA:  Pode chamar ela de Kaju tbm
Eu me chamo Sarah, e fiz curso de detetive

LIIA: basicamente somos todas detetives ccndwnv
Eu me chamo Marília, prazer

VOCÊ: Prazer em conhecê-las, eu me chamo (Digite seu nome)
Vocês moram aqui perto para que eu possa trabalhar com vocês?

CLARA: pelo o seu DDD somos do mesmo estado, nosso endereço é esse
endereço: rua complexadas número 7891'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 6")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte15()
        else:
            return Parte16()
        
class Parte7(Fase):
    def __int__(self):
        self.__descricao = '''Você realmente não quer se meter com isso, você se explica pra elas e diz que não quer participar disso e sai de novo, dessa vez elas não insistem. 
SEU JOGO ACABOU'''

    def executar(self):
        print("Parte 7")
        print(self.__descricao)

        return None
    
class Parte8(Fase):
    def __int__(self):
        self.__descricao = '''Você sai do seu carro e vai até a porta desse covil. Um silêncio ensurdecedor  paira no ambiente, parecia que o covil estava vazio. Você se aproxima?'''
        self.__opcoes = ["Se aproximar da porta","Permanecer no carro"]

    def executar(self):
        print("Parte 8")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte11()
        else:
            return Parte12()
        
class Parte9(Fase):
    def __int__(self):
        self.__descricao = '''Você abre sua mochila e lá tinha apenas suas chaves de casa, um caderno e uma caneta'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 9")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte10(Fase):
    def __int__(self):
        self.__descricao = '''Você pega seu celular e aproveita para olhar o grupo onde as meninas estavam para avisá-las  que você rebeceu uma ligação estranha com uma voz lhe dizendo um endereço'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 10")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte11(Fase):
    def __int__(self):
        self.__descricao = '''Você se aproxima da porta, e agora você tem duas opções: Bater na porta ou voltar pro carro'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 11")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte12(Fase):
    def __int__(self):
        self.__descricao = '''Você permanece no carro'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 12")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte13(Fase):
    def __int__(self):
        self.__descricao = '''Você olha seu GPS e nota que o endereço não era tão distante de onde você morava, durava em torno de uns 10 minutos para chegar lá. Assim você decidi seguir esse rumo.'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 13")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte14(Fase):
    def __int__(self):
        self.__descricao = '''Você não confia nas integrante do grupo e prefere trabalhar com ela apenas via mensagens, importando informações, com suas habilidades tecnológicas para facilitar as procura delas.
Apois falar para elas que não iria pro endereço você recebe uma mensagem no seu celular. Você olha a mensagem ou não?'''
        self.__opcoes = ["sim, olho a mensagem","não, ignoro e desligo as notificações"]

    def executar(self):
        print("Parte 14")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte15(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 15")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte16(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 16")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte17(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 17")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()     
        
class Parte18(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 18")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte19(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 19")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte21(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 21")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte22(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 22")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte23(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 23")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte24(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 24")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte25(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 25")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte26(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 26")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte27(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 27")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte28(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 28")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte29(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 29")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte30(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 30")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte31(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 31")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
              
class Parte32(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 32")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
