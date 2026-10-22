peso_total = float(input("insira o peso total do peixe: "))

if peso_total > 50:
    excesso = peso_total - 50
    multa = excesso * 4
    print(f"excedeu {excesso}kg - A multa será de R${multa}")

else:
    print("Não excedeu")
    