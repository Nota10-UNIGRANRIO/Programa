import tkinter as tk
from tkinter import messagebox
from tkinter import *
import json
import tkinter as image
import tkinter .ttk 
from tkinter import filedialog
from tkinter import ttk


class Livro:
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        
        self.livros = {}
    
    def to_dict(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'ano': self.ano,
            'genero': self.genero
        }

    def to_dict(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'ano': self.ano,
            'genero': self.genero
        }

    # métodos que afetam a classe como um todo e não dependem de instâncias específicas da classe. 
    @classmethod
    def from_dict(cls, dados):
        return cls(**dados)
    
class Biblioteca:
    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def consultar_livro(self, titulo):
        if titulo in self.livros:
            return self.livros[titulo]
        else:
            return None

    def listar_livros_por_autor(self, autor):
        livros_autor = [livro for livro in self.livros.values() if livro.autor == autor]
        return livros_autor

    def listar_livros_por_genero(self, genero):
        livros_genero = [livro for livro in self.livros.values() if livro.genero == genero]
        return livros_genero

    
    def to_json(self):
        return {titulo: livro.to_dict() for titulo, livro in self.livros.items()}

    def from_json(self, livro_dict):
        self.livros = {titulo: Livro.from_dict(dados) for titulo, dados in livro_dict.items()}

#--------------------------Pop up---------------------------------------------------------------------------------------------------------
class InformacoesLivroPopup:
    def __init__(self, parent, livro):
        self.parent = parent
        self.livro = livro

        # Crie uma nova janela Toplevel para as informações do livro
        self.popup = tk.Toplevel(parent)
        self.popup.title("Informações do Livro")
        
        frameCima = Frame(root, width=770, height=50, relief="flat")
        frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)
    

        # Adicione uma Treeview para exibir as informações do livro em formato de tabela
        self.tree = ttk.Treeview(self.popup, columns=("Título", "Autor", "Ano", "Gênero"), show="headings")
        self.tree.grid(row=0, column=0, columnspan=3, padx=5, pady=10, sticky="NSEW")


        # Adicione algum espaçamento entre as células da grade
        self.popup.grid_columnconfigure(0, weight=1)
        self.popup.grid_rowconfigure(0, weight=1)

        # Adicione os dados ao Treeview
        self.adicionar_dados_treeview()
        
        # Configure as dimensões da janela
        self.popup.minsize(600, 100)  # Largura x Altura
        self.popup.geometry("900x50")  # Largura x Altura

        # Centralize a janela na tela
        self.centralizar_janela()

        # Adicione algum espaçamento entre as células da grade
        self.popup.grid_columnconfigure(0, weight=1)
        self.popup.grid_rowconfigure(0, weight=1)

        # Adicione os dados ao Treeview
        self.adicionar_dados_treeview()

        
        # Adicione um rótulo para exibir as informações
        mensagem = f"Informações do Livro:\n\nTítulo: {livro.titulo}\nAutor: {livro.autor}\nAno: {livro.ano}\nGênero: {livro.genero}"
        label = tk.Label(self.popup, text=mensagem, padx=10, pady=10)
        titulo_label = tk.grid(row=1, column=0, padx=5, pady=10, sticky="NSEW")
        livro = self.biblioteca.consultar_livro
        
              
        label.pack()

    def adicionar_dados_treeview(self):
        # Adicione as colunas ao Treeview
        self.tree.heading('Título', text='Título')
        self.tree.heading('Autor', text='Autor')
        self.tree.heading('Ano', text='Ano')
        self.tree.heading('Gênero', text='Gênero')

        # Adicione os dados ao Treeview em colunas
        self.tree.insert("", "end", values=(self.livro.titulo, self.livro.autor, self.livro.ano, self.livro.genero))

        

        
