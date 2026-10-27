| Cenário | O que o curl mostrou                          | $LASTEXITCODE | O servidor respondeu? | Onde parou                          |
|---------|-----------------------------------------------|---------------|-----------------------|-------------------------------------|
| A       | 200                                           | 0             | Sim                   | Completou tudo                      |
| B       | 503                                           | 0             | Sim                   | Completou tudo (resposta de erro)   |
| C       | (28) Operation timed out ... 0 bytes received | 28            | Não, dentro do prazo  | Conectou, mas a resposta não veio   |
| D       | (7) Failed to connect                         | 7             | Não                   | TCP (porta fechada)                 |
| E       | (6) Could not resolve host                    | 6             | Não                   | DNS (nome inexistente)              |
