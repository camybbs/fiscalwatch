"""Executa uma verificação manual.

Uso: python -m app.main URL
"""

import sys

from app.monitors.http_monitor import SUCCESS, check_http


def main():
    if len(sys.argv) != 2:
        print("Uso: python -m app.main URL")
        return 2

    result = check_http(sys.argv[1])

    for campo, valor in result.items():
        print(f"{campo:>17}: {valor}")

    # Código de saída: 0 = sucesso, 1 = falha (igual ao $LASTEXITCODE da Aula 5)
    return 0 if result["status"] == SUCCESS else 1


if __name__ == "__main__":
    sys.exit(main())
