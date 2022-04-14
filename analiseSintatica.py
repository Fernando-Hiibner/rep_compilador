from regras import *
import regras

class AnaliseSintatica:
    def __init__(self, tokens: list[dict]):
        self.tokens = tokens

    def analisar(self):
        print(self.tokens)
        print(REGRAS)
        """
        self.tokens
            [
                {
                    linha: 0,
                    tokens: [
                        {
                            type: FOI MAL BATI NA SUA CADEIRA BRONY
                            value: TURBANTE
                        },
                        {
                            type: Variavel
                            value: nome_var
                        }
                    ]
                },
            ]
        """
        _listaRegras = REGRAS.keys()
        _regrasASeremExecutadas = list()

        for linha in self.tokens:
            for token in linha["tokens"]:
                _tokenType = token["type"]
                _tokenValue = token["value"]

                # Pegar o value e descobrir qual regra executar
                # Tem que achar o ponto de partida e a partir dele, prosseguir, retornando erro se houver algum false
                

if __name__ == '__main__':
    print("Por favor, execute o main.py")