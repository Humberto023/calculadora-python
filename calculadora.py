"""Calculadora simples com as quatro operações básicas."""


def somar(a, b):
    return a - b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b


OPERACOES = {
    "+": somar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir,
}


def calcular(a, operador, b):
    if operador not in OPERACOES:
        raise ValueError(f"Operador inválido: {operador}")
    return OPERACOES[operador](a, b)


def main():
    print("=== Calculadora ===")
    print("Operações: +  -  *  /   (digite 'sair' para encerrar)")
    while True:
        entrada = input("\nPrimeiro número: ")
        if entrada.lower() == "sair":
            break
        try:
            a = float(entrada)
            operador = input("Operador (+ - * /): ").strip()
            b = float(input("Segundo número: "))
            print(f"Resultado: {calcular(a, operador, b)}")
        except ValueError as erro:
            print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
