# Importação de libs do sistema
from json import dumps
from datetime import datetime
from pathlib import Path

# Importação do Léxico
from lexico import *


class AnaliseLexica:
    """Classe que fara a leitura e Análise Sintática de um arquivo .c"""

    def __init__(self, caminho: str, caminhoSaida: str):
        self.caminho = caminho
        self.caminhoSaida = caminhoSaida
        self.arquivoAnalisado: list[dict] = list()
        self.analisar()

    def analisar(self):
        """Função que vai ler e analisar o arquivo .c definido no self.path"""
        tokens: list[dict] = list()
        with open(Path(self.caminho), 'r', encoding='utf-8') as arquivo:
            for (index, linha) in enumerate(arquivo.readlines()):
                # tokensLinha: dict = {"linha": index, "tokens": self.separarTokens(linha)}
                tokens.append(
                    {"linha": index, "tokens": self.separarTokens(linha)})

        self.arquivoAnalisado = tokens

        data = str(datetime.now()).replace(":", "-")
        with open(Path(self.caminhoSaida+data+".json"), 'w', encoding='utf-8') as saida:
            saida.write(str(dumps(tokens, indent=4)))
            saida.close()

    def separarTokens(self, linha: str):
        """ Separa a linha em tokens"""

        # Checa se a String é vazia
        if(len(linha.strip()) == 0):
            return list()

        # Lógica onde vamos iterar na lista e separar os tokens
        listaTokens: list = list()
        _token: str = str()
        _pular: int = 0
        for (index, char) in enumerate(linha):
            if(_pular > 0):
                _pular -= 1
                continue
            if(char in SIMBOLOS_DE_ENCAPSULAMENTO):
                if(len(_token.strip()) != 0):
                    listaTokens.append(_token)
                listaTokens.append(char)
                _token = ""
                continue

            if(_token in PALAVRAS_RESERVADAS or _token in SIMBOLOS_DE_ENCAPSULAMENTO):
                listaTokens.append(_token)
                _token = ""
                continue

            _tokenPlusChar = _token + char
            if(_tokenPlusChar in PALAVRAS_RESERVADAS or _tokenPlusChar in SIMBOLOS_DE_ENCAPSULAMENTO):
                listaTokens.append(_tokenPlusChar)
                _token = ""
                continue
            if(char in SIMBOLOS_RESERVADOS):
                try:
                    _triplo = char+linha[index+1]+linha[index+2]
                except:
                    _triplo = None

                try:
                    _duplo = char+linha[index+1]
                except:
                    _duplo = None

                if(_triplo in SIMBOLOS_COMPOSTOS_TRIPLOS):
                    if(len(_token.strip()) != 0):
                        listaTokens.append(_token)
                    listaTokens.append(_triplo)
                    _token = ""
                    _pular = 2
                    continue

                elif(_duplo in SIMBOLOS_COMPOSTOS_DUPLOS):
                    if(len(_token.strip()) != 0):
                        listaTokens.append(_token)
                    listaTokens.append(_duplo)
                    _token = ""
                    _pular = 1
                    continue
                else:
                    if(len(_token.strip()) != 0):
                        listaTokens.append(_token)
                    listaTokens.append(char)
                    _token = ""
                    continue

            if(len(char.strip()) == 0):
                if(len(_token.strip()) == 0):
                    continue
                else:
                    listaTokens.append(_token)
                    _token = ""
                    continue
            _token += char

        if(len(listaTokens) > 0):
            for (index, item) in enumerate(listaTokens):
                if(item in SIMBOLOS_COMPOSTOS_TRIPLOS):
                    listaTokens[index] = {
                        "type": "SIMBOLO_COMPOSTO_TRIPLO", "value": item}
                elif(item in SIMBOLOS_COMPOSTOS_DUPLOS):
                    listaTokens[index] = {
                        "type": "SIMBOLO_COMPOSTO_DUPLO", "value": item}
                elif(item in SIMBOLOS_RESERVADOS):
                    listaTokens[index] = {
                        "type": "SIMBOLO_RESERVADO", "value": item}
                elif(item in SIMBOLOS_DE_ENCAPSULAMENTO):
                    listaTokens[index] = {
                        "type": "SIMBOLO_DE_ENCAPSULAMENTO", "value": item}
                elif(item in PALAVRAS_RESERVADAS):
                    listaTokens[index] = {
                        "type": "PALAVRA_RESERVADA", "value": item}
                else:
                    listaTokens[index] = {
                        "type": "INDETERMINADO", "value": item}
            return listaTokens
        else:
            return list()


if __name__ == '__main__':
    print("Por favor, execute o main.py")
