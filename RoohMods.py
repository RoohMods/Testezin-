import PySimpleGUI as sg

def criar_menu():
    menu_def = [
        ['Curso de Programação', ['Como é Esse Curso de Programação?','Quem é o Professor de Programação?']],
        ['CVTI', ['O que é CVTI?']],
        ['MEI',['O que é MEI?']],
        ['Imposto de Renda',['O que é Imposto de Renda?']],
        ['Renda Bruta',['O que é Renda Bruta?']],
        ['Despesas',['O que é Despesas?']],
        ['Isenção',['O que é Isenção?']],
        ['Renda Tributavel',['O que é Renda Tributavel?']],
    ]
    return menu_def



sg.theme('DarkBrown4')

def telaapresentacao():
        
        layout = [
        [sg.MenuBar(criar_menu())],    
        [sg.Frame(" Projeto da Turma de Programação, Segundas e Quartas das 14h ás 16h ",font = ('Helvetica', 12), layout=[
        [sg.Text('''
O projeto a seguir foi criado pela turma de Programação sob a Orientação do Professor João para o evento do CVTI Innovation Day,
O Projeto foi idealizado sob a ajuda ao MEI, o Microempreendedor Individual.
Para auxiliá-lo a declarar ao Imposto de Renda caso ele tenha um ganho acima de R$: 28559.70.
        ''', font = ('Helvetica', 16))],
        [sg.Button('Iniciar O Projeto')]
    ] ,border_width=5)]
        ]
        window = sg.Window('Apresentação do Projeto', layout)
        while True:
            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Cancel'):
                break
            elif event in 'Como é Esse Curso de Programação?':
                sg.popup('O Curso ensina os fundamentos da programação e ensina a criar programas em Python',font = ('Helvetica', 12))
            elif event in 'Quem é o Professor de Programação?':
                sg.popup('O Professor do Curso de Programação e o Professor João, quem também é Professor de Robotica',font = ('Helvetica', 12))
            elif event in 'O que é CVTI?':
                sg.popup('''
Centro Vocacional de Tecnologia e Inovação
Um projeto da Prefeitura de Nova Iguaçu em Parceria com o Governo Federal
                         ''',font = ('Helvetica', 12))
            elif event in 'O que é MEI?':
                sg.popup('''
O Microempreendedor Individual (MEI) é uma figura jurídica do Brasil, é a pessoa que trabalha por conta própria e que se legaliza 
como pequeno empresário, para ser um microempreendedor individual, Poderá ter um faturamento anual de até R$ 81000.00 e não ter participação em outra empresa como sócio ou titular, 
o MEI também pode ter um empregado contratado que receba um salário mínimo ou o piso da categoria.
                        ''',font = ('Helvetica', 12))
            elif event in 'O que é Imposto de Renda?':
                sg.popup('''
O Imposto de Renda é um tributo cobrado anualmente pelo Governo Federal sobre os ganhos de pessoas e de empresas.
Ele é pago conforme os rendimentos declarados, de forma que os cidadãos com renda maior pagam mais impostos.
Pessoas físicas que ganham até R$28559.70 não precisa declarar e serão Isentas do tributo.
                         ''',font = ('Helvetica', 12))
            elif event in 'O que é Renda Bruta?':
                sg.popup('''
Renda bruta é o total de ganhos ou receitas obtidas por uma pessoa, empresa ou organização 
antes da dedução de qualquer imposto, tributo ou despesas.
                        ''',font = ('Helvetica', 12))
            elif event in 'O que é Despesas?':
                sg.popup('''
As despesas são recursos aplicados à estrutura gerencial de uma empresa, com o objetivo de sustentar seu funcionamento
como um todo. Em outras palavras, podemos dizer que elas estão relacionadas à administração do negócio. Pode ser Dividida em:
-Despesas Fixas
As despesas fixas correspondem a gastos mensais fixos, como o nome indica. 
Elas são constantes e, em muitos casos, previsíveis, pois não estão vinculadas às oscilações no volume de produção.
-Despesas Variáveis
Já as variáveis são aquelas que estão relacionadas ao volume de produção e, por isso, os valores oscilam de um período para outro.
-Despesas Operacionais
As operacionais são aquelas despesas fundamentais para manter o funcionamento da empresa
-Despesas Não Operacionais
As não operacionais são aquelas que não estão ligadas diretamente ao funcionamento ou à realização da atividade principal da empresa.
Alguns exemplos são o pagamento de juros e dividendos.
-Despesas Pré-Operacionais
Já as pré-operacionais são essenciais para que a empresa tenha condições de realizar suas atividades e expandir seus processos.
Elas são pagas antes do início da produção e são inevitáveis para a implementação do negócio.
                        ''',font = ('Helvetica', 12))
            elif event in 'O que é Isenção?':
                sg.popup('''
Isenção de taxas é a dispensa do pagamento de valores cobrados sobre determinados serviços.
Essa isenção é uma prerrogativa que na maioria das vezes requer o cumprimento de algumas exigências, como no Caso do MEI onde
ocorre pela ocupação que está Habilitado.Que no caso são:
-Comercio, Industria e Transporte de Carga que recebe 8 porcento de Isenção
-Transporte de Passageiros que recebe 16 porcento de Isenção
-Serviços em Geral que recebe 32 porcento de Isenção
                        ''',font = ('Helvetica', 12))
            elif event in 'O que é Renda Tributavel?':
                sg.popup('Um rendimento tributável é aquele que está sujeito à cobrança de Imposto de Renda.',font = ('Helvetica', 12))
            elif event in '':
                sg.popup('')
            elif event in '':
                sg.popup('')
            elif event in '':
                sg.popup('')
            elif event in ('Iniciar O Projeto'):
                window.close()
                tema1 = sg.theme('DarkGrey15')
                tela1(tema1)
                break
        window.close()

