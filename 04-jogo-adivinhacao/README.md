# Jogo de Adivinhação

O computador sorteia um número de 1 a 20 e o jogador tenta adivinhar em até 3 tentativas.

## Funcionalidades

- Dicas de "maior" ou "menor" a cada tentativa
- Range dinâmico que fecha conforme os palpites
- Detecção automática quando só resta um número possível
- Aviso de última tentativa
- Validação de entrada (número fora do range, texto inválido)

## Conceitos aplicados

- Módulo `random` (`randint`)
- `while` com contador de tentativas
- `try/except` para tratamento de erros
- Flag booleana (`acertou`)
- Atualização dinâmica de limites (`minimo`/`maximo`)

## Como usar

```bash
python jogo_adivinhacao.py
```
