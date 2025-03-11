from base import Fase
from util import JogoUtil

print("=-"*15, "ÍNICIO DO JOGO", "-="*15)

class FaseInicial(Fase):
    def __init__(self):
        self.__descricao ='''Você acorda com seu celular lotado de notificações em um grupo que haviam te adicionado com pessoas desconhecidas. Quando você abre o grupo, você foi marcado diversas vezes, por pessoas que você nunca nem ouviu falar e que estavam a te questionar quem diabos é você e por que justamente VOCÊ tinha que entrar naquele grupo. Você se pergunta o porquê de ter sido adicionado ali e o que estava acontecendo. Um dos membros do grupo diz que na cidade deles, de nome "Kuromins", tinha um sequestrador que ultimamente andava levando muitas pessoas de lá, eles também se explicaram que todos ali são detetives, e que nesse grupo cada um tem uma função, além disso lhe contaram que 'alguém' deu seu número a eles.
Você, após ouvir o depoimento deles, recebe uma ligação estranha... O que você faz?'''
        self.__opcoes = ["Atende o telefone", "Desliga o telefonema e  sai do grupo", "Olhar o celular" ]

    def executar(self):
        print("\nFase Inicial")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha =  JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte2()
        elif escolha == 1:
            return Parte3()
        else:
            print('''NOTÍCIAS DO WOLF MANCHETE: Jovem estudante do instituto federal da Cidade Kuromins é sequestrada e até agora não temos vertígios de quem cometeu essa crueldade.
                A família da jovem Isabela Monteiro permanece preocupada



                GALERIA DE FOTOS você não tem fotos registradas

 

                TELEFONE Nenhuma chamada registrada''')
            return FaseInicial()
        
class Parte2(Fase):
    def __init__(self):
        self.__descricao = '''Você atende o telefone e ouve a voz de um tal 'Fantasma'. Você nota que ele fala isso para tentar impedir você de sofrer o mesmo destino que aquelas pessoas. Além das vozes abafadas, você ouve o 'Fantasma' dizendo o endereço de uma cidade próxima.
            Após o ocorrido, o que você decide?'''
        self.__opcoes = ["Ir para o endereço", "Mencionar no grupo", "Olhar o celular"]
    
    def executar(self):
        print("Parte 2")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha =  JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte4()
        elif escolha ==1:
            return Parte5()
        else:
            print('''NOTÍCIAS DO WOLF
                 MANCHETE: Jovem estudante do instituto federal da Cidade Kuromins é sequestrada e até agora não temos vertígios de quem cometeu essa crueldade.
                   A família da jovem Isabela Monteiro permanece preocupada
                  
                  
                  GALERIA DE FOTOS
                  você não tem fotos registradas
                  
                 
                  TELEFONE
                  Uma chamada registrada com o número 33 9123-333''')
            return Parte2()


class Parte3(Fase):
    def __int__(self):
        self.__descricao = '''Você digita "Mas o que diabos está acontecendo?" e sai do grupo, porém eles te colocam de novo e pedem para você dar uma chance a eles, dizendo que só você poderia ajudar eles nessa missão'''
        self.__opcoes = ["Ajudar elas","Sair mesmo assim"]

    def executar(self):
        print("Parte 3")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha =  JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte6()
        else:
            return Parte7()
        
