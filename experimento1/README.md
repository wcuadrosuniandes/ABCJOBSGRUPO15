# ABC jobs experimento 1 disponibilidad

## Requisitos

- Docker
- Docker compose
- Python 3.9

## Pasos para ejecutar el experimento

1. Clonar el repositorio
2. Teniendo instalado docker y docker-compose ejecutar el comando `docker-compose build`
3. Ejecutar el comando `docker-compose up`
4. Ir a la carpeta de FormRegisterCandidateView
5. Ejecutar el comando `pip install -r requirements.txt` o si se tiene virtualenv crear un entorno virtual y ejecutar el comando `pip install -r requirements.txt`
6. Ejecutar el comando `python script.py` aca ya debera poder ver los resultados en la consola del enmascardo de los errores simulando el front
7. Ejecutar el comando `docker-compose exec apigateway /bin/bash` para entrar al contenedor de apigateway
8. Aca ya va a poder ver la carpeta de error.log que es donde el monitor esta almacenando los errores `cat error.log`
9. Para ver cuantos errores fueron capturados el monitor ejecutar el comando `wc -l error.log`
