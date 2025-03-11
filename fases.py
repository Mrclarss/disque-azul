 from base import Fase
from util import JogoUtil

print("=-"*15, "ÍNICIO DO JOGO", "-="*15)

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao ='''texto

        '''
        self.__opcoes = ["a", "b", "c" ]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha =  JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        elif escolha == 1:
            return Parte()
        else:
            print('''NOTÍCIAS DO WOLF
                 MANCHETE: Jovem estudante do instituto federal da Cidade Kuromins é sequestrada e até agora não temos vertígios de quem cometeu essa crueldade.
                   A família da jovem Isabela Monteiro permanece preocupada
                  
                  ''')
            return FaseInicial()
        
class Parte2(Fase):
    def __init__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a", "b", "c"]
    
    def executar(self):
        print("Parte 2")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha =  JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        elif escolha ==1:
            return Parte()
        else:
            print('''NOTÍCIAS DO WOLF
                 MANCHETE: Jovem estudante do instituto federal da Cidade Kuromins é sequestrada e até agora não temos vertígios de quem cometeu essa crueldade.
                   A família da jovem Isabela Monteiro permanece preocupada
                  
                  ''')
            return Parte2()


class Parte3(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 3")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte4(Fase):
    def __init__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b","c"]
    
    def executar(self):
        print("Parte 4")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha =  JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        elif escolha == 1:
            return Parte()
        else: 
            print('''texto''')
            return Parte4()
        
class Parte5(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 5")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()

class Parte6(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 6")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte7(Fase):
    def __int__(self):
        self.__descricao = '''texto'''

    def executar(self):
        print("Parte 7")
        print(self.__descricao)

        return None
    
class Parte8(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 8")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()
        
class Parte9(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
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
        self.__descricao = '''texto'''
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
        self.__descricao = '''texto'''
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
        self.__descricao = '''texto'''
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
        self.__descricao = '''texto'''
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
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

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
