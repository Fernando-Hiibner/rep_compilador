import argparse

from analiseLexica import AnaliseLexica
from analiseSintatica import AnaliseSintatica


if __name__ == '__main__':
    # Criação do Parser de comandos da linha de comando
    parser = argparse.ArgumentParser(description='Compila um arquivo .c')

    # Parse Args (Necessary)
    parser.add_argument('input_path', help='Caminho do arquivo .c que você quer compilar')

    # Parse Args (Optional)
    parser.add_argument('-top', '--tokens_output_path', default='./data/output/tokens/token_output',
                        help='Caminho da saida .txt com os tokens separados do arquivo que você passou')
    args = parser.parse_args()

    analisadorLexico = AnaliseLexica(args.input_path, args.tokens_output_path)
    tokens = analisadorLexico.arquivoAnalisado

    analisadorSintatico = AnaliseSintatica(tokens)
    analisadorSintatico.analisar()