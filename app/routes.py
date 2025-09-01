from flask import Flask, request
from app.logic import calcular_salario_liquido, brl
from app.forms import pagina

def init_routes(app: Flask):
    @app.get("/")
    def index():
        return pagina()

    @app.post("/resultado")
    def resultado():
        try:
            salario_str = request.form.get("salario", "").replace(",", ".").strip()
            dependentes_str = request.form.get("dependentes", "").strip()
            usar_proposta = request.form.get("proposta_ir") == "on"

            salario = float(salario_str)
            dependentes = int(dependentes_str)

            liquido_atual, liquido_proposta, inss, ir_atual, ir_proposta, beneficio_dep = calcular_salario_liquido(salario, dependentes)

            msg = f"""
            <div class="alert alert-success">
              <h4 class="alert-heading">Resultado</h4>
              <ul>
                <li><strong>Salário bruto:</strong> {brl(salario)}</li>
                <li><strong>INSS (8%):</strong> {brl(inss)}</li>
                <li><strong>IR (regra atual 2.500):</strong> {brl(ir_atual)}</li>
                <li><strong>Benefício por dependentes ({dependentes}×R$200):</strong> {brl(beneficio_dep)}</li>
                <hr>
                <li><strong>💵 Salário líquido (regra atual):</strong> {brl(liquido_atual)}</li>
              </ul>
            """

            if usar_proposta:
                msg += f"""
                <div class="mt-3">
                  <strong>💵 Salário líquido (proposta IR até R$ 5.000):</strong> {brl(liquido_proposta)}
                  <br><small class='text-muted'>*Caso a proposta seja aprovada.</small>
                </div>
                """

            msg += '<a href="/" class="btn btn-outline-primary mt-3">← Novo cálculo</a></div>'

            return pagina(msg)

        except ValueError:
            return pagina('<div class="alert alert-danger">Erro: insira valores numéricos válidos e não negativos.</div>')
