quantAcoesCompra = int(input("Quantidade de ações compradas:"))

valorAcaoCompra = float(input("Valor da ação durante a compra:"))

valorTaxaCompra = float(input("Taxa paga por ação durante a compra:"))

quantAcoesVenda = int(input("Quantidade de ações vendidas:"))

valorAcaoVenda = float(input("Valor da ação durante a venda:"))

valorTaxaVenda = float(input("Taxa paga durante a venda:"))

dif = (quantAcoesVenda * valorAcaoVenda + (valorTaxaVenda * quantAcoesVenda)) - (quantAcoesCompra * valorAcaoCompra + (valorTaxaCompra * quantAcoesCompra))

print(f"\nValor total gasto na compra: R$ {quantAcoesCompra * valorAcaoCompra + (valorTaxaCompra * quantAcoesCompra):.2f}   .")

print(f"Valor pago em taxas durante a compra: R$ {valorTaxaCompra * quantAcoesCompra}   .")

print(f"Valor total ganho na venda: R$ {quantAcoesVenda * valorAcaoVenda + (valorTaxaVenda * quantAcoesVenda):.2f}   .")

print(f"Valor pago em taxas durante a venda: R$ {valorTaxaVenda * quantAcoesVenda}   .")

print(f"A diferença entre a compra e a venda é: R$ {dif}   .")
