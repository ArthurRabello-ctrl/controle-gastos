from datetime import date, datetime

from banco import (
    criar_tabelas,
    inserir_lancamento,
    listar_categorias,
    listar_lancamentos,
    total_por_categoria,
    total_por_tipo,
)


def ler_valor():
    while True:
        texto = input("Valor (ex: 18,50): ").strip().replace(",", ".")
        try:
            valor = float(texto)
        except ValueError:
            print("Valor inválido. Digite apenas números.")
            continue
        if valor <= 0:
            print("O valor precisa ser maior que zero.")
            continue
        return valor


def ler_data():
    while True:
        texto = input("Data (AAAA-MM-DD) ou Enter para hoje: ").strip()
        if texto == "":
            return date.today().isoformat()
        try:
            datetime.strptime(texto, "%Y-%m-%d")
        except ValueError:
            print("Data inválida. Exemplo correto: 2026-10-18")
            continue
        return texto


def ler_mes():
    while True:
        texto = input("Mês (AAAA-MM) ou Enter para o mês atual: ").strip()
        if texto == "":
            return date.today().strftime("%Y-%m")
        try:
            datetime.strptime(texto, "%Y-%m")
        except ValueError:
            print("Mês inválido. Exemplo correto: 2026-10")
            continue
        return texto


def registrar():
    print("\nCategorias disponíveis:")
    for nome, tipo in listar_categorias():
        print(f"  - {nome} ({tipo})")

    categoria = input("\nCategoria: ").strip()
    descricao = input("Descrição: ").strip()
    valor = ler_valor()
    data = ler_data()

    if inserir_lancamento(data, descricao, valor, categoria):
        print("Lançamento registrado!")
    else:
        print(f"Categoria '{categoria}' não existe. Nada foi salvo.")


def ver_lancamentos():
    linhas = listar_lancamentos()
    if not linhas:
        print("\nNenhum lançamento ainda.")
        return

    print()
    for lancamento_id, data, descricao, valor, categoria, tipo in linhas:
        print(f"{data} | {categoria:<15} | {descricao:<22} | R$ {valor:>8.2f}")


def resumo():
    mes = ler_mes()
    entradas = total_por_tipo("entrada", mes)
    saidas = total_por_tipo("saida", mes)
    saldo = entradas - saidas

    print(f"\n=== RESUMO DE {mes} ===")
    print(f"Entradas: R$ {entradas:>9.2f}")
    print(f"Saídas:   R$ {saidas:>9.2f}")
    print(f"Saldo:    R$ {saldo:>9.2f}")

    gastos = total_por_categoria("saida", mes)
    if not gastos:
        print("\nNenhum gasto neste mês.")
        return

    print("\n=== GASTOS POR CATEGORIA ===")
    for nome, total, quantidade in gastos:
        print(f"{nome:<15} | R$ {total:>8.2f} | {quantidade} lançamento(s)")


def menu():
    while True:
        print("\n=== CONTROLE DE GASTOS ===")
        print("1 - Registrar lançamento")
        print("2 - Ver lançamentos")
        print("3 - Resumo do mês")
        print("0 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            registrar()
        elif opcao == "2":
            ver_lancamentos()
        elif opcao == "3":
            resumo()
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    criar_tabelas()
    menu()