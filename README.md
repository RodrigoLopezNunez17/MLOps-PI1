# Presentación.

Se estará trabajando con tres [datasets](https://drive.google.com/drive/folders/1oQDaRujAzagUWsswGeHT_jcoYoTzc3dr?usp=drive_link) de [steam](https://store.steampowered.com/?l=spanish).

## Objetivos:

- Realizar una extracción, limpieza y carga adecuada.
- Realizar un análisis de sentimientos con la variable "review" del dataset "user_reviews.json.gz".
- Realizar el desarrollo de cinco apis utilizando [FastApi](https://fastapi.tiangolo.com/) y [Render](https://render.com/).
- Realizar un desarrollo exploratorio de los datos.
- Realizar un sistema de recomendación, ya sea item-item o user-item.

## Vistazo General.

El proyecto consta de los archivos:

- main.py: Donde se desarrolla el deploy en FastApi.
- requests.txt: Donde se enlistan las librerías utilizadas en el proyecto. Este archivo es necesario para Render.

y de las carpetas:

- Datasets: Donde se guardan todos los archivos que se crean o leen.
- ETL: En donde para cada archivo se realiza un proceso de extracción, limpieza y carga.
- Api: En donde para cada archivo se realiza la tranformación de los datasets que necesitará cada api.
- Sentiment Analysis: Donde se desarrolla el proceso de lenguaje natural.
- Sistema de Recomendación: Donde se desarrolla un sistema de recomendación item-item con similitud del coseno.
