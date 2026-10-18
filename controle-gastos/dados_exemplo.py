from banco import criar_tabelas, inserir_categoria, inserir_lancamento

criar_tabelas()

categorias = [
    ("Soldo", "entrada"),
    ("Ajuda da mãe", "entrada"),
    ("Outras ajudas", "entrada"),
    ("Comissão de formatura", "saida"),
    ("SCAER", "saida"),
    ("Internet", "saida"),
    ("Cantina", "saida"),
    ("Uber", "saida"),
    ("Restaurantes", "saida"),
    ("Cinema", "saida"),
]

for nome, tipo in categorias:
    inserir_categoria(nome, tipo)

# Valores inventados, só para testar
inserir_lancamento("2026-10-01", "Soldo de outubro", 1000.00, "Soldo")
inserir_lancamento("2026-10-02", "Ajuda mensal", 300.00, "Ajuda da mãe")
inserir_lancamento("2026-10-05", "Internet do mês", 100.00, "Internet")
inserir_lancamento("2026-10-07", "Lanche na cantina", 18.50, "Cantina")
inserir_lancamento("2026-10-10", "Uber para a cidade", 32.00, "Uber")

print("Dados inseridos!")