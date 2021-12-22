from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

tags_metadata = [
    {
        "name": "calc",
        "description": "Calcul la suite de fibonnaci (cf sujet).",
    }
]

app = FastAPI(openapi_tags=tags_metadata)

#CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def calculateFibonacciSum(n) :
    # On ne rentre pas dans la boucle si n = 0
    if (n <= 0) :
        return 0

    # Initialisation du tableau
    fibo =[0] * (n+1)
    fibo[1] = 1

    # Initialisation du résultat
    sn = fibo[0] + fibo[1]
    
    # Calcul de la somme
    for i in range(2,n+1) :
        fibo[i] = fibo[i-1] + fibo[i-2]
        sn = sn + fibo[i]
    return sn

@app.get("/{n}",tags=["calc"])
def calc(n: int):
    return calculateFibonacciSum(n)