from tkinter import *
from tkinter import ttk
import sqlite3

class Funcs():
    def clean_fields(self):
        self.input_name.delete(0, END) 
    
    def switch_to_cadastro_tab(self):
        self.page.select(self.page3)
        self.show_frame_2 = False  # Oculta o frame ao mudar para a aba "cadastro"
        self.frame_2.place_forget()  # Oculta o frame_2
    
    def switch_to_locatarios_tab(self):
        self.page.select(self.page2)
        self.show_frame_2 = True  # Mostra o frame ao voltar para a aba "Locatarios"
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.97, relheight=0.46)
    
    def db_connect(self):
        self.conn = sqlite3.connect("bancoslx.db")
        self.cursor = self.conn.cursor(); print("conectado ao banco")
    def db_disconect(self):
        self.conn.close(); print("desconectado ao banco")
    def db_create(self):
        self.db_connect()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
                            cod INTEGER PRIMARY KEY AUTOINCREMENT, 
                            nome_cliente CHAR(40) NOT NULL,
                            cpf VARCHAR(11) NOT NULL,
                            endereço CHAR(40) NOT NULL,
                            inicio_contrato VARCHAR(6) NOT NULL, 
                            aniversario_contrato VARCHAR(6) NOT NULL,
                            fim_contrato VARCHAR(6)

                                );
                            """)
        self.conn.commit()
        self.db_disconect()                    


class Application(Funcs):
    def __init__(self):
        self.root = Tk()
        self.screen()
        self.widgets()
        self.buttons_frame1()
        self.list_frame2()
        self.db_create()
        self.root.mainloop()
    
    def screen(self):
        self.root.title("SISTEMA SLX")
        self.root.configure(background="#D3D3D3")
        self.root.geometry("{0}x{1}+0+0".format(self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
        self.root.resizable(True, True)
    
    def widgets(self):
        self.frame_1 = Frame(self.root, bd=4, bg="white", 
                             highlightbackground="#D3D3D3", highlightthickness=2)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.97, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg="white", 
                             highlightbackground="#D3D3D3", highlightthickness=2)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.97, relheight=0.46)
    
    def buttons_frame1(self):
        ### Paginas e configuração
        self.page = ttk.Notebook(self.frame_1)
        self.page1 = Frame(self.page)
        self.page2 = Frame(self.page)
        self.page3 = Frame(self.page)

        self.page1.configure(background="white")
        self.page2.configure(background="white")
        self.page3.configure(background="white")

        self.page.add(self.page1, text="Inicio")
        self.page.add(self.page2, text="Locatarios")
        self.page.add(self.page3, text="cadastro")
        
        self.page.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)
         
        ### Botões Pagina de Locatarios
       
        ### Botão Busca
        self.bt_search = Button(self.page2, text="Buscar", bd=2, bg="black", fg="white",
                                font=('verdana', 10, 'bold'))
        self.bt_search.place(relx=0.01, rely=0.25, relwidth=0.1, relheight=0.15)    
        
        ### Botão Limpar
        self.bt_clean = Button(self.page2, text="Limpar", bd=2, bg="black", fg="white",
                               font=('verdana', 10, 'bold'), command=self.clean_fields)
        self.bt_clean.place(relx=0.12, rely=0.25, relwidth=0.1, relheight=0.15)

        ### Botão Novo
        self.bt_new = Button(self.page2, text="Novo", bd=2, bg="black", fg="white",
                             font=('verdana', 10, 'bold'), command=self.switch_to_cadastro_tab)
        self.bt_new.place(relx=0.66, rely=0.07, relwidth=0.1, relheight=0.15)

        ### Botão Editar
        self.bt_edit = Button(self.page2, text="Editar", bd=2, bg="black", fg="white",
                              font=('verdana', 10, 'bold'))
        self.bt_edit.place(relx=0.77, rely=0.07, relwidth=0.1, relheight=0.15)
        
        ### Botão Excluir
        self.bt_delete = Button(self.page2, text="Excluir", bd=2, bg="black", fg="white",
                                font=('verdana', 10, 'bold'))
        self.bt_delete.place(relx=0.88, rely=0.07, relwidth=0.1, relheight=0.15)

        ### Botão Nome
        self.lb_busca = Label(self.page2, text="Nome:", bg="White", fg="black",
                                                font=('verdana', 10, 'bold'))
        self.lb_busca.place(relx=0.01, rely=0.02)

        ### Barra de Digitação 
        self.input_name = Entry(self.page2, bg="white", 
                             highlightbackground="black", highlightthickness=1, fg="black",
                             font=("verdana", 10, "bold"))
        self.input_name.place(relx=0.01, rely=0.1, relwidth=0.4, relheight=0.09)
        
        ### Pagina Cadastro 
    
        ### Botão Salvar Cadastro   
        self.bt_save = Button(self.page3, text="Salvar", bd=2, bg="black", fg="white",
                                font=('verdana', 10, 'bold'))
        self.bt_save.place(relx=0.82, rely=0.87, relwidth=0.08, relheight=0.12)
        
        ### Botão Limpar Cadastro
        self.bt_clean = Button(self.page3, text="Limpar", bd=2, bg="black", fg="white",
                               font=('verdana', 10, 'bold'), command=self.clean_fields)
        self.bt_clean.place(relx=0.92, rely=0.87, relwidth=0.08, relheight=0.12)

        self.lb_busca = Label(self.page3, text="Nome:", bg="White", fg="black",
                                                font=('verdana', 10, 'bold'))
        self.lb_busca.place(relx=0.01, rely=0.02)

        self.input_name = Entry(self.page3, bg="white", 
                             highlightbackground="black", highlightthickness=1, fg="black",
                             font=("verdana", 10, "bold"))
        self.input_name.place(relx=0.01, rely=0.1, relwidth=0.25, relheight=0.09)

        self.lb_address = Label(self.page3, text="Endereço:", bg="White", fg="black",
                                font=('verdana', 10, 'bold'))
        self.lb_address.place(relx=0.01, rely=0.2)

        self.input_address = Entry(self.page3, bg="white", 
                             highlightbackground="black", highlightthickness=1, fg="black",
                             font=("verdana", 10, "bold"))
        self.input_address.place(relx=0.01, rely=0.28, relwidth=0.4, relheight=0.09)

        self.lb_address = Label(self.page3, text="Endereço:", bg="White", fg="black",
                                font=('verdana', 10, 'bold'))
        self.lb_address.place(relx=0.01, rely=0.2)

        self.input_address = Entry(self.page3, bg="white", 
                             highlightbackground="black", highlightthickness=1, fg="black",
                             font=("verdana", 10, "bold"))
        self.input_address.place(relx=0.01, rely=0.48, relwidth=0.15, relheight=0.09)

        self.lb_address = Label(self.page3, text="CPF:", bg="White", fg="black",
                                font=('verdana', 10, 'bold'))
        self.lb_address.place(relx=0.01, rely=0.4)

        self.input_address = Entry(self.page3, bg="white", 
                             highlightbackground="black", highlightthickness=1, fg="black",
                             font=("verdana", 10, "bold"))
        self.input_address.place(relx=0.01, rely=0.68, relwidth=0.15, relheight=0.09)
        

    
    def list_frame2(self):
        self.show_frame_2 = True
        self.CLIlist = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8"))
        self.CLIlist.heading("#0", text="")
        self.CLIlist.heading("#1", text="Codigo")
        self.CLIlist.heading("#2", text="Nome")
        self.CLIlist.heading("#3", text="Endereço")
        self.CLIlist.heading("#4", text="CPF")          
        self.CLIlist.heading("#5", text="Inicio")
        self.CLIlist.heading("#6", text="Aniversário")
        self.CLIlist.heading("#7", text="Fim")

        self.CLIlist.column("#0", width=1)
        self.CLIlist.column("#1", width=50)
        self.CLIlist.column("#2", width=250)
        self.CLIlist.column("#3", width=450)
        self.CLIlist.column("#4", width=180)
        self.CLIlist.column("#5", width=100)
        self.CLIlist.column("#6", width=100)
        self.CLIlist.column("#7", width=100)
        
        self.CLIlist.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.85)

        self.scrool_list = Scrollbar(self.frame_2, orient="vertical")
        self.CLIlist.configure(yscroll=self.scrool_list.set)
        self.scrool_list.place(relx=0.96, rely=0.01, relwidth=0.02, relheight=0.85)

        
        self.page3.bind("<<NotebookTabChanged>>", lambda event: self.switch_to_locatarios_tab())

Application()   