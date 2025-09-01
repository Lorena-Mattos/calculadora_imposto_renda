import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from app.logic import calcular_salario_liquido

def test_calculo_normal():
    liquido_atual, liquido_proposta, inss, ir_atual, ir_proposta, dep = calcular_salario_liquido(2000, 1)
    assert round(ir_atual,2) == 0
    assert round(liquido_atual,2) == 2000 - 2000*0.08 + 200

def test_calculo_acima_ir():
    liquido_atual, liquido_proposta, inss, ir_atual, ir_proposta, dep = calcular_salario_liquido(6000, 2)
    assert round(ir_proposta,2) == 6000*0.15
    assert round(ir_atual,2) == 6000*0.15

def test_calculo_isenção_proposta():
    liquido_atual, liquido_proposta, inss, ir_atual, ir_proposta, dep = calcular_salario_liquido(5000, 0)
    assert ir_proposta == 0

def test_salario_negativo():
    with pytest.raises(ValueError):
        calcular_salario_liquido(-1000, 1)

def test_dependentes_negativo():
    with pytest.raises(ValueError):
        calcular_salario_liquido(2000, -2)
