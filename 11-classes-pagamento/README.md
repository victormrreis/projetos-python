# Classes — Sistema de Pagamento

Sistema de pagamento com polimorfismo. Classe base `Pagamento` com filhas `Pix`, `Cartao` e `Boleto`, cada uma processando o pagamento de forma diferente.

## Conceitos aplicados

- Polimorfismo (mesmo método `processar()`, saídas diferentes)
- Herança
- Cálculo com parâmetros (parcelas no cartão)
- Iteração sobre lista de objetos com `for`
- F-strings com formatação monetária

## Como usar

```bash
python classe_pagamento.py
```