def tela1(tema1):
    layout = [
        [sg.Frame(" Tela de Declaração de Renda ",font = ('Helvetica', 14), layout=[
        [sg.Text('Digite a Renda Bruta para ser Testado: R$', font = ('Helvetica', 16)), sg.InputText()],
        [sg.Button('Prosseguir ➡')]
    ] ,border_width=5)]
        
        
]

    window = sg.Window('Teste 1 de 4',layout)

    while True:
        event, values = window.read()

        try:
            if event in ('Prosseguir ➡'):
                if float(values[0]) <= 28559.70:
                    sg.popup('O Valor Inserido não deve ser declarado, pois o imposto de renda deve ser maior que 28559.70', font=('Helvetica', 15))
                elif float(values[0]) > 81000:
                    sg.popup('O Valor Inserido é Superior ao Limite em que o MEI pode ter, você deve migrar para MicroEmpresa', font=('Helvetica', 14))
                elif float(values[0]) > 0:
                    RendaBruta = values[0]
                    window.close()
                    tema2 = sg.theme('DarkPurple4')
                    tela2(tema2,RendaBruta)
                    break
            elif event in (sg.WIN_CLOSED):
                break
        except ValueError:
            continue
    window.close()
def tela2(tema2,RendaBruta):
    layout = [
        [sg.Frame(" Tela de Declaração de Despesa ", font = ('Helvetica', 14) ,layout=[       
        [sg.Text('Digite o valor das Despesas Feitas pelo MEI: R$',font = ('Helvetica', 16)), sg.InputText()],
        [sg.Button('Prosseguir ➡')]
    ] ,border_width=5)]
]

    window = sg.Window('Tela 2 de 4', layout)

    while True:
        event, values = window.read()

        try:
            if event in ('Prosseguir ➡'):
                if float(values[0]) <= (float(RendaBruta) * 0.8):
                    Despesa = float(values[0]) 
                    DespesaRenda = float(RendaBruta) - float(Despesa)
                    window.close()
                    tela3(RendaBruta,DespesaRenda)
                    break
                elif float(values[0]) > (float(RendaBruta) * 0.8):
                    sg.popup('O Valor Inserido é Superior ao Limite em que o MEI pode ter, você deve migrar para MicroEmpresa', font=('Helvetica', 16))
                elif event in (sg.WIN_CLOSED):
                    break
        except ValueError:
            continue    
    window.close()

def tela3(RendaBruta,DespesaRenda):
    layout = [
            [sg.Frame(" Tela de Declaração de Ocupação do MEI ", font = ('Helvetica', 14) ,layout=[       
            [sg.Text('Indique qual é a sua ocupação para receber isenção: ', font = ('Helvetica', 16)),sg.OptionMenu(['Comércio','Transporte','Serviços em Geral'], k = 'Escolha')],
            [sg.Button('Prosseguir ➡')]
            ], border_width=5)]
            ]


    window = sg.Window('Tela 3 de 4', layout)

    while True:
        event, values = window.read()

        try:
            if event in ('Prosseguir ➡'):
             if values['Escolha'] in 'Comércio':
                isencao = float(RendaBruta) * 0.08
                RendaTributavel = float(DespesaRenda) - float(isencao)
                window.close()
                tela4(RendaTributavel,isencao)
                break
             elif values['Escolha'] in 'Transporte':
                isencao = float(RendaBruta) * 0.16
                RendaTributavel = float(DespesaRenda) - float(isencao)
                window.close()
                tela4(RendaTributavel,isencao)
                break
             elif values['Escolha'] in 'Serviços em Geral':
                isencao = float(RendaBruta) * 0.32
                RendaTributavel = float(DespesaRenda) - float(isencao)
                window.close()
                tela4(RendaTributavel,isencao)
                break
             elif event in (sg.WIN_CLOSED):
                    break
        except ValueError:
            continue
    window.close()

def tela4(RendaTributavel,isencao):
    texto = 'Você deve declarar esse valor, porém Não PRECISARÁ PAGAR NADA, já que é menor de R$: 28559.70' if RendaTributavel <= 28559.70 else 'Você terá que pagar a Receita Federal, quando fizer a Declaração Escolha a Opção Alíquota Simples'
    layout = [
            [sg.Frame(" Tela de Demonstração da Renda Tributavél ", font = ('Helvetica', 14),layout=[       
            [sg.Text(f'Sua Renda tributavél é R$: {RendaTributavel:2}', font = ('Helvetica', 16))],
            [sg.Text(texto, font = ('Helvetica', 16))],
            [sg.Text(f'Sua Isenção é R$: {isencao:2}',font = ('Helvetica', 16))]
            ], border_width=5)]
            ]
    window = sg.Window('Tela 4 de 4, Conclusão', layout,grab_anywhere=True)

    while True:
        event = window.read()[0]

        if event == sg.WIN_CLOSED:
            break
    window.close()

telaapresentacao()
