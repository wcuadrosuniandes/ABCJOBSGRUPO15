# ABC jobs experimento 1 disponibilidad

## requisitos

## pasos para ejecutar el experimento

1. Clonar el repositorio
2. teniendo instalado docker y docker-compose ejecutar el comando `docker-compose build`
3. ejecutar el comando `docker-compose up`
4. ir a la carpeta de FormRegisterCandidateView
5. ejecutar el comando `pip install -r requirements.txt` o si se tiene virtualenv crear un entorno virtual y ejecutar el comando `pip install -r requirements.txt`
6. ejecutar el comando `python script.py` aca ya debera poder ver los resultados en la consola del enmascardo de los errores simulando el front
7. ejecutar el comando `docker-compose exec apigateway sh` para entrar al contenedor de apigateway
8. aca ya va a poder ver la carpeta de error.log que es donde el monitor esta almacenando los errores `cat error.log`
9. para ver cuantos errores capturo el monitor ejecutar el comando `wc -l error.log`