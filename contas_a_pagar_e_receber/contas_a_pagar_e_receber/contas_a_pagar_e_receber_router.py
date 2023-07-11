from decimal import Decimal
from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/contas_a_pagar_e_receber")

class cprResponse(BaseModel):
    id: int
    desc: str
    valor: Decimal
    tipo: str # pagar // receber

class cprRequest(BaseModel):
    desc: str
    valor: Decimal
    tipo: str # pagar // receber


@router.get("/", response_model=List[cprResponse])
def listar_contas():
    return [
        cprResponse(
            id=1,
            desc='ALuguel',
            valor=350,
            tipo='pagar',
        ),
        cprResponse(
            id=2,
            desc='Salário',
            valor=5000,
            tipo='receber',
        ),
    ]

@router.post("/", response_model=cprResponse, status_code=201)
def criar_conta(conta: cprRequest):
    return cprResponse(
            id=3,
            desc=conta.desc,
            valor=conta.valor,
            tipo=conta.tipo,
        )