from multiprocessing.connection import answer_challenge
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

#Carregar o arquivo do excel
df = pd.read_excel('question.xlsx')

#Pegar as perguntaas aleatoriamente
questions = df.sample(n=10).values.tolist()

#Variaveis globais
score = 0
current_question = 0


# Função para marcação das perguntas
def check_answer(option):
    global score, current_question

    if option == correct_answer.get():
        score += 1

    current_question += 1

    if current_question < len(questions):
        display_question()
        
    else:
        show_result()

# Função para mostrar a próxima pergunta
def display_question():
    global answer  # Remova a passagem do argumento 'answer'
    question, option1, option2, option3, option4, correct_answer_text = questions[current_question]
    question_label.config(text=question)
    option1_btn.config(text=option1, state=tk.NORMAL, command=lambda: check_answer(1))
    option2_btn.config(text=option2, state=tk.NORMAL, command=lambda: check_answer(2))
    option3_btn.config(text=option3, state=tk.NORMAL, command=lambda: check_answer(3))
    option4_btn.config(text=option4, state=tk.NORMAL, command=lambda: check_answer(4))

    correct_answer.set(correct_answer_text)

#função para exibir o resultado final
def show_result():
    messagebox.showinfo("Quiz encerrado", f"Parabenéns! Você completou o Quiz. \n\n Pontuação final: {score}/{len(questions)}")
    option1_btn.config(state=tk.DISABLED)
    option2_btn.config(state=tk.DISABLED)
    option3_btn.config(state=tk.DISABLED)    
    option4_btn.config(state=tk.DISABLED)
    play_again_btn.pack()


#função para jogar novamente
def jogar_novamente():
    global score, current_question
    score = 0 
    current_question = 0
    random.shuffle(questions)
    option1_btn.config(state=tk.NORMAL)
    option2_btn.config(state=tk.NORMAL)
    option3_btn.config(state=tk.NORMAL)
    option4_btn.config(state=tk.NORMAL)
    play_again_btn.pack_forget()



#layout da tela do jogo
janela = tk.Tk()
janela.title('Nota10')
janela.geometry("600x600")

#cores de fundo e fontes das perguntas
background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"
button_test_color = "#FFFFFF"
button_text_color = "#FFFFFF"

janela.config(bg=background_color)
janela.option_add('#Font', 'Arial')


#icone na tela
app_icon = PhotoImage (file="logo.png")
app_label = tk.Label(janela, image=app_icon, bg=background_color, width=100, height=100)
app_label.pack(pady=10)


#Componente de perguntas - na interface
question_label = tk.Label(janela, text ="", wraplength=360, bg=background_color, fg=text_color, font=("Arial",12, "bold"))
question_label.pack(pady=20)

correct_answer = tk.IntVar()

#primeiro botão
option1_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_test_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option1_btn.pack(pady=10)

#Seegundo botão
option2_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_test_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option2_btn.pack(pady=10)

#Terceiro botão
option3_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_test_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option3_btn.pack(pady=10)

#Quarto botão
option4_btn = tk.Button(janela, text="", width=30, bg=button_color, fg=button_test_color, state=tk.DISABLED, font=("Arial", 10, "bold"))
option4_btn.pack(pady=10)

#Joga novamente
play_again_btn = tk.Button(janela, command=jogar_novamente, text="Jogar Novamente",  width=30, bg=button_color, fg=button_test_color, font=("Arial", 10, "bold"))




display_question()


janela.mainloop()
