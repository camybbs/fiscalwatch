"""Verificação HTTP do FiscalWatch.

Faz UMA requisição a um alvo autorizado, mede o tempo e classifica o resultado.
Não grava, não agenda e não alerta: isso fica para outros módulos.
"""

import time
from datetime import datetime, timezone

import httpx

# Os quatro tipos de resultado definidos em docs/fluxo-verificacao.md
SUCCESS = "success"
HTTP_ERROR = "http_error"
TIMEOUT = "timeout"
CONNECTION_ERROR = "connection_error"

MAX_ERROR_LENGTH = 200


def check_http(url, timeout_seconds=5.0, expected_status_codes=(200,)):
    """Faz um GET em `url` e devolve um dicionário com o resultado.

    Nunca deixa uma exceção de rede escapar: toda falha vira um resultado.
    Assim, um alvo fora do ar não derruba o monitor.
    """
    checked_at = datetime.now(timezone.utc)
    start = time.perf_counter()

    try:
        response = httpx.get(url, timeout=timeout_seconds)
    except httpx.TimeoutException:
        status = TIMEOUT
        http_code = None
        error = f"Sem resposta em {timeout_seconds}s"
    except httpx.RequestError as exc:
        status = CONNECTION_ERROR
        http_code = None
        error = f"{type(exc).__name__}: {exc}"[:MAX_ERROR_LENGTH]
    else:
        # Só chega aqui se NÃO houve exceção: o servidor respondeu.
        http_code = response.status_code
        if http_code in expected_status_codes:
            status = SUCCESS
            error = None
        else:
            status = HTTP_ERROR
            error = f"Código {http_code} fora dos esperados {list(expected_status_codes)}"
        # Não guardamos o corpo da resposta: ele pode conter dados fiscais.

    duration_ms = (time.perf_counter() - start) * 1000

    return {
        "url": url,
        "status": status,
        "http_status_code": http_code,
        "duration_ms": round(duration_ms, 1),
        "checked_at": checked_at.isoformat(),
        "error_message": error,
    }
