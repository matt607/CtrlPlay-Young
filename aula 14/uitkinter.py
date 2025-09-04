import tkinter

#criar a janela principal
janela = tkinter.Tk()
janela.title('Exemplo Tkinter')
janela.geometry('300x200')

#função chamada quando  quando o botão é clicado
def clique():
    label.config(text='Você clicou no botão!')

#criar um label
label = tkinter.Label(janela, text='Olá, Tkinter!', font=('Arial', 14))
label.pack(pady=20)

#criar um botão
botao = tkinter.Button(janela, text='Clique Aqui', command=clique)
botao.pack()

#iniciar o loop da interface
janela.mainloop()