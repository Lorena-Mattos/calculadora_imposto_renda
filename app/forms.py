from flask import render_template_string

HTML_FORM = """
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Calculadora de Salário Líquido</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
<style>
body {{ background: #f8f9fa; font-family: Arial, sans-serif; }}
.container {{ max-width: 700px; margin-top: 50px; }}
.card {{ border-radius: 1rem; box-shadow: 0 0 20px rgba(0,0,0,0.1); padding: 20px; }}
.btn-primary {{ border-radius: 30px; padding: 10px 20px; }}
.tooltip-text {{ font-size: 0.9em; color: #555; }}
.explicacao {{ font-size: 0.9em; margin-top: 10px; }}
</style>
</head>
<body>
<div class="container">
  <div class="card">
    <h2 class="text-center mb-4">💰 Calculadora de Salário Líquido</h2>
    <form action="/resultado" method="post">
      <div class="mb-3">
        <label class="form-label">Salário Bruto</label>
        <input type="text" class="form-control" name="salario" placeholder="Ex.: 3000,00">
        <small class="tooltip-text">
          É o salário antes de qualquer desconto. É o que você “ganha no contrato”.
        </small>
      </div>
      <div class="mb-3">
        <label class="form-label">Número de Dependentes</label>
        <input type="number" class="form-control" name="dependentes" min="0" step="1" placeholder="Ex.: 2">
        <small class="tooltip-text">
          Cada dependente gera um benefício de R$ 200,00, que reduz os descontos.
        </small>
      </div>
      <div class="form-check mb-3">
        <input class="form-check-input" type="checkbox" name="proposta_ir" id="proposta_ir">
        <label class="form-check-label" for="proposta_ir">
          Mostrar cálculo considerando proposta de isenção IR até R$ 5.000 (em tramitação)
        </label>
      </div>
      <div class="d-grid">
        <button type="submit" class="btn btn-primary">Calcular</button>
      </div>
    </form>
    <hr>
    <div class="explicacao">
      <h5>💡 Explicações para leigos:</h5>
      <ul>
        <li><strong>INSS (8%)</strong>: contribuição para a previdência, garante aposentadoria e benefícios.</li>
        <li><strong>IR (Imposto de Renda)</strong>: imposto que o governo cobra do salário. Hoje, só quem ganha acima de R$ 2.500 paga, mas há uma proposta para isenção até R$ 5.000.</li>
        <li><strong>Dependentes</strong>: cada pessoa que depende de você no IR (filhos, cônjuge, etc.) reduz o imposto em R$ 200 por dependente.</li>
        <li><strong>Salário Líquido</strong>: é o que sobra para você depois de todos os descontos e benefícios.</li>
        <li><strong>Proposta em tramitação</strong>: se aprovada, quem ganhar até R$ 5.000 não pagará IR. Aqui você já pode simular o efeito.</li>
      </ul>
    </div>
    {mensagem}
  </div>
</div>
</body>
</html>
"""

def pagina(mensagem: str = "") -> str:
    """Renderiza a página HTML, opcionalmente com mensagem de resultado."""
    return render_template_string(HTML_FORM.format(mensagem=mensagem))
