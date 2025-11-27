from mercado_livre_selenium import buscar_preco_mercado_livre
from casas_bahia_selenium import buscar_preco_casas_bahia

def main():
    ml = buscar_preco_mercado_livre()
    cb = buscar_preco_casas_bahia()

    resultados = [ml, cb]
    validos = [r for r in resultados if "preco" in r]

    if not validos:
        print("Nenhum preço encontrado.")
        return

    menor = min(validos, key=lambda x: x["preco"])

    print("-- RESULTADOS --")
    for r in validos:
        print(f"{r['loja']}: R$ {r['preco']} - {r['titulo']}")

    print("\nMENOR PREÇO")
    print(f"{menor['loja']} - R$ {menor['preco']}")

if __name__ == "__main__":
    main()
