import re
import random
import json

class SimpleChatbot:
    def __init__(self, info_base_path="info_base.json"): #construtor da classe
        self.info_base = self._load_info_base(info_base_path) #chama o metodo _load_ para carregar os dados do arquivo json e os armazena na variavel self.

    def _load_info_base(self, path): #Este é um método privado. Sua função é carregar a base de conhecimento.
        with open(path, 'r', encoding='utf-8') as f:#Abre o arquivo especificado pelo path no modo de leitura ('r'). O encoding='utf-8' é importante para garantir que caracteres especiais (acentos, cedilhas) sejam lidos corretamente. O with garante que o arquivo seja fechado automaticamente após o uso.
            return json.load(f)

    def process_input(self, user_input):
        user_input = user_input.lower().strip() # Normaliza a entrada

        for intent, data in self.info_base.items():
            for pattern in data["patterns"]:
                if re.search(pattern, user_input): # Usa regex para encontrar o padrão
                    return random.choice(data["responses"])

        # Se nenhuma intenção for encontrada
        return "Desculpe, não entendi. Você pode reformular sua pergunta?"
    
