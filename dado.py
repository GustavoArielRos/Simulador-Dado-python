import random
import PySimpleGUI as sg


class Dados:


    # Criando a função principal

    def __init__(self):
        # self.mensagem = 'Você quer jogar o dado?[SIM/NÃO] '


        # Layout
        self.layout =[
            [sg.Text('Arremessar o dado?')],
            [sg.Button('SIM'),sg.Button('NÃO')]
        ]

    # Criando a função iniciar

    def Iniciar(self):


            # Criando uma janela
            self.janela = sg.Window('Dado virtual',layout = self.layout,size =(200,80))

            # Ler os valores da tela
            self.eventos, self.valores = self.janela.Read()

            # Usando esses valores
            try:

                if self.eventos == 'SIM' or self.eventos == 'S':
                    self.Girando_dado()




                elif self.eventos == 'NÃO' or self.eventos == 'N':
                    print('Tudo bem, agradeçemos a sua participação no jogo.')


                else:
                    print('Opção inválidade, por favor digite SIM ou NÃO.')

            except:
                print('ERRO NO PROGRAMA!')






    # Criando a função que gira o dado
    def Girando_dado(self):
        dados_numeros = []
        dados_numeros = list(range(1, 7))
        resultado = random.choice(dados_numeros)
        print(resultado)


simular = Dados()
simular.Iniciar()