class Parte4(Fase):
    def __init__(self):
        self.__descricao = '''O endereço mencionado te leva até um covil não muito distante de onde você mora, o covil era simples por fora, tinha apenas uma porta, uma câmera e uma campainha. Você estava dentro de seu carro , com sua mochila nas costas e seu celular no bolso, o que você faz agora?'''
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
            VOCÊ: gente...eu recebi uma ligação estranha

            uma pessoa com o perfil feminino de nome Liia fala:
            -- OQUÊ?!?

            Outra pessoa com perfil feminino de nome Maju fala:
            -- E o que disseram?

            VOCÊ: me disseram um endereço
            endereço: rua complexadas número 7891

            LIIA: É O NOSSO ENDEREÇO!!

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

            VOCÊ: blz, eu vou ajudar vcs, mas podem ao menos se apresentar?

            CLARA: Vdd kksks, nem nos apresentamos, prazer me chamo Clara e eu sou graduada em perícia criminal

            MAJU: Somos mt mal educadas kkkkkk
            Eu sou Maria Julianne, mas pode me chamar de Maju mesmo, e eu sou doutora em matemática e curso perícia

            SARICURINHA: chame ela de kaju q é mais fácil
            meu nome é sarah e eu fiz curso de detetive

            LIIA: Basicamente somos todas detetives idghyeashe
            Eu me chamo Marília, prazer

            VOCÊ: Prazer em conhecê-las, eu me chamo (Digite seu nome)
            Vocês moram aqui perto para que eu possa trabalhar com vocês?

            CLARA: pelo o seu DDD somos do mesmo estado, nosso endereço é esse
            endereço: rua complexadas número 7891'''
        self.__opcoes = ["Trabalhar a distância","Ir para o endereço"]

    def executar(self):
        print("Parte 6")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte14()
        else:
            return Parte4()
        
class Parte7(Fase):
    def __int__(self):
        self.__descricao = '''Você realmente não quer se meter com isso, você se explica pra elas e diz que não quer participar disso e sai de novo, dessa vez elas não insistem.'''

    def executar(self):
        print("Parte 7")
        print(self.__descricao)

        return None
    
class Parte8(Fase):
    def __int__(self):
        self.__descricao = '''Você sai do seu carro e vai até a porta desse covil. Um silêncio ensurdecedor paira no ambiente, parecia que o covil estava vazio. Você se aproxima?'''
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
        self.__descricao = '''Você abre sua mochila e lá tinha apenas suas chaves de casa, um caderno, uma caneta e um notebook'''

    def executar(self):
        print("Parte 9")
        print(self.__descricao)

        return Parte4()

        
class Parte10(Fase):
    def __int__(self):
        self.__descricao = '''Você pega seu celular e aproveita para olhar o grupo onde as meninas estavam para avisá-las  que você rebeceu uma ligação estranha com uma voz lhe dizendo um endereço'''

    def executar(self):
        print("Parte 10")
        print(self.__descricao)

        return Parte5()
        
class Parte11(Fase):
    def __int__(self):
        self.__descricao = '''Você se aproxima da porta, e agora você tem duas opções: Bater na porta ou voltar pro carro'''
        self.__opcoes = ["Bater na porta","Voltar pro carro"]

    def executar(self):
        print("Parte 11")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte17()
        else:
            return Parte54()
        
class Parte12(Fase):
    def __int__(self):
        self.__descricao = '''Você permanece no carro'''
        self.__opcoes = ["Comentar o ocorrido no grupo e permanecer no carro","Ir investigar o vulto"]

    def executar(self):
        print("Parte 12")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte47()
        else:
            return Parte46()
        
class Parte13(Fase):
    def __int__(self):
        self.__descricao = '''Você olha seu GPS e nota que o endereço não era tão distante de onde você morava, durava em torno de uns 10 minutos para chegar lá. Assim você decidi seguir esse rumo.'''

    def executar(self):
        print("Parte 13")
        print(self.__descricao)

        return Parte4()
        
class Parte14(Fase):
    def __int__(self):
        self.__descricao = '''Você não confia nas integrante do grupo e prefere trabalhar com ela apenas via mensagens, importando informações, com suas habilidades tecnológicas para facilitar a procura delas.
            Após falar para elas que não iria pro endereço você recebe uma mensagem no seu celular. Você olha a mensagem ou não?'''
        self.__opcoes = ["Sim, olho a mensagem","Não, ignoro e bloqueio o contato"]

    def executar(self):
        print("Parte 14")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte35()
        else:
            return Parte36()
        

class Parte17(Fase):
    def __int__(self):
        self.__descricao = '''Você bate na porta'''

    def executar(self):
        print("Parte 17")
        print(self.__descricao)

        return Parte18()     
        
class Parte18(Fase):
    def __int__(self):
        self.__descricao = '''Escuta um barulhão de alguma coisa caindo'''

    def executar(self):
        print("Parte 18")
        print(self.__descricao)

        return Parte18()
        
class Parte19(Fase):
    def __int__(self):
        self.__descricao = '''VOZ 1: QUE ODIO, NOSSA PROVA!!

