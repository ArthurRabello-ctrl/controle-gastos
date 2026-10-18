# Controle de Gastos

Aplicação de linha de comando para controle financeiro pessoal, feita em
Python com banco de dados SQLite. Permite registrar entradas e saídas,
listar lançamentos e ver o resumo mensal por categoria.

## Funcionalidades

- Registro de lançamentos com data, descrição, valor e categoria
- Listagem de todos os lançamentos
- Resumo mensal: total de entradas, saídas, saldo e gastos por categoria
- Validação de valores, datas e categorias digitados pelo usuário

## Tecnologias

- Python 3
- SQLite (módulo `sqlite3` da biblioteca padrão)

## Como executar

```bash
git clone https://github.com/ArthurRabello-ctrl/controle-gastos.git
cd controle-gastos
python dados_exemplo.py   # opcional: carrega dados fictícios
python main.py
```

## Estrutura do banco de dados

- `categorias` (id, nome, tipo)
- `lancamentos` (id, data, descricao, valor, categoria_id)

Cada lançamento se liga a uma categoria por chave estrangeira.

## Decisões técnicas

- Consultas parametrizadas (`?`) para evitar SQL Injection
- Banco e interface em arquivos separados (`banco.py` e `main.py`)
- Valores em `REAL` por simplicidade; em um sistema real, o ideal seria
  guardar centavos como inteiros para evitar erros de arredondamento

## Próximos passos

- Editar e excluir lançamentos
- Exportar relatório em CSV
- Testes automatizados
