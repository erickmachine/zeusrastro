#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📱 Phone Tracker Simulator - Ferramenta Educacional
Simula rastreamento de números de telefone brasileiros
Apenas para fins de estudo - Usa informações públicas de DDDs e operadoras
"""

import sys
import time
import random

# Cores ANSI para terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# Base de dados de DDDs brasileiros
DDD_DATABASE = {
    # São Paulo
    "11": {"estado": "São Paulo", "cidade": "São Paulo e Região Metropolitana", "regiao": "Sudeste"},
    "12": {"estado": "São Paulo", "cidade": "São José dos Campos, Taubaté", "regiao": "Sudeste"},
    "13": {"estado": "São Paulo", "cidade": "Santos, São Vicente", "regiao": "Sudeste"},
    "14": {"estado": "São Paulo", "cidade": "Bauru, Marília", "regiao": "Sudeste"},
    "15": {"estado": "São Paulo", "cidade": "Sorocaba", "regiao": "Sudeste"},
    "16": {"estado": "São Paulo", "cidade": "Ribeirão Preto", "regiao": "Sudeste"},
    "17": {"estado": "São Paulo", "cidade": "São José do Rio Preto", "regiao": "Sudeste"},
    "18": {"estado": "São Paulo", "cidade": "Presidente Prudente", "regiao": "Sudeste"},
    "19": {"estado": "São Paulo", "cidade": "Campinas, Piracicaba", "regiao": "Sudeste"},
    # Rio de Janeiro
    "21": {"estado": "Rio de Janeiro", "cidade": "Rio de Janeiro e Região Metropolitana", "regiao": "Sudeste"},
    "22": {"estado": "Rio de Janeiro", "cidade": "Campos dos Goytacazes, Nova Friburgo", "regiao": "Sudeste"},
    "24": {"estado": "Rio de Janeiro", "cidade": "Volta Redonda, Petrópolis", "regiao": "Sudeste"},
    # Espírito Santo
    "27": {"estado": "Espírito Santo", "cidade": "Vitória, Vila Velha", "regiao": "Sudeste"},
    "28": {"estado": "Espírito Santo", "cidade": "Cachoeiro de Itapemirim", "regiao": "Sudeste"},
    # Minas Gerais
    "31": {"estado": "Minas Gerais", "cidade": "Belo Horizonte e Região Metropolitana", "regiao": "Sudeste"},
    "32": {"estado": "Minas Gerais", "cidade": "Juiz de Fora", "regiao": "Sudeste"},
    "33": {"estado": "Minas Gerais", "cidade": "Governador Valadares", "regiao": "Sudeste"},
    "34": {"estado": "Minas Gerais", "cidade": "Uberlândia, Uberaba", "regiao": "Sudeste"},
    "35": {"estado": "Minas Gerais", "cidade": "Poços de Caldas, Varginha", "regiao": "Sudeste"},
    "37": {"estado": "Minas Gerais", "cidade": "Divinópolis", "regiao": "Sudeste"},
    "38": {"estado": "Minas Gerais", "cidade": "Montes Claros", "regiao": "Sudeste"},
    # Paraná
    "41": {"estado": "Paraná", "cidade": "Curitiba e Região Metropolitana", "regiao": "Sul"},
    "42": {"estado": "Paraná", "cidade": "Ponta Grossa", "regiao": "Sul"},
    "43": {"estado": "Paraná", "cidade": "Londrina", "regiao": "Sul"},
    "44": {"estado": "Paraná", "cidade": "Maringá", "regiao": "Sul"},
    "45": {"estado": "Paraná", "cidade": "Foz do Iguaçu, Cascavel", "regiao": "Sul"},
    "46": {"estado": "Paraná", "cidade": "Pato Branco, Francisco Beltrão", "regiao": "Sul"},
    # Santa Catarina
    "47": {"estado": "Santa Catarina", "cidade": "Joinville, Blumenau", "regiao": "Sul"},
    "48": {"estado": "Santa Catarina", "cidade": "Florianópolis", "regiao": "Sul"},
    "49": {"estado": "Santa Catarina", "cidade": "Chapecó, Lages", "regiao": "Sul"},
    # Rio Grande do Sul
    "51": {"estado": "Rio Grande do Sul", "cidade": "Porto Alegre e Região Metropolitana", "regiao": "Sul"},
    "53": {"estado": "Rio Grande do Sul", "cidade": "Pelotas, Rio Grande", "regiao": "Sul"},
    "54": {"estado": "Rio Grande do Sul", "cidade": "Caxias do Sul, Passo Fundo", "regiao": "Sul"},
    "55": {"estado": "Rio Grande do Sul", "cidade": "Santa Maria", "regiao": "Sul"},
    # Centro-Oeste
    "61": {"estado": "Distrito Federal", "cidade": "Brasília", "regiao": "Centro-Oeste"},
    "62": {"estado": "Goiás", "cidade": "Goiânia", "regiao": "Centro-Oeste"},
    "63": {"estado": "Tocantins", "cidade": "Palmas", "regiao": "Norte"},
    "64": {"estado": "Goiás", "cidade": "Rio Verde, Itumbiara", "regiao": "Centro-Oeste"},
    "65": {"estado": "Mato Grosso", "cidade": "Cuiabá", "regiao": "Centro-Oeste"},
    "66": {"estado": "Mato Grosso", "cidade": "Rondonópolis", "regiao": "Centro-Oeste"},
    "67": {"estado": "Mato Grosso do Sul", "cidade": "Campo Grande", "regiao": "Centro-Oeste"},
    "68": {"estado": "Acre", "cidade": "Rio Branco", "regiao": "Norte"},
    "69": {"estado": "Rondônia", "cidade": "Porto Velho", "regiao": "Norte"},
    # Nordeste
    "71": {"estado": "Bahia", "cidade": "Salvador", "regiao": "Nordeste"},
    "73": {"estado": "Bahia", "cidade": "Ilhéus, Itabuna", "regiao": "Nordeste"},
    "74": {"estado": "Bahia", "cidade": "Juazeiro", "regiao": "Nordeste"},
    "75": {"estado": "Bahia", "cidade": "Feira de Santana", "regiao": "Nordeste"},
    "77": {"estado": "Bahia", "cidade": "Vitória da Conquista, Barreiras", "regiao": "Nordeste"},
    "79": {"estado": "Sergipe", "cidade": "Aracaju", "regiao": "Nordeste"},
    "81": {"estado": "Pernambuco", "cidade": "Recife", "regiao": "Nordeste"},
    "82": {"estado": "Alagoas", "cidade": "Maceió", "regiao": "Nordeste"},
    "83": {"estado": "Paraíba", "cidade": "João Pessoa, Campina Grande", "regiao": "Nordeste"},
    "84": {"estado": "Rio Grande do Norte", "cidade": "Natal", "regiao": "Nordeste"},
    "85": {"estado": "Ceará", "cidade": "Fortaleza", "regiao": "Nordeste"},
    "86": {"estado": "Piauí", "cidade": "Teresina", "regiao": "Nordeste"},
    "87": {"estado": "Pernambuco", "cidade": "Petrolina, Garanhuns", "regiao": "Nordeste"},
    "88": {"estado": "Ceará", "cidade": "Juazeiro do Norte, Sobral", "regiao": "Nordeste"},
    "89": {"estado": "Piauí", "cidade": "Picos, Floriano", "regiao": "Nordeste"},
    # Norte
    "91": {"estado": "Pará", "cidade": "Belém", "regiao": "Norte"},
    "92": {"estado": "Amazonas", "cidade": "Manaus", "regiao": "Norte"},
    "93": {"estado": "Pará", "cidade": "Santarém", "regiao": "Norte"},
    "94": {"estado": "Pará", "cidade": "Marabá", "regiao": "Norte"},
    "95": {"estado": "Roraima", "cidade": "Boa Vista", "regiao": "Norte"},
    "96": {"estado": "Amapá", "cidade": "Macapá", "regiao": "Norte"},
    "97": {"estado": "Amazonas", "cidade": "Interior do Amazonas", "regiao": "Norte"},
    "98": {"estado": "Maranhão", "cidade": "São Luís", "regiao": "Nordeste"},
    "99": {"estado": "Maranhão", "cidade": "Imperatriz, Caxias", "regiao": "Nordeste"},
}

# Prefixos de operadoras (simulado - baseado em padrões comuns)
OPERADORAS = {
    "9": {
        "96": "Vivo",
        "97": "Vivo", 
        "98": "Vivo",
        "99": "Vivo",
        "91": "Claro",
        "92": "Claro",
        "93": "Claro",
        "94": "Claro",
        "84": "TIM",
        "85": "TIM",
        "88": "TIM",
        "89": "TIM",
        "81": "Oi",
        "82": "Oi",
        "83": "Oi",
    }
}

def print_banner():
    """Exibe o banner da ferramenta"""
    banner = f"""
{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗
║{Colors.GREEN}  ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗                  {Colors.CYAN}║
║{Colors.GREEN}  ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝                  {Colors.CYAN}║
║{Colors.GREEN}  ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗                    {Colors.CYAN}║
║{Colors.GREEN}  ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝                    {Colors.CYAN}║
║{Colors.GREEN}  ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗                  {Colors.CYAN}║
║{Colors.GREEN}  ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝                  {Colors.CYAN}║
║{Colors.YELLOW}        ████████╗██████╗  █████╗  ██████╗██╗  ██╗              {Colors.CYAN}║
║{Colors.YELLOW}        ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝              {Colors.CYAN}║
║{Colors.YELLOW}           ██║   ██████╔╝███████║██║     █████╔╝               {Colors.CYAN}║
║{Colors.YELLOW}           ██║   ██╔══██╗██╔══██║██║     ██╔═██╗               {Colors.CYAN}║
║{Colors.YELLOW}           ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗              {Colors.CYAN}║
║{Colors.YELLOW}           ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝              {Colors.CYAN}║
╠══════════════════════════════════════════════════════════════╣
║{Colors.WHITE}  📱 Phone Tracker Simulator v1.0                             {Colors.CYAN}║
║{Colors.WHITE}  🎓 Ferramenta Educacional - Apenas para Estudos             {Colors.CYAN}║
║{Colors.WHITE}  🐧 Otimizado para Kali Linux                                {Colors.CYAN}║
╚══════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)