VOZ 2: Calmaa! nem quebrou muito'''
        self.__opcoes = ["Bater na porta","Ouvir a conversa"]

    def executar(self):
        print("Parte 19")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte20()
        else:
            return Parte21()

class Parte20(Fase):
    def __int__(self):
        self.__descricao = '''Você bate novamente na porta, dessa vez uma jovem de cabelos compridos te recepciona.

Maju: Olá? quem é você?

Você: eu sou  (digite seu nome), uma pessoa me ligou me dizendo para vim para esse endereço

Maju: estranho... me siga'''
        self.__opcoes = ["Seguir ela","Ficar ali mesmo"]

    def executar(self):
        print("Parte 20")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte22()
        else:
            return Parte23()

class Parte21(Fase):
    def __int__(self):
        self.__descricao = '''Você fica com o ouvido na porta escutando tudo

VOZ 3: Ei, vocês escutaram algo??

VOZ 2: Só se for  o barulho que Clara fez

VOZ 1: FOI SEM QUERER'''

    def executar(self):
        print("Parte 21")
        print(self.__descricao)

        return Parte20()
              
class Parte22(Fase):
    def __int__(self):
        self.__descricao = ''' Você segue ela até uma salinha onde tinham mais quatro meninas com um semblante de preocupação.
Você de primeira percebe que as garotas são detetives, pelo o quadro cheio de fotos emarcações e papeis por todos os lados, você presume isso por fazer  a mesma coisa em seu trabalho.
Você então decide falar com elas, você fala que quer trabalhar com elas apenas ou conta que está ali pois uma voz misteriosa te ligou?'''
        self.__opcoes = ["Falar que quer trabalhar com elas","Contar que uma voz misteriosa ligou"]

    def executar(self):
        print("Parte 22")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte27()
        else:
            return Parte28()
              
class Parte23(Fase):
    def __int__(self):
        self.__descricao = '''Foi inútil isso, você ficar ai parado não vai adiantar nada.
OPS...
Você sente que tem alguém te observando, o  que você faz. Segue a garota ate dentro de casa ou vai até onde você acha que tem alguma pessoa ou você so fica parado ali?'''
        self.__opcoes = ["Ir com ela","Vai até onde você acha que tem uma pessoa","Fica parado ali"]

    def executar(self):
        print("Parte 23")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte22()
        elif escolha == 1:
            return Parte24()
        else:
            return Parte26()
              
class Parte24(Fase):
    def __int__(self):
        self.__descricao = '''Você foi até a pessoa?
Lamento em te informar, mas naquele arbusto algo terrível te esperava, ele era poderoso, tinha consigo um machado de lenhador, ao mesmo momento em que você se aproxima ele crava o machado em você mas... por quê?'''

    def executar(self):
        print("Parte 24")
        print(self.__descricao)

        return Parte25()
              
class Parte25(Fase):
    def __int__(self):
        self.__descricao = '''Parece que não foi so você que que recebeu uma mensagem de um tal de 'Fantasma', o famoso Lobisomem já sabia que você viria para aqui, era tudo esquematiza. Agora você morre na dúvida se deveria mesmo ter confiado no tal 'Fantasma' ou se ele queria te ajudar e alguma das meninas do grupo teria descorberto que você viria mais cedo ou mais tarde. Mas enfim, você não tem mais tempo de pensar, agora é só esperar o seu destino.
VOCÊ MORREU! '''

    def executar(self):
        print("Parte 25")
        print(self.__descricao)

        return None
              
class Parte26(Fase):
    def __int__(self):
        self.__descricao = '''Sério? Você não vai ficar salvo ai, sai logo! RÁPIDO! Antes que...

