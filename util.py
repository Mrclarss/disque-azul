class JogoUtil:
    @staticmethod
    def exibir_opcoes(opcoes):
        for i, opcao in enumerate(opcao,1):
            print(f"{i}.{opcao}")

        @staticmethod
        def fazer_escolha(opcoes):
            while True:
                try:
                    escolha = int(input("\nEscolha uma opção: ")) - 1
                    if 0 <= escolha < len(opcoes):
                        return escolha
                    else:
                        print("Ops!...Tente novamente.")
                except ValueError: #impede que o usario quebre o codigo
                    print("Escoha inválida. Tente novamente.")

        def identidade(opcoes):
            def __init__(self):
                self.__identidade = input("Qual o seu nome? \n")

            def executar(self):
                print("Configuração do personagem")
                print(self.__identidade)
                print ("Bem vindo, {}".format(self.__identidade))
