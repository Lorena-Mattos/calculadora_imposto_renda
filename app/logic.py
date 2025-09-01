from typing import Tuple

def calcular_salario_liquido(salario: float, dependentes: int) -> Tuple[float, float, float, float, float, float]:
    """
    Retorna:
    liquido_atual, liquido_proposta, inss, ir_atual, ir_proposta, beneficio_dep
    """
    if salario < 0 or dependentes < 0:
        raise ValueError("Valores negativos não são permitidos.")

    inss = salario * 0.08

    # IR vigente
    ir_atual = salario * 0.15 if salario > 2500 else 0.0

    # IR proposta (tramitação)
    ir_proposta = salario * 0.15 if salario > 5000 else 0.0

    beneficio_dep = dependentes * 200.0

    liquido_atual = salario - inss - ir_atual + beneficio_dep
    liquido_proposta = salario - inss - ir_proposta + beneficio_dep

    return liquido_atual, liquido_proposta, inss, ir_atual, ir_proposta, beneficio_dep

def brl(valor: float) -> str:
    """Formata número no padrão brasileiro."""
    neg = valor < 0
    v = abs(valor)
    s = f"{v:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"-R$ {s}" if neg else f"R$ {s}"