Você não teve nem tempo de raciocinar, só nota que um machado de longe bem no meio do seu rosto, você já não tem mais esperança... Mas espera aí, você ainda está respirando, você sente alguém te puxando, mas pra onde? Quem está te puxando?
Sua missão acaba aqui não tem como você fazer mais ações
VOCÊ MORREU?'''

    def executar(self):
        print("Parte 26")
        print(self.__descricao)

        return None
              
class Parte27(Fase):
    def __int__(self):
        self.__descricao = '''Talvez elas pudessem ajudar em alguma coisa, mas se você prefere trabalhar sozinho, vamos prosseguir'''

    def executar(self):
        print("Parte 27")
        print(self.__descricao)

        return Parte29()
              
class Parte28(Fase):
    def __int__(self):
        self.__descricao = '''Elas perguntaram qual era o número que te ligou falando isso, você quer olhar seu celular para ter certeza?'''
        self.__opcoes = ["Olhar o celular","Não dizer o número de telefone"]

    def executar(self):
        print("Parte 28")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte31()
        else:
            return Parte45()
              
class Parte29(Fase):
    def __int__(self):
        self.__descricao = '''Sarah: Trabalhar com a gente?

Maju: esquisito...

Liia: O que te faz querer trabalhar com a gente?

Você: Eu tenho meus motivos

Clara: Olha, você até pode.. mas a gente ja tem uma missão bem complicada

Você: eu sei, o notíciario posta muita coisa sobre vocês, aparentemente você são bem famosas

Clara: Já falamos para não colocarem tantas informações, esse assasino sequestrador podem ter acesso a internet.

Sarah: No meio da floresta? A gente tinha descoberto que ele esconde as vítimas na floresta

Maju: Oh, se for trabalhar com a gente vai precisar disso

(é um distintivo da perícia, adicionado no inventário)

Você: Ok... Então quer dizer que esse monstrinho se esconde na floresta?

Liia: E o mais engraçado é que ele se fantasia de lobo.

Você: Muito interessante, então ele gosta de uma fantasia

Deseja anotar em seu caderno?'''
        self.__opcoes = ["Ir para a floresta","Fazer anotações","Continuar conversando"]

    def executar(self):
        print("Parte 29")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte44()
        elif escolha == 1:
            return Parte30()
        else:
            return Parte31()
              
class Parte30(Fase):
    def __int__(self):
        self.__descricao = '''Você abre seu inventario e pega  seu caderninho de anotações'''

    def executar(self):
        print("Parte 30")
        print(self.__descricao)
        inventario = ["Caderno", "caneta", "Chaves de casa", "Notebook"]
        print(f"Na sua mochila tem {inventario}")

        return Parte32()
              
class Parte31(Fase):
    def __int__(self):
        self.__descricao = '''Apenas continua a conversa'''

    def executar(self):
        
        print("Parte 31")
        print(self.__descricao)

        return Parte32()
              
class Parte32(Fase):
    def __int__(self):
        self.__descricao = '''Liia: ontem anoite eu fui conversar  com um amigo meu que também era amigo de uma das vítimas e ele disse que a última vez que ele viu  a Isabela foi em uma festa, ela estava bem bebadâ, e deu isso aqui pra ele.

( ela mostra um colar com a incial M)

Você: Uma inicial M? Bom eu tenho algumas suspeitas, ou é do sobrenome dela, ou é alguém que a presenteou, qual o nome do seu amigo?

Liia: Não tem nada aver, é João Carvalho

Você: Eu pesquisar mais um pouco sobre, pode me emprestar o colar para eu analisar melhor?

Liia: Okok

(item adicionado na mochila)

Clara: Eu vou atrás para saber por que ele se fantasia de lobo e o que tem de tão interessante nessa floresta

Sarah: Essa floresta desde sempre foi meio assombrada assim, e ela é escura e tem muitos lugares pra esconder, talvez seja por isso o lugar escolhido pelo o Lobo

Clara: Pode ser

