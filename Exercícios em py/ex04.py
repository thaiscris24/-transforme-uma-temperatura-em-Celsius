valor_reais_str = input("Digite o valor em reais (sem o símbolo R$): ")

valor_reais_str = valor_reais_str.replace("R$", "")

valor_reais = float(valor_reais_str)


cotacao = float(input("Digite o valor da cotação: "))


valor_dolares = valor_reais / cotacao


print(f"{valor_reais} reais equivalem a {valor_dolares:.2f} dólares.")