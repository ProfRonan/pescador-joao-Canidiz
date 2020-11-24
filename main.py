"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    A = float(input("Quantos quilos foram pescados?"))
    P = (A - 50) * 4 
    if P < 0: 
      P = 0 
    print(f"O peixe pescado tem {A}kg, a multa devida é R$ {P:.2f}.")


if __name__ == '__main__':
    main()