def print_loading(text, duration=2):
    """Simula uma animação de carregamento"""
    chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{Colors.YELLOW}[{chars[i % len(chars)]}] {text}...{Colors.RESET}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write(f'\r{Colors.GREEN}[✓] {text}... Concluído!{Colors.RESET}\n')

def clean_number(phone):
    """Remove caracteres não numéricos do número"""
    return ''.join(filter(str.isdigit, phone))

def get_operadora(numero):
    """Tenta identificar a operadora pelo prefixo (simulado)"""
    if len(numero) >= 2:
        primeiro = numero[0]
        prefixo = numero[:2]
        if primeiro == "9" and prefixo in OPERADORAS.get("9", {}):
            return OPERADORAS["9"][prefixo]
    
    # Se não encontrar, retorna uma operadora aleatória (simulação)
    operadoras = ["Vivo", "Claro", "TIM", "Oi"]
    return random.choice(operadoras)

def get_tipo_linha(numero):
    """Identifica se é celular ou fixo"""
    if numero.startswith("9") or numero.startswith("8") or numero.startswith("7"):
        return "Celular (Móvel)"
    else:
        return "Telefone Fixo"

def track_number(ddd, numero):
    """Rastreia o número e exibe informações"""
    print(f"\n{Colors.CYAN}{'═' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.WHITE}🔍 INICIANDO RASTREAMENTO...{Colors.RESET}")
    print(f"{Colors.CYAN}{'═' * 60}{Colors.RESET}\n")
    
    # Animações de loading
    print_loading("Conectando aos servidores", 1.5)
    print_loading("Consultando base de dados de DDDs", 1)
    print_loading("Identificando operadora", 1)
    print_loading("Coletando informações da região", 1.5)
    print_loading("Processando dados", 1)
    
    # Busca informações do DDD
    info_ddd = DDD_DATABASE.get(ddd)
    
    if not info_ddd:
        print(f"\n{Colors.RED}[✗] DDD {ddd} não encontrado na base de dados!{Colors.RESET}")
        print(f"{Colors.YELLOW}[!] DDDs válidos: 11-99 (Brasil){Colors.RESET}\n")
        return False
    
    # Obtém informações
    operadora = get_operadora(numero)
    tipo_linha = get_tipo_linha(numero)
    numero_formatado = f"({ddd}) {numero[:5]}-{numero[5:]}" if len(numero) >= 9 else f"({ddd}) {numero}"
    
    # Exibe resultados
    print(f"\n{Colors.GREEN}{'═' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.GREEN}✓ RASTREAMENTO CONCLUÍDO COM SUCESSO!{Colors.RESET}")
    print(f"{Colors.GREEN}{'═' * 60}{Colors.RESET}\n")
    
    print(f"{Colors.CYAN}┌──────────────────────────────────────────────────────────┐{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.BOLD}{Colors.WHITE}  📱 INFORMAÇÕES DO NÚMERO                               {Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}├──────────────────────────────────────────────────────────┤{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} {Colors.YELLOW}Número:{Colors.RESET}      {numero_formatado:<41}{Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} {Colors.YELLOW}DDD:{Colors.RESET}         {ddd:<41}{Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} {Colors.YELLOW}Tipo:{Colors.RESET}        {tipo_linha:<41}{Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}├──────────────────────────────────────────────────────────┤{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.BOLD}{Colors.WHITE}  🌍 LOCALIZAÇÃO                                         {Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}├──────────────────────────────────────────────────────────┤{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} {Colors.YELLOW}Estado:{Colors.RESET}      {info_ddd['estado']:<41}{Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} {Colors.YELLOW}Cidade:{Colors.RESET}      {info_ddd['cidade'][:41]:<41}{Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} {Colors.YELLOW}Região:{Colors.RESET}      {info_ddd['regiao']:<41}{Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}├──────────────────────────────────────────────────────────┤{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.BOLD}{Colors.WHITE}  📡 OPERADORA                                           {Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}├──────────────────────────────────────────────────────────┤{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} {Colors.YELLOW}Operadora:{Colors.RESET}   {operadora:<41}{Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}│{Colors.RESET} {Colors.YELLOW}Status:{Colors.RESET}      {Colors.GREEN}Ativo (Simulado){Colors.RESET}                         {Colors.CYAN}│{Colors.RESET}")
    print(f"{Colors.CYAN}└──────────────────────────────────────────────────────────┘{Colors.RESET}")
    
    # Coordenadas simuladas (centro aproximado da região)
    coords_simuladas = {
        "Sudeste": ("-23.5505", "-46.6333"),
        "Sul": ("-25.4284", "-49.2733"),
        "Nordeste": ("-12.9714", "-38.5014"),
        "Norte": ("-1.4558", "-48.4902"),
        "Centro-Oeste": ("-15.7801", "-47.9292"),
    }
    
    lat, lon = coords_simuladas.get(info_ddd['regiao'], ("-15.7801", "-47.9292"))
    
    print(f"\n{Colors.MAGENTA}┌──────────────────────────────────────────────────────────┐{Colors.RESET}")
    print(f"{Colors.MAGENTA}│{Colors.BOLD}{Colors.WHITE}  📍 COORDENADAS APROXIMADAS (Centro da Região)          {Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.MAGENTA}├──────────────────────────────────────────────────────────┤{Colors.RESET}")
    print(f"{Colors.MAGENTA}│{Colors.RESET} {Colors.YELLOW}Latitude:{Colors.RESET}    {lat:<41}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.MAGENTA}│{Colors.RESET} {Colors.YELLOW}Longitude:{Colors.RESET}   {lon:<41}{Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.MAGENTA}│{Colors.RESET} {Colors.YELLOW}Google Maps:{Colors.RESET} https://maps.google.com/?q={lat},{lon}   {Colors.MAGENTA}│{Colors.RESET}")
    print(f"{Colors.MAGENTA}└──────────────────────────────────────────────────────────┘{Colors.RESET}")
    
    return True

