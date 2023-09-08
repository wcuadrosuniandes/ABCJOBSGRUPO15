import requests

for i in range(0, 100):
    data = {
        "nombre": "test",
        "apellido": "test",
        "correo": "test@test.com",
        "experiencia": 4,
        "titulo": "test",
        "universidad": "test",
    }

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post("http://localhost:5000/register-candidate", json=data, headers=headers)
    
    if response.status_code != 200:
        print('Estamos teniendo problemas intenta mas tarde')
    else:
        correo = response.json().get('correo', '')
        mensaje = response.json().get('mensaje', '')
        status = response.json().get('status', '')

        output = f'Correo: {correo} - Mensaje: {mensaje} - Status: {status}'

        print(output)
