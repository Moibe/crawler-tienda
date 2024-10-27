from fastapi import FastAPI
import crawler

app = FastAPI()

@app.get("/")
def start():
    return {"Status":"Deployed"}

@app.get("/getProducts/")
def getTokens(url: str):

    if url in ('https://www.tiendasjumbo.co/supermercado/despensa/enlatados-y-conservas', 
               'https://www.tiendasjumbo.co/supermercado/despensa/harinas-y-mezclas-para-preparar',
               'https://www.tiendasjumbo.co/supermercado/despensa/bebida-achocolatada-en-polvo',
               'https://www.tiendasjumbo.co/supermercado/despensa/aceite'
               ):
        resultado = crawler.buscaProductos(url)
    else: 
        resultado = "Url no válida para éste servicio. Revisar que sea alguna de ésta y esté escrita exactamente igual, gracias: https://www.tiendasjumbo.co/supermercado/despensa/enlatados-y-conservas, https://www.tiendasjumbo.co/supermercado/despensa/harinas-y-mezclas-para-preparar, https://www.tiendasjumbo.co/supermercado/despensa/bebida-achocolatada-en-polvo, https://www.tiendasjumbo.co/supermercado/despensa/aceite"
    return resultado