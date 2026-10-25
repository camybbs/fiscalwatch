# FiscalWatch

Plataforma de monitoramento de disponibilidade e desempenho de serviços fiscais, desenvolvida como trilha prática de aprendizagem em Site Reliability Engineering (SRE).

## Problema

Integrações fiscais dependem de serviços externos, como APIs, web services SOAP/XML e infraestrutura de terceiros. Uma indisponibilidade, uma resposta lenta ou uma falha de comunicação pode interromper processos de emissão, consulta ou transmissão de documentos fiscais.

Sem monitoramento consistente, a equipe muitas vezes só descobre o problema quando alguém relata a falha. O FiscalWatch acompanha esses serviços continuamente para detectar indisponibilidade e degradação mais cedo.

## Público-alvo

Pessoas desenvolvedoras, profissionais de infraestrutura/SRE e equipes técnicas que precisam observar dependências de serviços fiscais.

## Objetivos

- Verificar periodicamente se um serviço responde dentro de critérios configuráveis.
- Registrar horário, resultado, código HTTP, duração e mensagem de erro de cada verificação.
- Exibir o estado atual e o histórico dos serviços monitorados.
- Abrir incidentes quando regras de falha forem atendidas e notificar responsáveis (inicialmente via Discord).
- Calcular indicadores operacionais, evoluindo para SLI, SLO e error budget.
- Manter a aplicação testável, documentada e reproduzível em ambiente local.

## Fora do escopo

- Emitir documentos fiscais ou substituir sistemas de gestão fiscal.
- Contornar autenticação, limites ou mecanismos de proteção de serviços externos.
- Armazenar certificados, credenciais ou dados fiscais reais.
- Executar varreduras ou testes de carga contra serviços de terceiros sem autorização.