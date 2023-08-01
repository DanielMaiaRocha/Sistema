from tkinter import * 
from tkinter import ttk

root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.screen()
        self.widgets()
        self.buttons_frame1()
        root.mainloop()
    
    def screen(self):
        self.root.title("SISTEMA SLX")
        self.root.configure(background= "#D3D3D3")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
    
    def widgets(self):
        self.frame_1 = Frame(self.root, bd= 4, bg= "white", 
                             highlightbackground="#D3D3D3", highlightthickness= 2)
        self.frame_1.place(relx= 0.02,  rely= 0.02, relwidth= 0.97, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd= 4, bg= "white", 
                             highlightbackground="#D3D3D3", highlightthickness= 2 )
        self.frame_2.place(relx= 0.02,  rely= 0.5, relwidth= 0.97, relheight= 0.46)
    
    def buttons_frame1(self):

        ### Botão busca
        self.bt_search = Button(self.frame_1, text= "Buscar", bd= 2, bg="black", fg="white"
                              , font= ('verdana', 10, 'bold'))
        self.bt_search.place(relx= 0.01, rely= 0.25, relwidth= 0.1, relheight= 0.15)    

        ###Botão limpa
        self.bt_clean = Button(self.frame_1, text= "Limpar", bd= 2, bg="black", fg="white"
                              , font= ('verdana', 10, 'bold'))
        self.bt_clean.place(relx= 0.12, rely= 0.25, relwidth= 0.1, relheight= 0.15)

        ###Botão Novo
        self.bt_new = Button(self.frame_1, text= "Novo", bd= 2, bg="black", fg="white"
                              , font= ('verdana', 10, 'bold'))
        self.bt_new.place(relx= 0.66, rely= 0.07, relwidth= 0.1, relheight= 0.15)

        ###Botão Editar
        self.bt_edit = Button(self.frame_1, text= "Editar", bd= 2, bg="black", fg="white"
                              , font= ('verdana', 10, 'bold'))
        self.bt_edit.place(relx= 0.77, rely= 0.07, relwidth= 0.1, relheight= 0.15)

        ###Botão Excluir
        self.bt_delete = Button(self.frame_1, text= "Excluir", bd= 2, bg="black", fg="white"
                              , font= ('verdana', 10, 'bold'))
        self.bt_delete.place(relx= 0.88, rely= 0.07, relwidth= 0.1, relheight= 0.15)

        ###Label Busca 
        self.lb_busca = Label(self.frame_1, text="Nome:", bg="White", fg= "black"
                                                , font= ('verdana', 10 , 'bold'))
        self.lb_busca.place(relx= 0.01, rely= 0.02)

        ###Input Busca 
        self.input_busca = Entry(self.frame_1, bg= "white", 
                             highlightbackground="black", highlightthickness= 1 , fg= "black"
                                , font= ("verdana", 10, "bold"))
        self.input_busca.place(relx= 0.01, rely= 0.1, relwidth= 0.4, relheight= 0.1)
    
    def list_frame2(self):
        self.CLIlist = ttk.Treeview(self.frame_2)
        


       

    

    


          




Application()