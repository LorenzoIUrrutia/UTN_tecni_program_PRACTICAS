import time

print("\nConversor del 0 al 15 decimal a binario:\n")
time.sleep(0.5)

for i in range(16):
    numero = i        
    restos: list[int] = [] 
    resto = 0
    
    while numero > 0:
        resto = numero % 2
        restos.append(resto)
        numero = numero // 2
    restos.reverse()
    
    binario_int = 0
    for bit in restos:
        binario_int = binario_int * 10 + bit

    print(f"{i} = {binario_int}")
    time.sleep(1)  

print("\nConversión finalizada.")
