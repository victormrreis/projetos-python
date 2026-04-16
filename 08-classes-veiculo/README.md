# Classes — Veículo

Sistema de veículos com herança. Classe base `Veiculo` com filhas `Carro` e `Moto`, cada uma com comportamentos próprios.

## Funcionalidades

- Veículo: acelerar, frear (com limite em 0), ver status
- Carro: buzinar, aviso de cinto antes de acelerar
- Moto: empinar (só em movimento), aviso ao estacionar

## Conceitos aplicados

- Herança (`class Carro(Veiculo)`)
- Sobrescrita de métodos
- `super()` para chamar métodos da classe pai
- Validação de estado antes de ações

## Como usar

```bash
python classe_veiculo.py
```
