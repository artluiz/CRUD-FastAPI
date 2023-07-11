import uvicorn
from fastapi import FastAPI

from contas_a_pagar_e_receber.contas_a_pagar_e_receber import contas_a_pagar_e_receber_router

app = FastAPI()

@app.get("/")
def home() -> str:
    return 'Bom dia'

app.include_router(contas_a_pagar_e_receber_router.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
