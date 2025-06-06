import tkinter as tk 
from tkinter import scrolledtext #cria caixa de texto no scroll
import threading #evita que a tela trave enquanto o bot gera a resposta
from index import SimpleChatbot #importando a classe

class ChatbotGUI: #criação da janela
    def __init__(self, master):
        self.master = master
        master.title("Chatbot de Atendimento")
        master.geometry("500x600")
        master.resizable(False, False)

        self.chatbot = SimpleChatbot(info_base_path="info_base.json")

        #widget

        # Área de exibição das mensagens
        self.chat_history = scrolledtext.ScrolledText(master, wrap=tk.WORD, state='disable', font=("Helvetica", 10), bg="#F0F0F0")
        self.chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        #frame de entrada de texto e botão de enviar
        input_frame = tk.Frame(master)
        input_frame.pack(padx=10, pady=10, fill=tk.X)

        #campo de entrada de texto do usuario
        self.user_input = tk.Entry(input_frame, font=("Helvetica, 10"))
        self.user_input.pack(padx=10, pady=(0, 10), fill=tk.X)
        self.user_input.bind("<Return>", self.send_message_event)

        #botão de enviar
        self.send_button = tk.Button(input_frame, text="Enviar", command=self.send_message, font=("Helvetica", 10, "bold"), bg="#4CAF50", fg="white", activebackground="#45A049")
        self.send_button.pack(side=tk.RIGHT, padx=(5, 0), ipadx=10, ipady=5)

        #mensagem inicial do chatbot
        self.display_message("Chatbot: Olá, como posso ajudra você hoje?", "bot")

    def display_message(self, message, sender): #view das mensagem e colocando os indentificadores
        self.chat_history.config(state='normal')
        if sender == "user":
            self.chat_history.insert(tk.END, "você: " + message + "\n", "user_tag")
        else:
            self.chat_history.insert(tk.END, message + "\n", "bot_tag")
        self.chat_history.yview(tk.END)
        self.chat_history.config(state='disabled')

    def send_message_event(self, event=None): #botão "enter" função
        self.send_message()

    def send_message(self):
        user_message = self.user_input.get()
        if not user_message:
            return
        
        self.display_message(user_message, "user")
        self.user_input.delete(0, tk.END)#limpa a barra de texto

        #faz o processo do bot em uma thread separada para não travar a interface
        threading.Thread(target=self._process_bot_response, args=(user_message,)).start()

    def _process_bot_response(self,user_message):#desabilita a entrada de dados enquanto o bot gera a respota
        self.send_button.config(state=tk.DISABLED)
        self.user_input.config(state=tk.DISABLED)

        bot_response = self.chatbot.process_input(user_message)

        #"after" para que este processo ocorra na thread principal
        self.master.after(0, self.display_message, bot_response, "bot")

        #reabilita a entrade de dadoss
        self.master.after(0, lambda: self.send_button.config (state=tk.NORMAL))
        self.master.after(0, lambda: self.user_input.config (state=tk.NORMAL))

    
if __name__=="__main__":

    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()   