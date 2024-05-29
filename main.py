# Las librerías necesarias son importadas.
from fastapi import FastAPI
import pandas as pd, numpy as np

# Se define la clase "FastAPI" a la variable "app".
app = FastAPI()

# Se define la primer api "developer".
@app.get('/Developer')
def developer(desarrollador:str)->dict:
    """
        input: Es un valor de tipo "str".

        output: Es un diccionario de la siguiente manera:
                            {
                        "Cantidad de Items": {
                            "2016": 33,
                            "2017": 16
                                            },
                        "Contenido Free": {
                            "2016": "42%",
                            "2017": "37%"
                                          }
                            }
    """

    data = pd.read_parquet("Datasets/Apis/developer/developer.parquet")     # Se importa el dataset "developer.parquet"

    ans = data[data['developer']==desarrollador][['Cantidad de Items','Contenido Free']].to_dict() # Se filtra el contenido con respecto a el parámetro "desarrollador",
                                                                                                    # se seleccionan sólo las columnas "Cantidad de Items y Contenido Free"
                                                                                                    # ya que el año está como índice dentro del dataframe,
                                                                                                    # para finalmente convertir el dataframe a un formato de diccionario.
    return ans  # Se retorna la respuesta





# Se define la segunda api "user_data".
@app.get('/userdata')
def userdata(user_id:str)->dict:
    """
        input: Es un valor de tipo "str".

        output: Es un diccionario de la siguiente manera:
                    {
                        "user_id": [
                            "--ace--"
                        ],
                        "Dinero Gastado": [
                            "4.99 USD"
                        ],
                        "% de recomendación": [
                            "100%"
                        ],
                        "Cantidad de Items": [
                            2
                        ]
                    }
    """
    user_data = pd.read_parquet("Datasets/Apis/user_data/user_data.parquet")    # Se importa el dataset "user_data.parquet".

    ans = user_data[user_data['user_id']==user_id].to_dict(orient='list')   # Se filtra la información de acuerdo a el parámetro "user_id" y
                                                                            # se transforma a un formato de diccionario. En el parámetro "orient", el valor "list" sirve
                                                                            # para especificar que retorne un diccionario donde las claves son las columnas y los valores 
                                                                            # son listas de valores de celdas.

    return ans  # Se retorna la respuesta.




# Define la tercer api "best_developer_year".
@app.get('/BestDeveloperYear')
def best_developer_year(año:int)->dict:
    """
        input: Es un valor "int" entre 2010-2015.

        output: Es un diccionario de la siguiente manera:
                    {
                    "Puesto 1": "Valve",
                    "Puesto 2": "Tripwire Interactive",
                    "Puesto 3": "Facepunch Studios"
                    }
    """
    best_developer_year = pd.read_parquet("Datasets/Apis/best_developer_year/bdy.parquet") # Se importa el dataset "bdy.parquet", donde "bdy" hace referencia a "best developer year".

    ans = best_developer_year[best_developer_year['Año']==año].nlargest(n=3,columns='Conteo')['developer'].to_list() 
    # Se filtra la información de acuerdo al parámetro "año", se seleccionan los tres valores mas grandes con "nlargest"
    # de tal forma que se pueda filtran casos en los que haya un empate de conteo, dónde "n" es el número de valores que queremos y "columns"
    # es la columna(s) por la que se quiere filtrar. Después, se selecciona sólo la información acorde con "developer", para
    # finalmente convertirlo en una lista.
    
    ans = {'Puesto 1':ans[0],     # Se crea un diccionario con las claves como el número de ranking, y como valores a los repectivos items de la lista antes creada.
           'Puesto 2':ans[1],
           'Puesto 3':ans[2]} 
    return ans # Se retorna la respuesta.




# Se define la cuarta api "developer_reviews_analysis".
@app.get('/DeveloperReviewsAnalysis')
def developer_reviews_analysis( desarrolladora : str )->dict:
    """
        input: Es un valor de tipo "str" de la columna "developer" de el dataset "steam_games.parquet"

        output: Es un diccionario de la siguiente manera:
                   {
                    "3909": [
                        "Negative = 6",
                        "Positive = 21"
                            ]
                    }
    """
    developer_reviews_analysis = pd.read_parquet("Datasets/Apis/developer_reviews_analysis/dra.parquet") # Se importa el dataset "dra.parquet", donde "dra" hace referencia a 
                                                                                                         # "developer reviews analysis".
    ans = developer_reviews_analysis.loc[desarrolladora].to_dict() # Se filtra la información respecto al parámetro "desarrolladora" y se transforma a un formato de diccionario.

    ans = {desarrolladora:[f"Negative = {ans.get('count_neg')}",f"Positive = {ans.get('count_pos')}"]} # Se crea un diccionario que toma como clave el mismo parámetro "desarrolladora",
                                                                                                       # y como valor una lista que se apoya en los valores del diccionario previamente creado.

    return ans # Se retorna la respuesta.



@app.get('/RecomendacionJuego')
def recomendacion_juego(id_de_producto:int)->list:
    """
        input: Es un valor "int" de la columna "item_id" del dataset "steam_games.parquet"

        output: Es una lista de la siguiente forma:
                        [
                        "Battle Royale Trainer",
                        "Foreign Legion: Buckets of Blood",
                        "Bionic Commando",
                        "Lead and Gold: Gangs of the Wild West",
                        "Pound of Ground",
                        "Tom Clancy's Splinter Cell®"
                        ]

    """
    steam_games = pd.read_parquet("Datasets/Apis/recomendation/games.parquet") # Se importa el dataset "recommendation.parquet" en el cual hay información filtrada de "steam_games.parquet"S
    mtx_sim = pd.read_parquet("Datasets/Apis/recomendation/cosine_sim.parquet") # Se importa el dataset "cosine_sim.parquet" el cual es la matriz de similitud.

    product_id = steam_games[steam_games['id']==id_de_producto].index[0] # En "steam_games", se busca el valor de acuerdo al parámetro "id_de_producto" y se obtiene su índice.

    recomend_prod = np.argsort(-mtx_sim[product_id])[1:6] # Se busca el índice previamente obtenido dentro de "mtx_sim(Matriz de Similitud)", con "np.argsort" se busca obtener y ordernar de menor a mayor
                                                          # los ÍNDICES. Con el signo " - (menos)" se busca reordenar de mayuor a menor. Para finalmente seleccionar del segundo al sexto elemento (top 5)
                                                          # ya que el elemento con índice 0 es el mismo producto relacionado a "id_de_producto". Dichos índices representan a los productos más similares.

    ans = list(steam_games.loc[recomend_prod,'title']) # Los índices previamente obtenidos se buscan en "steam_games" retornando sólo los títulos. Finalmente, se transforma en una lista.

    return ans # Se retorna la respuesta
