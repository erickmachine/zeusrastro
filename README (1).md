# Phone Tracker Simulator 📱

Ferramenta educacional em Python para simular rastreamento de números de telefone brasileiros. Desenvolvida para estudos de OSINT e estrutura de telecomunicações.

> **Aviso Legal:** Esta ferramenta utiliza apenas informações públicas sobre a estrutura de DDDs brasileiros. Não acessa dados privados, não rastreia localização real e não identifica proprietários de linhas.

---

## Requisitos

- Python 3.6+
- Kali Linux (ou qualquer distribuição Linux)

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/phone-tracker-simulator.git
cd phone-tracker-simulator
```

### 2. Dê permissão de execução

```bash
chmod +x scripts/phone_tracker.py
```

### 3. Execute a ferramenta

```bash
python3 scripts/phone_tracker.py
```

---

## Uso

### Modo Interativo

Execute o script e siga as instruções:

```bash
python3 scripts/phone_tracker.py
```

Você será solicitado a inserir:
- **DDD:** Código de área (ex: 11, 21, 31)
- **Número:** Número do telefone (8 ou 9 dígitos)

### Exemplo de Saída

```
╔══════════════════════════════════════════════════════════════════╗
║                    PHONE TRACKER SIMULATOR                       ║
║                   [ Ferramenta Educacional ]                     ║
╚══════════════════════════════════════════════════════════════════╝

[+] Digite o DDD: 11
[+] Digite o número (8 ou 9 dígitos): 987654321

══════════════════════════════════════════════════════════════════
                      RESULTADO DA ANÁLISE
══════════════════════════════════════════════════════════════════

[INFO] Número Analisado
├─ Número Completo: +55 (11) 98765-4321
├─ DDD: 11
└─ Número: 987654321

[GEO] Localização Geográfica
├─ Estado: São Paulo
├─ Região: São Paulo - Capital e Grande SP
├─ Coordenadas: -23.5505, -46.6333
└─ Fuso Horário: UTC-3 (Brasília)

[TEL] Informações de Telefonia
├─ Tipo de Linha: Celular (9 dígitos)
├─ Operadora Estimada: Vivo
└─ Prefixo: 987
```

---

## Funcionalidades

| Função | Descrição |
|--------|-----------|
| Identificação de Estado | Detecta o estado brasileiro pelo DDD |
| Tipo de Linha | Diferencia celular (9 dígitos) de fixo (8 dígitos) |
| Estimativa de Operadora | Identifica operadora pelo prefixo do número |
| Coordenadas | Retorna coordenadas aproximadas da região |

---

## DDDs Suportados

A ferramenta suporta todos os DDDs brasileiros:

| Região | DDDs |
|--------|------|
| São Paulo | 11, 12, 13, 14, 15, 16, 17, 18, 19 |
| Rio de Janeiro | 21, 22, 24 |
| Espírito Santo | 27, 28 |
| Minas Gerais | 31, 32, 33, 34, 35, 37, 38 |
| Paraná | 41, 42, 43, 44, 45, 46 |
| Santa Catarina | 47, 48, 49 |
| Rio Grande do Sul | 51, 53, 54, 55 |
| Distrito Federal | 61 |
| Goiás | 62, 64 |
| Tocantins | 63 |
| Mato Grosso | 65, 66 |
| Mato Grosso do Sul | 67 |
| Acre | 68 |
| Rondônia | 69 |
| Bahia | 71, 73, 74, 75, 77 |
| Sergipe | 79 |
| Pernambuco | 81, 87 |
| Alagoas | 82 |
| Paraíba | 83 |
| Rio Grande do Norte | 84 |
| Ceará | 85, 88 |
| Piauí | 86, 89 |
| Maranhão | 98, 99 |
| Pará | 91, 93, 94 |
| Amazonas | 92, 97 |
| Roraima | 95 |
| Amapá | 96 |

---

## Estrutura do Projeto

```
phone-tracker-simulator/
├── README.md
├── LICENSE
└── scripts/
    └── phone_tracker.py
```

---

## Disclaimer

Esta ferramenta foi desenvolvida **exclusivamente para fins educacionais**. O uso indevido para atividades ilegais é de total responsabilidade do usuário.

**O que esta ferramenta NÃO faz:**
- Não rastreia localização real de pessoas
- Não acessa dados privados ou cadastros
- Não identifica nome do proprietário da linha
- Não intercepta chamadas ou mensagens

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

1. Fork o projeto
2. Crie sua branch (`git checkout -b feature/nova-funcionalidade`)
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/nova-funcionalidade`)
5. Abra um Pull Request

---

**Desenvolvido para estudos de OSINT e telecomunicações**
```

```text file="LICENSE"
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
