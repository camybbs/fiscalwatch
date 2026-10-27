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


## Requisitos

- Python 3.10 ou superior
- Git

## Preparando o ambiente

```powershell
git clone https://github.com/SEU-USUARIO/fiscalwatch.git
cd fiscalwatch

python -m venv .venv
.\.venv\Scripts\Activate.ps1          # Linux/macOS: source .venv/bin/activate

pip install -r requirements-dev.txt
Copy-Item .env.example .env           # Linux/macOS: cp .env.example .env
```

## Roadmap

- [x] MVP 0: base do projeto (repositório, documentação, ambiente)
- [ ] MVP 1: monitor HTTP
- [ ] MVP 2: histórico
- [ ] MVP 3: agendamento
- [ ] MVP 4: API e dashboard
- [ ] MVP 5: alertas
- [ ] MVP 6: observabilidade
- [ ] MVP 7: entrega (Docker e CI/CD)
- [ ] MVP 8: práticas SRE