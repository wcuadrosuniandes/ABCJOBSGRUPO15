import requests

data = {
    "nombre": "test",
    "apellido": "test",
    "correo": "test@test.com",
    "experiencia": 4,
    "titulo": "test",
    "universidad": "test",
}
headers = {
    "Content-Type": "application/json",
}

for i in range(0, 100):
    response = requests.post(
        "http://localhost:5000/register-candidate", json=data, headers=headers
    )

    if response.status_code != 200:
        print(f"Estamos teniendo problemas intenta mas tarde - Status: {response.status_code}")
        continue

    try:
        json = response.json()
        correo = json.get("correo", "")
        mensaje = json.get("mensaje", "")
        status = json.get("status", "")

        print(f"Correo: {correo} - Mensaje: {mensaje} - Status: {status}")
    except requests.exceptions.JSONDecodeError:
        print("La respuesta no es un json válido")
