# Diário Pessoal

Aplicação de diário no terminal com CRUD completo e persistência de dados em arquivo de texto.

## Funcionalidades

- Criar nova entrada (com data e hora automática)
- Ler todas as entradas
- Editar uma entrada existente
- Apagar uma entrada específica
- Apagar todas as entradas

## Conceitos aplicados

- Leitura e escrita de arquivos (`open` com modos `a`, `r`, `w`)
- `datetime` para timestamps automáticos
- `readlines()` e `writelines()` para manipulação linha a linha
- `enumerate()` para listagem numerada
- `try/except` para `FileNotFoundError` e `ValueError`
- `pop()` para remoção por índice
- Limpeza de tela com `subprocess`

## Como usar

```bash
python diario_pessoal.py
```

As entradas são salvas em `meu_diario.txt` no mesmo diretório.
