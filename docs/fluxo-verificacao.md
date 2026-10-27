| Cenário | O que o curl mostrou                          | $LASTEXITCODE | O servidor respondeu? | Onde parou                          |
|---------|-----------------------------------------------|---------------|-----------------------|-------------------------------------|
| A       | 200                                           | 0             | Sim                   | Completou tudo                      |
| B       | 503                                           | 0             | Sim                   | Completou tudo (resposta de erro)   |
| C       | (28) Operation timed out ... 0 bytes received | 28            | Não, dentro do prazo  | Conectou, mas a resposta não veio   |
| D       | (7) Failed to connect                         | 7             | Não                   | TCP (porta fechada)                 |
| E       | (6) Could not resolve host                    | 6             | Não                   | DNS (nome inexistente)              |


# Fluxo de uma verificação

## Etapas de uma requisição

Quando um programa acessa uma URL como `https://httpbin.org/status/200`, acontecem
quatro etapas, nesta ordem. Qualquer uma delas pode falhar:

1. **DNS:** traduz o nome (`httpbin.org`) para um endereço IP. Se o nome não existe,
   para aqui.
2. **TCP:** abre uma conexão com aquele IP, na porta do serviço (443 para https,
   80 para http). Se não há nenhum programa escutando na porta, a conexão é recusada.
3. **TLS** (só em https): o servidor apresenta um certificado provando quem é, e o
   canal passa a ser criptografado. Foi a etapa mais lenta nas medições
   (cerca de 410 ms de 860 ms).
4. **HTTP:** o cliente envia o pedido (`GET /status/200`) e o servidor devolve uma
   resposta com um código de status (2xx sucesso, 4xx erro de quem pediu,
   5xx erro do servidor).

O **timeout** é o tempo máximo que o cliente aceita esperar. Sem ele, um servidor
que nunca responde travaria o monitor para sempre.

## Experimentos

Ferramentas: `curl.exe`, `Test-NetConnection` e `Resolve-DnsName` no PowerShell.
Alvos: servidor local (`python -m http.server`) e httpbin.org, conforme
[alvos autorizados](alvos-autorizados.md).

| Cenário | O que o curl mostrou                          | $LASTEXITCODE | O servidor respondeu? | Onde parou                          |
|---------|-----------------------------------------------|---------------|-----------------------|-------------------------------------|
| A       | 200                                           | 0             | Sim                   | Completou tudo                      |
| B       | 503                                           | 0             | Sim                   | Completou tudo (resposta de erro)   |
| C       | (28) Operation timed out ... 0 bytes received | 28            | Não, dentro do prazo  | Conectou, mas a resposta não veio   |
| D       | (7) Failed to connect                         | 7             | Não                   | TCP (porta fechada)                 |
| E       | (6) Could not resolve host                    | 6             | Não                   | DNS (nome inexistente)              |

### Observações

- **O 503 terminou com código de saída 0.** Para o curl, a conversa HTTP funcionou.
  O monitor não pode confiar só em "a requisição completou": precisa comparar o
  código HTTP com os códigos esperados.
- **Os tempos variam** entre medições idênticas (858 a 956 ms). Uma medição isolada
  não basta; mais à frente usaremos mediana e percentis.
- **O DNS ficou mais rápido** na terceira medição (12 ms) por causa do cache.
- **No Windows, a conexão recusada levou cerca de 2 s** para falhar. Falhar também
  leva tempo, e o timeout precisa considerar isso.

## Conclusão

O monitor precisa distinguir **quatro** tipos de resultado:

| Tipo               | Cenários | Significado                                         |
|--------------------|----------|-----------------------------------------------------|
| `success`          | A        | Respondeu com um código esperado                    |
| `http_error`       | B        | Respondeu, mas com código inesperado                |
| `timeout`          | C        | Não respondeu dentro do prazo                       |
| `connection_error` | D, E     | Não foi possível conectar (DNS, porta, rede)        |

**Por quê:** cada tipo aponta para uma investigação diferente. Um `http_error`
indica que o servidor está de pé e o problema está na aplicação ou em uma
dependência dela. Um `connection_error` indica que não há ninguém atendendo:
serviço parado, rede, firewall ou endereço errado. Um `timeout` sugere lentidão
ou sobrecarga.

DNS (E) e TCP (D) foram agrupados porque, nos dois casos, o monitor não alcançou o
servidor e a investigação começa pela infraestrutura. O detalhe de qual etapa falhou
fica registrado na mensagem de erro.
