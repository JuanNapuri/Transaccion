
import random
from datetime import datetime
import pytz


# ================= TRANSACCION INTERNACIONAL =================
SALDO_PERU = random.randint(111111,777777)
SALDO_CHINA = random.randint(222222,888888)

TRANSFER = random.randint(333333,444444)
ACTUAL_PERU = SALDO_PERU-TRANSFER
ACTUAL_CHINA = SALDO_CHINA + TRANSFER

print("PERU SALDO ACTUAL: ",format(SALDO_PERU, ","))
print("CHINA SALDO ACTUAL: ", format(SALDO_CHINA, ","))
print("="*80)
print("Importe de transferencia: ", format(TRANSFER, ","))
print("Saldo actualizado:\n" + "Perú = " + format(ACTUAL_PERU, ",") + "\n" + "China = " + format(ACTUAL_CHINA, ",") + "\n")



# ================= IMPRIMIR LA HORA TRANSACCION =================
print("Hora y fecha paises \n", )
limaperu = pytz.timezone('America/Lima')
shangaichina = pytz.timezone('Asia/Shanghai')

hora_peru = datetime.now(limaperu)
hora_china = datetime.now(shangaichina)

print(f"Hora y fecha capital en Peru: {hora_peru.strftime('%H:%M:%S %d/%m/%Y')}")
print(f"Hora y fecha capital en China: {hora_china.strftime('%H:%M:%S %d/%m/%Y')}")



print("-"*80)
# ================= JUEGO DE DADOS =================
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

print("Dados aleatorios \n")
print("Dado 1: ", dado1)
print("Dado 2: ", dado2)

# Comparar los resultados
if dado1 > dado2:
    print("Gano Dado 1.")
elif dado2 > dado1:
    print("Gano Dado 2.")
else:
    print("Empate.")