def show_ddd_list():
    """Mostra lista de DDDs disponíveis"""
    print(f"\n{Colors.CYAN}{'═' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.WHITE}📋 LISTA DE DDDs BRASILEIROS{Colors.RESET}")
    print(f"{Colors.CYAN}{'═' * 60}{Colors.RESET}\n")
    
    regioes = {}
    for ddd, info in DDD_DATABASE.items():
        regiao = info['regiao']
        if regiao not in regioes:
            regioes[regiao] = []
        regioes[regiao].append((ddd, info['estado'], info['cidade']))
    
    for regiao, ddds in sorted(regioes.items()):
        print(f"{Colors.YELLOW}▸ {regiao}:{Colors.RESET}")
        for ddd, estado, cidade in sorted(ddds):
            print(f"  {Colors.GREEN}{ddd}{Colors.RESET} - {estado} ({cidade})")
        print()

def main():
    """Função principal"""
    print_banner()
    
    while True:
        print(f"\n{Colors.CYAN}┌──────────────────────────────────────────────────────────┐{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.BOLD}{Colors.WHITE}  MENU PRINCIPAL                                         {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}├──────────────────────────────────────────────────────────┤{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}[1]{Colors.RESET} Rastrear número de telefone                        {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}[2]{Colors.RESET} Listar DDDs brasileiros                            {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.GREEN}[3]{Colors.RESET} Sobre a ferramenta                                 {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}│{Colors.RESET}  {Colors.RED}[0]{Colors.RESET} Sair                                               {Colors.CYAN}│{Colors.RESET}")
        print(f"{Colors.CYAN}└──────────────────────────────────────────────────────────┘{Colors.RESET}")
        
        try:
            opcao = input(f"\n{Colors.YELLOW}➤ Escolha uma opção: {Colors.RESET}").strip()
        except KeyboardInterrupt:
            print(f"\n\n{Colors.RED}[!] Operação cancelada pelo usuário.{Colors.RESET}")
            break
        
        if opcao == "1":
            print(f"\n{Colors.WHITE}Digite o número no formato: DDD + NÚMERO{Colors.RESET}")
            print(f"{Colors.WHITE}Exemplo: 11999887766 ou (11) 99988-7766{Colors.RESET}\n")
            
            try:
                telefone = input(f"{Colors.YELLOW}➤ Número de telefone: {Colors.RESET}").strip()
            except KeyboardInterrupt:
                print(f"\n{Colors.RED}[!] Operação cancelada.{Colors.RESET}")
                continue
            
            # Limpa o número
            numero_limpo = clean_number(telefone)
            
            if len(numero_limpo) < 10:
                print(f"\n{Colors.RED}[✗] Número inválido! Deve ter pelo menos 10 dígitos (DDD + número).{Colors.RESET}")
                continue
            
            # Extrai DDD e número
            ddd = numero_limpo[:2]
            numero = numero_limpo[2:]
            
            # Executa o rastreamento
            track_number(ddd, numero)
            
        elif opcao == "2":
            show_ddd_list()
            
        elif opcao == "3":
            print(f"\n{Colors.CYAN}{'═' * 60}{Colors.RESET}")
            print(f"{Colors.BOLD}{Colors.WHITE}📚 SOBRE A FERRAMENTA{Colors.RESET}")
            print(f"{Colors.CYAN}{'═' * 60}{Colors.RESET}")
            print(f"""
{Colors.WHITE}Phone Tracker Simulator v1.0{Colors.RESET}

{Colors.YELLOW}Descrição:{Colors.RESET}
  Esta é uma ferramenta {Colors.GREEN}EDUCACIONAL{Colors.RESET} que simula o rastreamento
  de números de telefone brasileiros utilizando informações 
  {Colors.GREEN}PÚBLICAS{Colors.RESET} sobre a estrutura de numeração telefônica do Brasil.

{Colors.YELLOW}Funcionalidades:{Colors.RESET}
  • Identificação do estado e região pelo DDD
  • Identificação aproximada da cidade/área
  • Detecção do tipo de linha (móvel/fixo)
  • Estimativa da operadora pelo prefixo

{Colors.YELLOW}Limitações:{Colors.RESET}
  • {Colors.RED}NÃO{Colors.RESET} rastreia localização real de pessoas
  • {Colors.RED}NÃO{Colors.RESET} acessa dados privados
  • {Colors.RED}NÃO{Colors.RESET} identifica o proprietário da linha
  • Coordenadas são aproximadas (centro da região)

{Colors.YELLOW}Aviso Legal:{Colors.RESET}
  {Colors.RED}Esta ferramenta é apenas para fins educacionais.{Colors.RESET}
  O uso indevido para atividades ilegais é de total 
  responsabilidade do usuário.

{Colors.YELLOW}Desenvolvido para:{Colors.RESET} Kali Linux / Python 3
{Colors.YELLOW}Licença:{Colors.RESET} Educacional
""")
            
        elif opcao == "0":
            print(f"\n{Colors.GREEN}[✓] Obrigado por usar o Phone Tracker Simulator!{Colors.RESET}")
            print(f"{Colors.YELLOW}[!] Lembre-se: Use apenas para fins educacionais.{Colors.RESET}\n")
            break
        else:
            print(f"\n{Colors.RED}[✗] Opção inválida! Tente novamente.{Colors.RESET}")

if __name__ == "__main__":
    main()
