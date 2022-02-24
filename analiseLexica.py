# Importação de libs do sistema
import re
import argparse

# Importação do Léxico
from lexico import *



class AnaliseSintatica:
    """Classe que fara a leitura e Análise Sintática de um arquivo .c"""
    def __init__(self, caminho: str):
        self.caminho = caminho
        self.analisar()
    
    def analisar(self):
        """Função que vai ler e analisar o arquivo .c definido no self.path"""        
        with open(self.caminho, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo.readlines():
                if(not self.checarReservadas(linha)):
                    return False

    def checarReservadas(self, linha: str):
        """ Separa a linha em tokens e checa se estão contidos em Palavras/Simbolos reservadas"""
        print(">>>", linha)
        print("Lenght:", len(linha))

        # Checa se a String é vazia
        if(re.match(r'^( )|()$', linha)): 
            print("Split: Linha vazia")
            return True
        # linha = linha.replace("\n", "").replace("(", " ( ").replace(")", " ) ")
        linha = re.sub(r"(;|\(|\)|,|{|}|\n|\s{1})", r" \1 ", linha)
        print("OI:", linha)
        print("Split:", linha.split(" "))
        # print("Split:", re.split(r"/;|\(|\)|,|{|}|\n|\s/g", linha))
        # print("Split:", re.split(r"/;|\(|\)|,|{|}|\n|\s{1}/g", linha))

        # linha = linha.replace(" ", "§").replace(";", "§").replace("(", "§").replace(")", "§").replace(",", "§").replace("{", "§").replace("}", "§").replace("\n", "§")
        # print(linha)
        # print(linha.split("§"))
        return True
        

if __name__ == '__main__':
    # Criação do Parser de comandos da linha de comando
    parser = argparse.ArgumentParser(description='Analisar um arquivo .c')

    # Parse Args
    parser.add_argument('path', help='Caminho do arquivo .c que você quer analisar')
    args = parser.parse_args()

    AnaliseSintatica(args.path)