#-----------------------------------------------GERENCIADOR DO LAYOUT E POSIÇÃO-----------------------------------------------------------
class BibliotecaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Biblioteca")

        self.biblioteca = Biblioteca()
  
        
        #Cores do programa --------------------------------
        co1 = "#000000"
        co2 = "#F8F8FF"
        co3 = "#F8F8FF"
        co4 = "#e06636"
        co5 = "#263238"
        co6 = "#00BFFF"
        co7 = "#403d3d"

        #Frames--------------------------------------------
        
        frameCima = Frame(root, width=770, height=50, bg=co6, relief="flat")
        frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)
        
        frameEsquerda = Frame(root, width=100, height=100, bg=co1, relief="solid")
        frameEsquerda.grid(row=1, column=0, sticky=NSEW)
        
        frameDireita = Frame(root, width=600, height=265, bg=co2, relief="raised")
        frameDireita.grid (row=1, column=1, sticky=NSEW)

        
        # Interface Gráfica-------------------------------

        
        
        #------------------Label logo -------------
        app_logo = Label(frameCima ,text="Gerenciado de Livro", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15'), bg=co6, fg=co1)
        app_logo.place (x=50, y=7)
      
        
        #titulo
        self.titulo_label = tk.Label(frameDireita, text="Título do Livro:", anchor=NW, font=('Verdana 11'), bg=co3, fg=co1)
        self.titulo_entry = tk.Entry(frameDireita, width=25, justify='left', relief=SOLID)
        self.titulo_label.grid(row=1, column=0, padx=5, pady=10, sticky="NSEW")
        self.titulo_entry.grid(row=1, column=1,padx=5, pady=10, sticky="NSEW")
        

        #autor
        self.autor_label = tk.Label(frameDireita, text="Autor do Livro:", anchor=NW, font=('Verdana 11'), bg=co3, fg=co1)
        self.autor_entry = tk.Entry(frameDireita, width=25, justify='left', relief=SOLID)
        
        self.autor_label.grid(row=2, column=0, padx=5, pady=10, sticky="NSEW")
        self.autor_entry.grid(row=2, column=1, padx=5, pady=10, sticky="NSEW")
        
        #ano de lançamento
        self.ano_label = tk.Label(frameDireita, text="Ano de Lançamento:", anchor=NW, font=('Verdana 11'), bg=co3, fg=co1)
        self.ano_entry = tk.Entry(frameDireita, width=25, justify='left', relief=SOLID)
        
        self.ano_label.grid(row=3, column=0, padx=5, pady=10, sticky="NSEW")
        self.ano_entry.grid(row=3, column=1, padx=5, pady=10, sticky="NSEW")

        #genero
        self.genero_label = tk.Label(frameDireita, text="Gênero:", anchor=NW, font=('Verdana 11'), bg=co3, fg=co1)
        self.genero_entry = tk.Entry(frameDireita, width=25, justify='left', relief=SOLID)
        
        self.genero_label.grid(row=4, column=0, padx=5, pady=10, sticky="NSEW")
        self.genero_entry.grid(row=4, column=1, padx=5, pady=10, sticky="NSEW")
        
        #modificar      
        self.modificar_button = tk.Button(frameDireita, text="Alterar as informações", command=self.alterar_livro, anchor=NW, bg=co1, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        self.modificar_button.grid(row=6, column=0, pady=55, padx=105, columnspan=4)


        #botão para aperta as funções--------------------------
        #cadastro
        self.cadastrar_button = tk.Button(frameEsquerda, text="Cadastrar Livro", command=self.cadastrar_livro, anchor=NW, bg=co1, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        self.cadastrar_button.grid(row=4, column=0, columnspan=2, pady=15, padx=5)
        
        #consultar
        self.consultar_button = tk.Button(frameEsquerda, text="Consultar Livro", command=self.consultar_livro, anchor=NW, bg=co1, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        self.consultar_button.grid(row=5, column=0, columnspan=2, pady=15, padx=5)
        
        #lista autor
        self.listar_autor_button = tk.Button(frameEsquerda, text="Listar por Autor", command=self.listar_por_autor, anchor=NW, bg=co1, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        self.listar_autor_button.grid(row=6, column=0, columnspan=2, pady=15, padx=5)
        
        #genero
        self.listar_genero_button = tk.Button(frameEsquerda, text="Listar por Gênero", command=self.listar_por_genero, anchor=NW, bg=co1, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        self.listar_genero_button.grid(row=7, column=0, columnspan=2, pady=15, padx=30)
        
        #Salvar
        self.salvar_button = tk.Button(frameEsquerda, text="Salvar", command=self.salvar_dados, anchor=NW, bg=co1, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        self.salvar_button.grid(row=8, column=0, columnspan=2, pady=15, padx=5)
        
        #Carregar
        self.carregar_button = tk.Button(frameEsquerda, text="Carregar", command=self.carregar_dados, anchor=NW, bg=co1, fg=co3, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        self.carregar_button.grid(row=9, column=0, columnspan=2, pady=15, padx=5)
        
        #----------------------------------------------------Lista
        self.tree = ttk.Treeview(frameDireita, columns=('Título', 'Autor', 'Ano', 'Gênero'), show='headings')
        self.tree.heading('Título', text='Título')
        self.tree.heading('Autor', text='Autor')
        self.tree.heading('Ano', text='Ano')
        self.tree.heading('Gênero', text='Gênero')
        self.tree.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="NSEW")
        
        
        #----------------------interface--------------------------------
    def cadastrar_livro(self):
        titulo = self.titulo_entry.get()
        autor = self.autor_entry.get()
        ano = self.ano_entry.get()
        genero = self.genero_entry.get()
        

        if titulo and autor and ano and genero:
            livro = Livro(titulo, autor, ano, genero)
            self.biblioteca.cadastrar_livro(livro)
            messagebox.showinfo("Cadastro", "Livro cadastrado com sucesso!")
            
            # para atualizar a panilha
            self.atualizar_treeview() 
        else:
            messagebox.showwarning("Cadastro", "Preencha todos os campos.")

    def consultar_livro(self):
        titulo = self.titulo_entry.get()
        if titulo:
            livro = self.biblioteca.consultar_livro(titulo)
            if livro:
                # Crie uma instância da classe InformacoesLivroPopup
                InformacoesLivroPopup(self.root, livro)
                livro = self.biblioteca.consultar_livro
            else:
                messagebox.showwarning("Consulta", f"Livro com título '{titulo}' não encontrado.")
        else:
            messagebox.showwarning("Consulta", "Informe o título do livro.")

    def listar_por_autor(self):
        autor = self.autor_entry.get()
        if autor:
            livros = self.biblioteca.listar_livros_por_autor(autor)
            if livros:
                mensagem = "Livros do autor:\n\n"
                for livro in livros:
                    mensagem += f"Título: {livro.titulo}\nAno: {livro.ano}\nGênero: {livro.genero}\n\n"
                messagebox.showinfo("Listagem por Autor", mensagem)
            else:
                messagebox.showwarning("Listagem por Autor", f"Nenhum livro encontrado para o autor '{autor}'.")
        else:
            messagebox.showwarning("Listagem por Autor", "Informe o nome do autor.")

    def listar_por_genero(self):
        genero = self.genero_entry.get()
        if genero:
            livros = self.biblioteca.listar_livros_por_genero(genero)
            if livros:
                mensagem = "Livros do gênero:\n\n"
                for livro in livros:
                    mensagem += f"Título: {livro.titulo}\nAutor: {livro.autor}\nAno: {livro.ano}\n\n"
                messagebox.showinfo("Listagem por Gênero", mensagem)
            else:
                messagebox.showwarning("Listagem por Gênero", f"Nenhum livro encontrado para o gênero '{genero}'.")
        else:
            messagebox.showwarning("Listagem por Gênero", "Informe o gênero do livro.")
            
    
    def salvar_dados(self):
        nome_arquivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Arquivos JSON", "*.json")])
        if nome_arquivo:
            with open(nome_arquivo, 'w') as arquivo:
                json.dump(self.biblioteca.to_json(), arquivo, indent=2)
            print(f'Dados salvos em {nome_arquivo}')

    def carregar_dados(self):
        nome_arquivo = filedialog.askopenfilename(defaultextension=".json", filetypes=[("Arquivos JSON", "*.json")])
        if nome_arquivo:
            with open(nome_arquivo, 'r') as arquivo:
                dados = json.load(arquivo)
                self.biblioteca.from_json(dados)
            print(f'Dados carregados de {nome_arquivo}')
            
            self.atualizar_treeview()

    def atualizar_treeview(self):
        # Limpar dados antigos no Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Adicionar novos dados ao Treeview
        for livro in self.biblioteca.livros.values():
            self.tree.insert('', 'end', values=(livro.titulo, livro.autor, livro.ano, livro.genero))
            
    def alterar_livro(self):
    
        
        # Verificar se há algum item selecionado no Treeview
        if not self.tree.selection():
            messagebox.showwarning("Alteração de informações", "Nenhum livro selecionado.")
            return

        # Obter informações do livro selecionado no Treeview
        livro_selecionado = self.tree.selection()[0]
        titulo = self.tree.item(livro_selecionado, 'values')[0]
        autor = self.tree.item(livro_selecionado, 'values')[1]
        ano = self.tree.item(livro_selecionado, 'values')[2]
        genero = self.tree.item(livro_selecionado, 'values')[3]

        # Exibir informações do livro selecionado
        mensagem = f"Título: {titulo}\nAutor: {autor}\nAno: {ano}\nGênero: {genero}"
        messagebox.showinfo("Informações do livro", mensagem)

        # Criar uma nova janela para obter o novo título do livro
        popup = tk.Toplevel(self.root)
        popup.title("Digite o novo título do livro")
        popup.geometry("650x500")

        # Adicionar um Entry para o novo título
        novo_titulo_label = tk.Label(popup, text="Digite o novo Título:")
        novo_titulo_entry = tk.Entry(popup)
        novo_titulo_label.pack()
        novo_titulo_entry.pack()
        
        #Adicionar um botão para novo autor:
        novo_Autor_label = tk.Label(popup, text="Digite o novo autor:")
        novo_Autor_entry = tk.Entry(popup)
        novo_Autor_label.pack()
        novo_Autor_entry.pack()
        
        #adicionar um novo botão para o ano
        novo_Ano_label = tk.Label(popup, text="Digite o novo ano de lançamento:")
        novo_Ano_entry = tk.Entry(popup)
        novo_Ano_label.pack()
        novo_Ano_entry.pack()
        
        #adicionar um novo botão para gênero
        novo_genero_label = tk.Label(popup, text="Digite o novo Gênero:")
        novo_genero_entry = tk.Entry(popup)
        novo_genero_label.pack()
        novo_genero_entry.pack()

        def ok_button_click():
            novo_titulo = novo_titulo_entry.get()
            novo_Autor = novo_Autor_entry.get()
            novo_Ano = novo_Ano_entry.get()
            novo_genero = novo_genero_entry.get()
            
                    # Obter o livro selecionado
            livro_selecionado = self.tree.selection()[0]
            titulo = self.tree.item(livro_selecionado, 'values')[0]
            autor = self.tree.item(livro_selecionado, 'values')[1]
            Ano = self.tree.item(livro_selecionado, 'values')[2]
            genero = self.tree.item(livro_selecionado, 'values')[3]

            # Obter o objeto Livro correspondente da Biblioteca
            livro = self.biblioteca.consultar_livro(titulo)
            
            # Verificar se o livro foi encontrado
            if livro:
                # Atualizar os atributos do livro com os novos valores
                livro.titulo = novo_titulo
                livro.autor = novo_Autor
                livro.ano = novo_Ano
                livro.genero = novo_genero
                
        # Atualizar o Treeview
            self.atualizar_treeview()
                
            popup.destroy()
        
        ok_button = tk.Button(popup, text="OK", command=ok_button_click)
        ok_button.pack()
        


#----------------------------------------------------------------------------------------------------------------------------------------------
#Executavel da janela

root = tk.Tk()
root.title('Gerenciado de Livros')
root.geometry("1000x720")
root.rowconfigure(1, weight=1)
app = BibliotecaApp(root)
root.mainloop()
    

