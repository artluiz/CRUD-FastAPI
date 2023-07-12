from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_listar_cpr():
    response = client.get("/contas_a_pagar_e_receber")

    assert response.status_code == 200

    assert response.json() == [
        {'id': 1, 'desc': 'ALuguel', 'valor': 350, 'tipo': 'pagar'},
        {'id': 2, 'desc': 'Salário', 'valor': 5000, 'tipo': 'receber'}
    ]


def test_criar_conta():
    nova_conta = {
        "desc": "Star Rail",
        "valor": 25.9,
        "tipo": "pagar"
    }
    nova_conta_copy = nova_conta.copy()

    nova_conta_copy["id"] = 3

    response = client.post("/contas_a_pagar_e_receber", json=nova_conta)
    assert response.status_code == 201
    assert response.json() == nova_conta_copy