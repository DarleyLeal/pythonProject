def leiaInt(msg):
    while True:
        try:
            opc = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido!')
            continue
        except (KeyboardInterrupt):
            print('Usuário interrompeu programa! ')
            return 0
        else:
            return opc


def leiaFloat(msg):
    while True:
        try:
            opc = float(input(msg))
        except (ValueError, TypeError):
            print('Erro: por favor, digite um número real válido!')
            continue
        except (KeyboardInterrupt):
            print(f'Programa interrompido!')
            return 0
        else:
            return opc

