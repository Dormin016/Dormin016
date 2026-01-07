from datetime import datetime, timedelta
#entrada de dados
vencimento = input("Digite a data de vencimento (dd/mm/aaaa): ")

#converção para datetime
vencimento_dt = datetime.strptime(vencimento, "%d/%m/%Y")
hoje = datetime.now()

#calculo da difernça
diferença = vencimento_dt - hoje + timedelta(days=1)

print(f"faltam {diferença.days} dias para o vencimento.")