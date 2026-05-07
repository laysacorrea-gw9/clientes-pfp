"""
Case Técnico BTG Pactual - Natalia Sabati
Gera PDF profissional para apresentação
"""
from fpdf import FPDF
import os

class CaseBTG(FPDF):
    # Cores
    DARK = (15, 23, 42)
    GOLD = (201, 165, 92)
    WHITE = (255, 255, 255)
    LIGHT_GRAY = (241, 245, 249)
    MID_GRAY = (148, 163, 184)
    DARK_CARD = (30, 41, 59)
    GREEN = (34, 197, 94)
    BLUE = (59, 130, 246)

    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)
        # Register Unicode fonts (Arial from Windows)
        self.add_font('Arial', '', 'C:/Windows/Fonts/arial.ttf', uni=True)
        self.add_font('Arial', 'B', 'C:/Windows/Fonts/arialbd.ttf', uni=True)
        self.add_font('Arial', 'I', 'C:/Windows/Fonts/ariali.ttf', uni=True)

    def header(self):
        if self.page_no() > 1:
            self.set_fill_color(*self.DARK)
            self.rect(0, 0, 210, 12, 'F')
            self.set_font('Arial', 'I', 7)
            self.set_text_color(*self.GOLD)
            self.set_xy(10, 3)
            self.cell(0, 6, 'Case Técnico — Investment Advisor BTG Pactual | Natalia Sabati', 0, 0, 'L')
            self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(*self.MID_GRAY)
        self.cell(0, 10, f'Página {self.page_no()}/{{nb}}', 0, 0, 'C')

    def cover_page(self):
        self.add_page()
        # Background
        self.set_fill_color(*self.DARK)
        self.rect(0, 0, 210, 297, 'F')
        # Gold accent line
        self.set_fill_color(*self.GOLD)
        self.rect(20, 80, 60, 2, 'F')
        # Title
        self.set_font('Arial', 'B', 32)
        self.set_text_color(*self.WHITE)
        self.set_xy(20, 90)
        self.cell(0, 15, 'Case Técnico', 0, 1, 'L')
        self.set_font('Arial', '', 24)
        self.set_text_color(*self.GOLD)
        self.set_xy(20, 108)
        self.cell(0, 12, 'Investment Advisor', 0, 1, 'L')
        self.set_xy(20, 122)
        self.cell(0, 12, 'BTG Pactual', 0, 1, 'L')
        # Subtitle
        self.set_font('Arial', '', 14)
        self.set_text_color(*self.MID_GRAY)
        self.set_xy(20, 145)
        self.cell(0, 10, 'Simulação de Alocação e Wealth Planning', 0, 1, 'L')
        self.set_xy(20, 158)
        self.cell(0, 10, 'Cliente: Médico, 40 anos | R$ 1.000.000', 0, 1, 'L')
        # Author
        self.set_fill_color(*self.GOLD)
        self.rect(20, 230, 60, 1, 'F')
        self.set_font('Arial', 'B', 14)
        self.set_text_color(*self.WHITE)
        self.set_xy(20, 238)
        self.cell(0, 10, 'Natalia Sabati', 0, 1, 'L')
        self.set_font('Arial', '', 11)
        self.set_text_color(*self.MID_GRAY)
        self.set_xy(20, 250)
        self.cell(0, 8, 'Março 2026', 0, 1, 'L')

    def section_title(self, number, title):
        self.ln(5)
        # Gold accent
        self.set_fill_color(*self.GOLD)
        self.rect(10, self.get_y(), 3, 10, 'F')
        self.set_font('Arial', 'B', 16)
        self.set_text_color(*self.DARK)
        self.set_x(18)
        self.cell(0, 10, f'{number}. {title}', 0, 1, 'L')
        self.ln(2)

    def subsection(self, title):
        self.ln(3)
        self.set_font('Arial', 'B', 12)
        self.set_text_color(*self.DARK)
        self.cell(0, 8, title, 0, 1, 'L')
        self.ln(1)

    def body_text(self, text):
        self.set_font('Arial', '', 10)
        self.set_text_color(51, 65, 85)
        self.multi_cell(0, 6, text)
        self.ln(2)

    def bullet(self, text, indent=15):
        self.set_font('Arial', '', 10)
        self.set_text_color(51, 65, 85)
        x = self.get_x()
        self.set_x(indent)
        self.cell(5, 6, chr(8226), 0, 0)
        self.multi_cell(170, 6, text)
        self.ln(1)

    def highlight_box(self, text, color='gold'):
        if color == 'gold':
            bg = (255, 247, 230)
            border_color = self.GOLD
            txt_color = (120, 90, 30)
        elif color == 'blue':
            bg = (235, 245, 255)
            border_color = self.BLUE
            txt_color = (30, 64, 175)
        else:
            bg = (240, 253, 244)
            border_color = self.GREEN
            txt_color = (22, 101, 52)

        y = self.get_y()
        self.set_fill_color(*bg)
        self.set_draw_color(*border_color)
        # Calculate height needed
        self.set_font('Arial', 'B', 10)
        lines = len(text) / 80 + 1
        h = max(12, lines * 7 + 8)
        self.rect(15, y, 180, h, 'FD')
        self.set_fill_color(*border_color)
        self.rect(15, y, 3, h, 'F')
        self.set_text_color(*txt_color)
        self.set_xy(22, y + 3)
        self.multi_cell(168, 6, text)
        self.set_y(y + h + 3)

    def table(self, headers, rows, col_widths=None):
        if col_widths is None:
            col_widths = [180 / len(headers)] * len(headers)

        # Header
        self.set_fill_color(*self.DARK)
        self.set_text_color(*self.WHITE)
        self.set_font('Arial', 'B', 9)
        self.set_x(15)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 8, h, 0, 0, 'C', True)
        self.ln()

        # Rows
        self.set_text_color(51, 65, 85)
        self.set_font('Arial', '', 9)
        for j, row in enumerate(rows):
            if j % 2 == 0:
                self.set_fill_color(*self.LIGHT_GRAY)
            else:
                self.set_fill_color(*self.WHITE)
            self.set_x(15)
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 7, cell, 0, 0, 'C', True)
            self.ln()
        self.ln(3)

    def kpi_cards(self, cards):
        """cards = list of (label, value)"""
        w = 180 / len(cards)
        y = self.get_y()
        for i, (label, value) in enumerate(cards):
            x = 15 + i * w
            self.set_fill_color(*self.LIGHT_GRAY)
            self.rect(x, y, w - 3, 22, 'F')
            self.set_font('Arial', '', 7)
            self.set_text_color(*self.MID_GRAY)
            self.set_xy(x + 3, y + 2)
            self.cell(w - 6, 5, label, 0, 0, 'L')
            self.set_font('Arial', 'B', 12)
            self.set_text_color(*self.DARK)
            self.set_xy(x + 3, y + 9)
            self.cell(w - 6, 8, value, 0, 0, 'L')
        self.set_y(y + 27)


