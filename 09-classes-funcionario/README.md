# Classes — Funcionário

Sistema de funcionários com herança. Classe `Gerente` herda de `Funcionario` e gerencia uma equipe.

## Funcionalidades

- Funcionário: apresentar-se, receber aumento por percentual
- Gerente: tudo do funcionário + adicionar pessoas na equipe, listar equipe
- Apresentação personalizada mostrando tamanho da equipe

## Conceitos aplicados

- Herança com `super().__init__()` para estender o construtor
- Sobrescrita de `apresentar()` com `super()` para adicionar comportamento
- Composição: Gerente contém lista de objetos Funcionario
- Métodos com parâmetros dinâmicos (percentual de aumento)

## Como usar

```bash
python classe_funcionario.py
```
