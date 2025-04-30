from tkinter    import *
from local      import Local
import webview  # Escolhi esta biblioteca pois é fiel a html e facil de usar

# Vou implementar os valores atravez de uma interface grafica
class InterfaceGrafica:
    def __init__(self) -> None:
        pass


    # Devo ter certeza que o valor inserido seja um numero
    def validade_numero(self, P):
        # Caso user comece digitando um numero negativo a validação vai aceitar
        if P == "" or P == "-":
            return True
        try:
            # Tenta converter o valor de entrada, caso se aplica a float a validação aceita
            float(P)
            return True
        # Caso o valor de entrada seja um caractere qualquer então o valor não sera digitado
        except ValueError:
            return False


    # Este metodo é o mais importante da (classe), é aqui que fica as configurações da interface
    def Interface(self):
        janela = Tk()   # Crio aqui a janenela
        janela.title("Buscar Localização")

        # Atributo para a validade da entrada, se numero ou letra
        validade = (janela.register(self.validade_numero), '%P')

        # Para deixa a janela mais bonita e dinamica
        titulo = Label(janela, text="Digite em baixo o valor das cordenada", pady=10)
        titulo.grid(column=0,row=0)
        
        img = PhotoImage(file="imagens/lupa.png")
        imagem_dec = Label(image=img)
        imagem_dec.grid(column=2, row=5,padx=10, pady=10)

        # Para entrada da latitude
        txt_latitude = Label(janela, text="Informe aqui o valor da latitude: ")
        txt_latitude.grid(column=0, row=1)

        entrada_latitude = Entry(janela, validate="key", validatecommand=validade)
        entrada_latitude.grid(column=1,row=1, pady=10, padx=30)

        # Para entrada da longitude
        txt_longitude = Label(janela, text="Informe aqui o valor da longitude: ")
        txt_longitude.grid(column=0, row=2)

        entrada_longitude = Entry(janela, validate="key", validatecommand=validade)
        entrada_longitude.grid(column=1,row=2, pady=10)

        # Resultado
        result = ''
        saida = Label(janela, text='')
        saida.grid(column=3, row=1)
        
        
        # Resultado no mapa
        def resultado_mapa(local_img='imagens/nao_encontrado.html'):
            visual_map = webview.create_window("visual map", local_img)
            webview.start()

        
        # Para o botão
        def insere_valor():
            lat     = float(entrada_latitude.get())     #   A variavel [lat] e [long] vão coletar
            long    = float(entrada_longitude.get())    #   os valores de entrada da interface.
            local0 = Local(lat, long)                   #   A classe Local recebe seus valores aqui.
            resultado_mapa(local0.mapa())               #   Caso exista o local, map() ira retornar um arquivo HTML
            saida["text"] = local0.pesquisa()           #   Informa qual é o local ou se não existe


        enter = Button(janela, text="ENTER", command=insere_valor)
        enter.grid(column=0, row=4)

        janela.mainloop()   #Fim da janela