# Importação de libs do sistema
import argparse

# Importação do Léxico
from lexico import *



class AnaliseLexica:
    """Classe que fara a leitura e Análise Sintática de um arquivo .c"""
    def __init__(self, caminho: str):
        self.caminho = caminho
        self.analisar()
    
    def analisar(self):
        """Função que vai ler e analisar o arquivo .c definido no self.path"""
        tokens: list[dict] = list()
        with open(self.caminho, 'r', encoding='utf-8') as arquivo:
            for (index, linha) in enumerate(arquivo.readlines()):
                tokensLinha: dict = {"linha": index, "tokens": self.separarTokens(linha)}

    def separarTokens(self, linha: str):
        """ Separa a linha em tokens"""
        print(">>>", linha)
        print("Lenght:", len(linha))

        # Checa se a String é vazia
        if(len(linha.strip()) == 0): return list()
        
        # Lógica onde vamos iterar na lista e separar os tokens
        
        return list()
        

if __name__ == '__main__':
    # Criação do Parser de comandos da linha de comando
    parser = argparse.ArgumentParser(description='Analisar um arquivo .c')

    # Parse Args
    parser.add_argument('path', help='Caminho do arquivo .c que você quer analisar')
    args = parser.parse_args()

    AnaliseLexica(args.path)