def build():
    pdf = CaseBTG()
    pdf.alias_nb_pages()

    # ===================== CAPA =====================
    pdf.cover_page()

    # ===================== CLIENTE =====================
    pdf.add_page()
    pdf.section_title('1', 'O Cliente')
    pdf.kpi_cards([
        ('Idade', '40 anos'),
        ('Profissão', 'Médico'),
        ('Perfil', 'Moderado'),
        ('Capital', 'R$ 1.000.000'),
    ])
    pdf.bullet('Casado há 3 anos em comunhão total de bens')
    pdf.bullet('Esposa não trabalha — ele é o único provedor da família')
    pdf.bullet('Filho de 1 ano')
    pdf.bullet('Gastou tudo na reforma da casa, voltou a poupar')
    pdf.bullet('R$ 1.000.000 para realocar + aporte mensal de R$ 50.000')
    pdf.bullet('Sem reserva de emergência')
    pdf.bullet('Sem restrição a produto, conhecimento básico de investimentos')
    pdf.bullet('Se preocupa com esposa e gastos futuros do filho')

    # ===================== DIAGNÓSTICO =====================
    pdf.add_page()
    pdf.section_title('2', 'Diagnóstico Inicial — O Dado Faltante')
    pdf.highlight_box('O case não informa o custo de vida do cliente. Sem esse dado, é impossível calcular a reserva de emergência ou dimensionar a proteção patrimonial.', 'gold')
    pdf.ln(3)
    pdf.body_text('Isso não é um descuido — é um teste de capacidade analítica. O advisor precisa construir premissas antes de propor qualquer solução.')

    pdf.subsection('Premissas Adotadas')
    pdf.kpi_cards([
        ('Renda Bruta', 'R$ 150.000/mês'),
        ('Despesa Total', 'R$ 100.000/mês'),
        ('Poupança', 'R$ 50.000/mês'),
    ])
    pdf.bullet('Poupança de R$ 50.000 representa ~30% da renda — compatível com perfil de médico consolidado')
    pdf.bullet('Despesa fixa/essencial: R$ 60.000/mês')
    pdf.bullet('Despesa variável/lazer: R$ 40.000/mês')
    pdf.bullet('Regime de bens: comunhão total — todo patrimônio é compartilhado')
    pdf.bullet('Esposa 100% dependente financeiramente')

    # ===================== RESERVA =====================
    pdf.add_page()
    pdf.section_title('3', 'Reserva de Emergência')
    pdf.highlight_box('Antes de investir qualquer centavo, o cliente precisa de segurança.', 'blue')
    pdf.ln(3)
    pdf.kpi_cards([
        ('Meses', '6'),
        ('Base', 'R$ 60.000/mês'),
        ('Reserva Total', 'R$ 360.000'),
        ('Sobra p/ Investir', 'R$ 640.000'),
    ])
    pdf.bullet('6 meses de despesas fixas (não 12): médico terá DIT como segunda rede de proteção')
    pdf.bullet('Alocação: Tesouro Selic + CDB com liquidez diária')
    pdf.bullet('Capital disponível para carteira: R$ 1.000.000 - R$ 360.000 = R$ 640.000')

    # ===================== PROTEÇÃO DELE =====================
    pdf.add_page()
    pdf.section_title('4', 'Proteção Patrimonial')
    pdf.body_text('O cliente é o único provedor de uma família com esposa dependente e filho de 1 ano em regime de comunhão total. Sem proteção, qualquer imprevisto destrói o planejamento inteiro.')

    pdf.subsection('Seguros do Titular (40 anos, médico)')

    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(*CaseBTG.DARK)
    pdf.cell(0, 7, 'Seguro de Vida — Capital Segurado R$ 12 a 15 milhões', 0, 1)
    pdf.ln(1)
    pdf.bullet('Se ele falece, esposa e filho ficam sem renda. Com comunhão total, ela tem direito a 50% dos bens, mas o patrimônio hoje é pequeno e estará travado em inventário.')
    pdf.bullet('Cálculo por Despesas x Tempo: R$ 60.000 x 12 meses x 21 anos = R$ 15,12 milhões')
    pdf.bullet('Cálculo por Renda Perpétua (4%): R$ 720.000/ano / 4% = R$ 18 milhões')
    pdf.bullet('Capital sugerido: R$ 12-15MM (patrimônio cresce = auto-seguro progressivo)')
    pdf.bullet('Prêmio estimado: R$ 1.000 a 1.200/mês')

    pdf.ln(2)
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(*CaseBTG.DARK)
    pdf.cell(0, 7, 'Invalidez Permanente Total (IPT/IPA)', 0, 1)
    pdf.ln(1)
    pdf.bullet('Se fica inválido: situação PIOR que falecimento — família perde renda e ganha custo adicional')
    pdf.bullet('Capital segurado: R$ 12 a 15 milhões (mesma apólice)')
    pdf.bullet('Prêmio: incluso ou acréscimo de ~R$ 400/mês')

    pdf.ln(2)
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(*CaseBTG.DARK)
    pdf.cell(0, 7, 'DIT — Incapacidade Temporária', 0, 1)
    pdf.ln(1)
    pdf.bullet('Médico tem risco real de afastamento temporário')
    pdf.bullet('Valor diário: R$ 3.000 a 3.500 (60-70% da renda comprovável PJ)')
    pdf.bullet('Carência 15-30 dias coberta pela reserva de emergência')
    pdf.bullet('Prêmio: R$ 300 a 500/mês')

    pdf.ln(3)
    pdf.table(
        ['Cobertura', 'Capital Segurado', 'Prêmio Mensal'],
        [
            ['Vida', 'R$ 12-15 milhões', 'R$ 1.000-1.200'],
            ['Invalidez (IPT)', 'R$ 12-15 milhões', 'Incluso ou +R$ 400'],
            ['DIT', 'R$ 3.500/dia', 'R$ 300-500'],
            ['TOTAL DELE', '', 'R$ 1.700-2.100'],
        ],
        [60, 60, 60]
    )

    # ===================== PROTEÇÃO DELA =====================
    pdf.add_page()
    pdf.subsection('Seguros da Esposa (~37 anos)')

    pdf.highlight_box('Por que segurar quem não tem renda? Porque se ela morre ou fica inválida, ele fica sozinho com filho de 1 ano. Precisa de babá integral, apoio doméstico, e possivelmente reduzir plantões. Custo de substituição: R$ 10.000 a 15.000/mês.', 'gold')
    pdf.ln(3)

    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(*CaseBTG.DARK)
    pdf.cell(0, 7, 'Seguro de Vida — Capital R$ 1,5 a 2 milhões', 0, 1)
    pdf.ln(1)
    pdf.bullet('Cálculo: R$ 10.000/mês x 12 meses x 15 anos = R$ 1,8 milhão')
    pdf.bullet('Prêmio: R$ 150 a 250/mês (mulher, ~37 anos, sem profissão de risco)')

    pdf.ln(2)
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(*CaseBTG.DARK)
    pdf.cell(0, 7, 'Invalidez Permanente — Capital R$ 1,5 a 2 milhões', 0, 1)
    pdf.ln(1)
    pdf.bullet('Se fica inválida: não cuida do filho e gera custo adicional de cuidado dela')
    pdf.bullet('Prêmio: incluso ou acréscimo de ~R$ 100/mês')

    pdf.ln(3)
    pdf.table(
        ['Cobertura', 'Capital Segurado', 'Prêmio Mensal'],
        [
            ['Vida dela', 'R$ 1,5-2 milhões', 'R$ 150-250'],
            ['Invalidez dela', 'R$ 1,5-2 milhões', 'Incluso ou +R$ 100'],
            ['TOTAL DELA', '', 'R$ 250-350'],
        ],
        [60, 60, 60]
    )

    pdf.subsection('Custo Total da Proteção Familiar')
    pdf.table(
        ['Proteção', 'Prêmio Mensal'],
        [
            ['Seguros dele', 'R$ 1.700 a 2.100'],
            ['Seguros dela', 'R$ 250 a 350'],
            ['TOTAL FAMÍLIA', 'R$ 2.000 a 2.450'],
        ],
        [90, 90]
    )
    pdf.highlight_box('Representa ~1,5% da renda bruta — dentro do padrão recomendado de 1% a 3%.', 'green')

    # ===================== TESTAMENTO =====================
    pdf.add_page()
    pdf.section_title('5', 'Testamento')
    pdf.body_text('Com esposa dependente e filho menor de idade, o testamento é urgente.')
    pdf.bullet('Define tutoria legal do filho em caso de falecimento de ambos')
    pdf.bullet('Direciona a parte disponível (50%) conforme vontade do titular')
    pdf.bullet('Evita disputas e protege a família em momento de fragilidade')

    # ===================== VGBL =====================
    pdf.section_title('6', 'Previdência Privada (VGBL)')
    pdf.subsection('Objetivo: Renda passiva de R$ 80.000/mês aos 65 anos')

    pdf.highlight_box('Cálculo reverso: R$ 80.000/mês = R$ 960.000/ano. Pela regra dos 4%, são necessários R$ 24.000.000 aos 65 anos.', 'blue')
    pdf.ln(3)

    pdf.bullet('R$ 1 milhão investido hoje a 8% real por 25 anos = ~R$ 6,85 milhões')
    pdf.bullet('Falta acumular via aportes: ~R$ 17,15 milhões')
    pdf.bullet('Aporte mensal necessário (8% real, 25 anos): R$ 18.000 a 20.000/mês')

    pdf.ln(2)
    pdf.subsection('Proposta: R$ 20.000/mês em VGBL')
    pdf.bullet('VGBL (não PGBL) — médico recebe como PJ, declaração simplificada')
    pdf.bullet('Tabela regressiva: alíquota cai de 35% para 10% em 10 anos')
    pdf.bullet('Fundo multimercado para potencializar retorno no longo prazo')

    pdf.ln(2)
    pdf.subsection('Dupla Função do VGBL')
    pdf.bullet('1. Acumulação para aposentadoria com meta definida de R$ 80.000/mês')
    pdf.bullet('2. Instrumento sucessório — não entra em inventário, família acessa imediatamente para cobrir custos de inventário, ITCMD e despesas correntes')

    # ===================== CENÁRIO MACRO =====================
    pdf.add_page()
    pdf.section_title('7', 'Cenário Macroeconômico (Março 2026)')

    pdf.subsection('Brasil')
    pdf.bullet('Selic a 14,25% ao ano')
    pdf.bullet('IPCA em torno de 5%')
    pdf.bullet('Cenário fiscal desafiador')
    pdf.bullet('Juros reais elevados tornam a renda fixa extremamente atrativa')

    pdf.subsection('Global')
    pdf.bullet('Fed funds em torno de 4,5%')
    pdf.bullet('Dólar forte')
    pdf.bullet('Tensões geopolíticas persistentes')

    pdf.subsection('Impacto na Alocação')
    pdf.highlight_box('Renda fixa pagando IPCA+7% — oportunidade rara. Cautela em renda variável doméstica. Diversificação internacional via BDRs e ETFs globais.', 'gold')

    # ===================== ALOCAÇÃO =====================
    pdf.add_page()
    pdf.section_title('8', 'Alocação da Carteira (R$ 640.000)')

    pdf.table(
        ['Classe', '%', 'Valor', 'Ativos Sugeridos'],
        [
            ['Renda Fixa', '45%', 'R$ 288.000', 'Tesouro IPCA+, CDB, LCI/LCA, Debêntures'],
            ['Fundos Multimercado', '15%', 'R$ 96.000', 'Fundos macro e crédito privado'],
            ['Renda Variável', '15%', 'R$ 96.000', 'Dividendos, ETFs, BDRs'],
            ['FIIs', '13%', 'R$ 83.000', 'Logística, recebíveis, híbridos'],
            ['Alternativos', '7%', 'R$ 45.000', 'Crédito estrut., infra, private equity'],
            ['Previdência VGBL', '5%', 'R$ 32.000', 'VGBL multimercado'],
        ],
        [40, 15, 35, 90]
    )

    # ===================== APORTES =====================
    pdf.section_title('9', 'Aportes Mensais — R$ 50.000/mês')

    pdf.table(
        ['Destino', 'Valor Mensal', '% do Aporte'],
        [
            ['VGBL (aposentadoria)', 'R$ 20.000', '40%'],
            ['Renda Fixa', 'R$ 12.000', '24%'],
            ['Fundos Multimercado', 'R$ 5.000', '10%'],
            ['Renda Variável', 'R$ 5.000', '10%'],
            ['FIIs', 'R$ 5.000', '10%'],
            ['Alternativos', 'R$ 3.000', '6%'],
        ],
        [60, 60, 60]
    )
    pdf.bullet('Rebalanceamento trimestral para manter os percentuais alvo')

    # ===================== PROJEÇÃO =====================
    pdf.add_page()
    pdf.section_title('10', 'Projeção Patrimonial')
    pdf.body_text('Com aportes de R$ 50.000/mês, valores em poder de compra atual (descontada inflação):')

    pdf.table(
        ['Cenário', 'Em 10 anos (50 anos)', 'Em 25 anos (65 anos)'],
        [
            ['Conservador (8% real)', '~R$ 10 milhões', '~R$ 24 milhões'],
            ['Moderado (10% real)', '~R$ 12 milhões', '~R$ 34 milhões'],
            ['Otimista (12% real)', '~R$ 14 milhões', '~R$ 48 milhões'],
        ],
        [60, 60, 60]
    )

    pdf.highlight_box('No cenário conservador, o cliente atinge a meta de R$ 80.000/mês de renda passiva aos 65 anos.', 'green')

    # ===================== HOLDING =====================
    pdf.ln(5)
    pdf.section_title('11', 'Visão de Futuro — Holding Familiar')
    pdf.body_text('Quando o patrimônio atingir R$ 3 a 5 milhões, avaliar a constituição de uma holding familiar:')
    pdf.bullet('Otimização tributária sobre rendimentos de aluguel e investimentos')
    pdf.bullet('Planejamento sucessório estruturado')
    pdf.bullet('Proteção patrimonial contra riscos profissionais (médico tem exposição a processos)')
    pdf.ln(2)
    pdf.body_text('Não é prioridade imediata, mas faz parte do planejamento de longo prazo de um cliente com esse perfil de acumulação.')

    # ===================== PRÓXIMOS PASSOS =====================
    pdf.add_page()
    pdf.section_title('12', 'Próximos Passos')

    steps = [
        'Abrir conta e transferir os R$ 1.000.000',
        'Montar reserva de emergência (R$ 360.000) no mesmo dia',
        'Contratar seguros de vida e invalidez para ambos na primeira semana',
        'Agendar reunião com advogado para testamento',
        'Iniciar VGBL com aporte inicial de R$ 32.000',
        'Montar carteira com os R$ 640.000 restantes',
        'Configurar débito automático dos R$ 50.000 mensais',
        'Primeira revisão de carteira em 90 dias',
        'Avaliar holding familiar quando patrimônio atingir R$ 3 milhões',
    ]

    for i, step in enumerate(steps, 1):
        y = pdf.get_y()
        # Number circle
        pdf.set_fill_color(*CaseBTG.GOLD)
        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(*CaseBTG.WHITE)
        pdf.set_xy(18, y)
        pdf.cell(8, 8, str(i), 0, 0, 'C', True)
        # Text
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(51, 65, 85)
        pdf.set_xy(30, y)
        pdf.cell(0, 8, step, 0, 1, 'L')
        pdf.ln(2)

    # ===================== ENCERRAMENTO =====================
    pdf.ln(10)
    pdf.set_fill_color(*CaseBTG.GOLD)
    pdf.rect(15, pdf.get_y(), 180, 1, 'F')
    pdf.ln(8)
    pdf.set_font('Arial', 'I', 10)
    pdf.set_text_color(*CaseBTG.MID_GRAY)
    pdf.cell(0, 8, 'Material preparado para fins de simulação — Case Técnico BTG Pactual', 0, 1, 'C')
    pdf.cell(0, 8, 'Natalia Sabati | Março 2026', 0, 1, 'C')

    # Save
    output_path = os.path.join(os.path.dirname(__file__), 'Case_BTG_Natalia_Sabati.pdf')
    pdf.output(output_path)
    print(f'PDF gerado: {output_path}')
    return output_path

if __name__ == '__main__':
    build()