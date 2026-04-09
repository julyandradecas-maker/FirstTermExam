# FirstTermExam

Como ejecutar la API:

Primero se abre la terminal en wsl directamente en vusal studio code, luego se entra al entorno virtual:
- Para activar el servidor, se usa el comando uvicorn main:app --reload --host 0.0.0.0 --port 8000
- En el navegador se pone la url http://localhost:8000/docs para poder ir directamente a la documentación del FastAPI

Alli dentro se podran aplicar los cambios coorectamente según se lo requiera. Por ejemplo:
- En el apartado de PUT users se pone el id del usuario al que quieras actualizar y lo cambias:
  Usuario sin cambios:
   {
    "id": 1,
    "username": "admin",
    "password": "ad",
    "email": "admin@mail.com",
    "is_active": true
  },
  Usuario cambiado:
  {
    "id": 1,
    "username": "julian",
    "password": "ad",
    "email": "july@gmail.com",
    "is_active": true
  },

Código de fuerza bruta:

En la propia terminal de wsl en Visual Studio Code se debe entrar al entorno virtual y ejecutar el codigo con el comando python3 bruteforce1.py.
Después de eso se ejecutará el codigo para intentar averiguar la contraseña de un usuario especifico. Por ejemplo:
usuario_objetivo = "admin"

Salida:
[78] Intento fallido: 5
[79] Intento fallido: 6
[80] Intento fallido: 7
[81] Intento fallido: 8
[82] Intento fallido: 9
[83] Intento fallido: 0
[84] Intento fallido: aa
[85] Intento fallido: ab
[86] Intento fallido: ac
Usuario objetivo      : admin
Contraseña encontrada : ad
Total de intentos     : 87
Tiempo total          : 0.773s