Você: Eu vou pra um lugar mais calmo pra usar meu notebook'''

    def executar(self):
        print("Parte 32")
        print(self.__descricao)

        return Parte33()
              
class Parte33(Fase):
    def __int__(self):
        self.__descricao = '''Você vai para um canto mais calmo e abre seu notebook, lá você encontra algumas coisas úteis sobre o colar.

            Você achou em uma notícia de 10 anos atrás, em um acidente de carro de uma jovem chamada Manoela Medeiros e que tinha uma foto dela, dando um zoom e ajeitando a foto, você consegue ver o mesmo colar no pescoço dela.
            Sua hipótese é que a Isabela estava na cena do crime, e possivelmente pegou o colar.'''

    def executar(self):
        print("Parte 33")
        print(self.__descricao)

        return Parte34()
                          
class Parte34(Fase):
    def __int__(self):
        self.__descricao = '''Você recebe uma mensagem anônima'''

    def executar(self):
        print("Parte 34")
        print(self.__descricao)

        return Parte14()
                          
class Parte35(Fase):
    def __int__(self):
        self.__descricao = '''Ao receber a mensagem você nota que foi de uma pessoa não salva no celular, você também percebe que tem o mesmo número da pessoa que te ligou mais cedo, mas aparece sem nome e sem descrição, como se fosse uma conta a anônima.
            Você responde a mensagem ou bloqueia?'''
        self.__opcoes = ["Responde","Bloqueia"]

    def executar(self):
        print("Parte 35")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte37()
        else:
            return Parte36()
                          
class Parte36(Fase):
    def __int__(self):
        self.__descricao = '''Após bloquear o contato, o seu celular dá uma tela preta com a seguinte mensagem: 
            VOCÊ NÃO DEVERIA TER ME BLOQUEADO'''
        self.__opcoes = ["Desbloqueio o contato","Ignoro e deixo o contato bloqueado"]

    def executar(self):
        print("Parte 36")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte38()
        else:
            return Parte40()
                                      
class Parte37(Fase):
    def __int__(self):
        self.__descricao = '''De supresa ele já afirma para confiar nele e te mostra uma foto, uma foto que parecia ser uma carta, mas estava toda criptugrafadas'''

    def executar(self):
        print("Parte 37")
        print(self.__descricao)
        inventario.append('foto')

        return Parte38()
                                      
class Parte38(Fase):
    def __int__(self):
        self.__descricao = '''Ótimo, você desbloqueia ele  e o mesmo manda a mesma mensagem de mais cedo.
            No chat:

            VOCÊ: blz, o que você quer?

            'Fantasma': Eu vou ajudar você nesse caso.

            VOCÊ: Que caso?

            'Fantasma: O que você recebeu agora pouco

            VOCÊ: e o que faz eu confiar em você??

            'Fantasma': Porque eu confio em você.

            VOCÊ: haha, ta bom então
            quais são seus planos?

            'Fantasma': Boa, falou minha língua'''
        self.__opcoes = ["Você descriptografou","Ela descriptografou"]

    def executar(self):
        print("Parte 38")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte39()
        else:
            return Parte39()
                                             
class Parte39(Fase):
    def __int__(self):
        self.__descricao = '''Indepentende de quem foi que descriptografou ambos chegaram ao mesmo resultado, tinha algo escrito assim:

            " Neste território só há espaço para a alcatéia"

            'Fantasma': é inútil.

            Você: Por que? eu acho que pode ser uma grande dica

            'Fantasma': Isso é brincadeira de criança

            Você: falou o cara que tem o nome de fantasma

            'Fantasma': eu tenho motivos pra isso.
            Bom agora vou procurar mais pistas

            Você: vai lá, adeus!'''
        self.__opcoes = ["a","b","c"]

    def executar(self):
        print("Parte 39")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        elif escolha == 1:
            return Parte()
        else:
            return Parte()
                                                  
class Parte40(Fase):
    def __int__(self):
        self.__descricao = '''Você não consegue seguir em frente com a missão, pela primeira vez em sua vida você falhou, você viu, aos poucos cada uma de suas amigas serem pegas, e no final aquela que você mais confiava era uma traidora, era e sem coração acabou com a vida de todas as outras, e você só podia olhar para isso sem poder fazer nada para impedir.
            FIM'''

    def executar(self):
        print("Parte 40")
        print(self.__descricao)

        return None 
                                                              
class Parte41(Fase):
    def __int__(self):
        self.__descricao = '''Você: Antes de você ir embora

            Fantasma: ??

            Você: Eu estava pesquisando sobre uma pista que eu encontrei, de um colar.

            O que eu achei foi um acidente que aconteceu a 10 anos de uma jovem chamada Manoela Medeiros, o que eu acho mais estranho é por que isso estaria com a Isabela

            Fantasma: wow
            Você é bem bom nisso

            Sobre isso, é muito estranho, mas já pensou que talvez ela estivesse lá também.

            Você: eu pensei isso...
            Mas por que ela estaria lá

            Fantasma: Talvez elas se conheciam ou..

            Você: Quem cometeu esse acidente foi a Isabela

            Fantasma: Mas ela tinha extamente 10 anos a 10 anos atrás, como que ela fez isso?
            Eu vou procurar mais coisas, mas enquanto isso, mostra esse texto para as meninas'''

    def executar(self):
        print("Parte 41")
        print(self.__descricao)

        return Parte43() 
                                                                          
class Parte42(Fase):
    def __int__(self):
        self.__descricao = '''O fantasma te manda mensagem denovo

