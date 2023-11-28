import json
import os

class Livro:
    def _init_(self, titulo, autor, genero, id=None):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.id = id

class Biblioteca:
    def _init_(self):
        self.livros = []
        self.ultimo_id = 0
        if os.path.exists('livros.json'):
            with open('livros.json', 'r') as f:
                livros_json = json.load(f)
                for livro_json in livros_json:
                    livro = Livro(livro_json['titulo'], livro_json['autor'], livro_json['genero'], livro_json['id'])
                    self.livros.append(livro)
                    self.ultimo_id = max(self.ultimo_id, livro.id)

    def salvar_livros(self):
        livros_json = [
            {'titulo': livro.titulo, 'autor': livro.autor, 'genero': livro.genero, 'id': livro.id}
            for livro in self.livros
        ]
        with open('livros.json', 'w') as f:
            json.dump(livros_json, f)

    def adicionar_livro(self, livro):
        self.ultimo_id += 1
        livro.id = self.ultimo_id
        self.livros.append(livro)
        self.salvar_livros()

    def listar_livros(self):
        for livro in self.livros:
            print(f"{livro.id}: {livro.titulo}, {livro.autor}, {livro.genero}")

    def buscar_livro(self, id):
        for livro in self.livros:
            if livro.id == id:
                return livro
        return None

    def listar_livros_por_autor(self, autor):
        for livro in self.livros:
            if livro.autor == autor:
                print(f"{livro.id}: {livro.titulo}, {livro.autor}, {livro.genero}")

    def listar_livros_por_genero(self, genero):
        for livro in self.livros:
            if livro.genero == genero:
                print(f"{livro.id}: {livro.titulo}, {livro.autor}, {livro.genero}")