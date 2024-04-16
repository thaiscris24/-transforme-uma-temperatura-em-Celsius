
nome_produto = input("Digite o nome do produto: ")
quantidade = float(input("Digite a quantidade comprada: "))
valor_unitario = float(input("Digite o valor unitário do produto: "))


percentual_desconto_str = input("Digite o percentual de desconto a ser aplicado: ")
percentual_desconto = float(percentual_desconto_str.rstrip('%'))


total_sem_desconto = quantidade * valor_unitario


desconto = total_sem_desconto * (percentual_desconto / 100)


total_com_desconto = total_sem_desconto - desconto

print("Nome do produto:", nome_produto)
print("Valor total da venda:", total_com_desconto)