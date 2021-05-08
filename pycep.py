from classData import Getdata 
from tkinter import *
import os

App = Tk()

class Aplication():
    def __init__(self):
        self.App = App
        self.conf_window()
        self.conf_frames()
        self.conf_widgets()
        self.App.mainloop()

    def conf_window(self):
        self.App.title("PyCep - Consulta CEP")
        self.App.geometry("480x350+400+150")
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.App.wm_iconbitmap(self.path+'\img\icon.ico')
        self.App.minsize(width=480, height=350)
        self.App.maxsize(width=600, height=450)
        self.App.configure(background="#4f4f4f")

    def conf_frames(self):
        self.box_search = Frame(self.App, background="white", relief=SOLID, borderwidth=3)
        self.box_search.place(relx=0.15, rely=0.75, relwidth=0.60, relheight=0.15)
        self.box_button_alt = Frame(self.App, background="white", relief=RIDGE)
        self.box_button_alt.place(relx=0.25, rely=0.90, relwidth=0.30, relheight=0.05)
        self.box_action_bt = Frame(self.App, background="white", relief=RIDGE)
        self.box_action_bt.place(relx=0.56, rely=0.90, relwidth=0.15, relheight=0.05)
        self.box_bt_search = Frame(self.App, background="white", relief=SOLID, borderwidth=3)
        self.box_bt_search.place(relx=0.78, rely=0.80, relwidth=0.20, relheight=0.15)
        self.box_result = Frame(self.App, background="white", relief=FLAT, borderwidth=1)
        self.box_result.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.73)

    def conf_widgets(self):
    # ------------- CONFIGURAÇÃO DE SEGUNDO FRAME/WIDGETS DE ENDEREÇO --------------- #
        def changeAdress():
            self.box_adress_frame = Frame(self.App, background="black", relief=RIDGE)
            self.box_adress_frame.place(relx=0.02, rely=0.75, relwidth=0.75, relheight=0.15)
            self.input1_text = Label(self.box_adress_frame, text="Estado", background="black", foreground="white")
            self.input1_text.place(relx=0, rely=0, relwidth=0.17, relheight=0.40)
            self.input2_text = Label(self.box_adress_frame, text="Cidade", background="black", foreground="white")
            self.input2_text.place(relx=0.18, rely=0, relwidth=0.23, relheight=0.40)
            self.input3_text = Label(self.box_adress_frame, text="Bairro", background="black", foreground="white")
            self.input3_text.place(relx=0.42, rely=0, relwidth=0.60, relheight=0.40)

            self.input1 = Entry(self.box_adress_frame, background="white", foreground="black", borderwidth=1, font="Arial 12")
            self.input1.place(relx=0, rely=0.48, relwidth=0.17, relheight=0.60)
            self.input2 = Entry(self.box_adress_frame, background="white", foreground="black", borderwidth=1, font="Arial 12")
            self.input2.place(relx=0.18, rely=0.48, relwidth=0.23, relheight=0.60)
            self.input3 = Entry(self.box_adress_frame, background="white", foreground="black", borderwidth=1, font="Arial 12")
            self.input3.place(relx=0.42, rely=0.48, relwidth=0.60, relheight=0.60)
        
        # -------------------------- INICIO DE FUNÇÕES DE AÇÕES -------------------------- #
        def destroyframe():
            self.box_adress_frame.destroy()

        def cleanitens():
            self.result.delete('0.1', END)
            self.input_data.delete(0, END)
            self.input1.delete(0, END)
            self.input2.delete(0, END)
            self.input3.delete(0, END)

        delimitador = 45*"-"
        def verifyActive():
            try:
                if self.input_data.get() != "":
                    dados = Getdata.gettocep(self.input_data.get())
                    self.result.insert(END, dados)
                elif self.input1.get() != "" and self.input2.get() != "" and self.input3.get() != "":
                    dados = Getdata.gettoadress(self.input1.get(), self.input2.get(), self.input3.get())
                    for key in range(0, len(dados)):
                        data_dict = dados[key]
                        dataf = f"Cep: {data_dict['cep']}\nLogradouro: {data_dict['logradouro']}\nComplemento: {data_dict['complemento']}\nBairro: {data_dict['bairro']}\nLocalidade: {data_dict['localidade']}/{data_dict['uf']}\nDDD: {data_dict['ddd']}\n{delimitador}\n"
                        self.result.insert(END, dataf)
            except:
                self.result.insert(END, "ERRO, VERIFIQUE O QUE HÁ DE ERRADO!\n")
        # ------------------------------------- FIM --------------------------------------- #
        self.result = Text(self.box_result, background="black", foreground="white", font="Verdana 10 bold")
        self.result.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.scrolb = Scrollbar(self.box_result)
        self.scrolb.place(relx=0.98, rely=0, relwidth=0.02, relheight=1)
        self.result.config(yscrollcommand=self.scrolb.set)
        self.scrolb.config(command=self.result.yview)
        self.info_form = Label(self.box_search, text="Insira aqui o CEP", foreground="white",background="black", borderwidth=1)
        self.info_form.place(relx=0, rely=0, relwidth=1, relheight=0.40)
        self.input_data = Entry(self.box_search, borderwidth=1, foreground="black", font="Arial 12")
        self.input_data.place(relx=0, rely=0.40, relwidth=1, relheight=0.60)
        self.button_search = Button(self.box_bt_search, text="Buscar", relief=FLAT, background="white", foreground="black", command=verifyActive)
        self.button_search.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.button_clean = Button(self.box_action_bt, text="Clean" ,background="black", foreground="white", command=cleanitens)
        self.button_clean.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.button_cep = Button(self.box_button_alt, text="CEP", relief=SOLID, command=destroyframe)
        self.button_cep.place(relx=0, rely=0, relwidth=0.50, relheight=1)
        self.button_adress = Button(self.box_button_alt, text="ENDEREÇO", relief=SOLID, command=changeAdress)
        self.button_adress.place(relx=0.5, rely=0, relwidth=0.50, relheight=1)

Aplication()