Fantasma:
Achei um texto interessante sobre a  Isabela, depois você mostra as informações que conseguimos sobre ela pras meninas'''

    def executar(self):
        print("Parte 42")
        print(self.__descricao)

        return Parte43() 
                                                                                      
class Parte43(Fase):
    def __int__(self):
        self.__descricao = ''' "Às vezes, a escuridão parece ter vida própria. É como se cada sombra estivesse esperando por um momento de fraqueza, pronta para se mover e sussurrar segredos que não deveriam ser ouvidos. Eu sempre pensei que o medo era apenas uma emoção, mas agora percebo que ele pode se tornar uma presença, algo que nos observa, nos segue. E quando a noite cai, e o silêncio se instala, é nesse vazio que as dúvidas começam a crescer. O que realmente está escondido nas sombras? E, mais importante, quem ou o que está esperando para ser descoberto?"

O que isso significaria?'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 43")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte() 
                                                                                      
class Parte44(Fase):
    def __int__(self):
        self.__descricao = '''Você dá a ideia de ir logo para a floresta e ir enfrentar o LOBO, as meninas não topam então você vai sozinho para a floresta e lá você encontra o ele, com um machado nas mãos. O maníaco agora não terá piedade, enquanto você corre ele joga o machado em você acertando suas costas e te rasgando ao meio.
Esse foi seu final trágico'''

    def executar(self):
        print("Parte 44")
        print(self.__descricao)

        return None 
                                                                                      
class Parte45(Fase):
    def __int__(self):
        self.__descricao = '''Você: Não vou dizer o número

Sarah: É, ai tu te vira sozinho então, a gente tenta te ajudar, se esse número for o Lobo espero que ele te encontre e te coma vivo, sem noção'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 45")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte() 
            
class Parte46(Fase):
    def __int__(self):
        self.__descricao = '''Você esconde as coisas importantes dentro do carro, pega o celular, um canivete que estava no porta luvas e a mochila, fecha as portas e vai até a esquina.
Chegando lá você percebe que o vulto já tinha ido embora e tinha deixado uma boneca de pano da rainha de copas.'''
        self.__opcoes = ["Mandar foto no grupo","Você pega a boneca"]

    def executar(self):
        print("Parte 46")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte49()
        else:
            return Parte48()

class Parte47(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 47")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()

class Parte48(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 48")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()

class Parte49(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 49")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()

class Parte50(Fase):
    def __int__(self):
        self.__descricao = '''texto'''
        self.__opcoes = ["a","b"]

    def executar(self):
        print("Parte 50")
        print(self.__descricao)
        JogoUtil.exibir_opcoes(self.__opcoes)
        escolha = JogoUtil.fazer_escolha(self.__opcoes)

        if escolha == 0:
            return Parte()
        else:
            return Parte()