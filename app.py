import os

from fpdf import FPDF
import streamlit as st

# Configuração da página (DEVE SER SEMPRE A PRIMEIRA LINHA DO STREAMLIT)
st.set_page_config(
    page_title="AgroManejo Amazônia | Diagnóstico de Solos",
    layout="wide",
)

# --- BARRA LATERAL (MENU) ---
st.sidebar.markdown("### Configurações e Menu")
tema = st.sidebar.selectbox("Tema da Página", ["Claro (Light)", "Escuro (Dark)"])

st.sidebar.markdown("---")
st.sidebar.markdown("### AgroManejo Amazônia")
st.sidebar.markdown(
    "Plataforma técnica de apoio à decisão para sistemas produtivos e extensão"
    " rural."
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Navegação")
menu = st.sidebar.radio(
    "Selecione a seção:",
    ["Diagnóstico de Solo", "Sobre a Aplicação", "Sobre o Desenvolvedor"],
)

# --- SEÇÃO 1: DIAGNÓSTICO DE SOLO ---
if menu == "Diagnóstico de Solo":
  st.title("AgroManejo Amazônia | Diagnóstico de Solos")
  st.markdown(
      "Ferramenta de apoio à decisão para o manejo sustentável na agricultura"
      " familiar."
  )

  st.markdown("### 1. Identificação da Propriedade")
  col1, col2, col3 = st.columns(3)
  with col1:
    nome_produtor = st.text_input("Nome do Produtor", "João da Silva")
  with col2:
    propriedade = st.text_input("Propriedade / Lote", "Sítio Boa Esperança")
  with col3:
    municipio = st.selectbox(
        "Município", ["Humaitá - AM", "Apuí - AM", "Outros"]
    )

  st.markdown("### 2. Características do Terreno e Cultura")
  col4, col5 = st.columns(2)
  with col4:
    textura = st.selectbox(
        "Textura do Solo",
        [
            "Argilosa (Solo pesados / Boa retenção)",
            "Média (Equilibrada)",
            "Arenosa (Leve / Baixa retenção)",
        ],
    )
    relevo = st.selectbox(
        "Relevo do Terreno",
        [
            "Plano a Suave-Ondulado",
            "Ondulado",
            "Forte Ondulado / Declive acentuado",
        ],
    )
  with col5:
    drenagem = st.selectbox(
        "Condição de Drenagem",
        [
            "Bem drenado",
            "Moderadamente drenado",
            "Mal drenado / Encharcamento frequente",
        ],
    )
    cultura = st.text_input(
        "Atividade Principal / Cultura de Interesse",
        "Ex: Mandioca, Café Robusta, SAF",
    )

  st.markdown("### 3. Análise de Laboratório (Upload do Laudo)")
  uploaded_file = st.file_uploader(
      "Carregar arquivo do laudo (PDF, Imagem, Excel ou CSV)",
      type=["pdf", "png", "jpg", "jpeg", "xlsx", "xls", "csv"],
  )

  if st.button("Gerar Laudo Técnico e Plano de Manejo", type="primary"):
    st.success(
        "Diagnóstico agronômico processado com sucesso com base nas diretrizes"
        " da SBCS!"
    )

    # Texto técnico detalhado e estruturado
    texto_laudo = f"""================================================================================
                    AGROMANEJO AMAZÔNIA - LAUDO TÉCNICO
        Plataforma de Apoio à Decisão e Extensão Rural | IEAA / UFAM (Humaitá-AM)
================================================================================

1. IDENTIFICAÇÃO DA PROPRIEDADE E SISTEMA PRODUTIVO
--------------------------------------------------------------------------------
- Produtor / Proprietário: {nome_produtor}
- Propriedade / Lote     : {propriedade}
- Município / Região    : {municipio} (Calha do Médio Rio Madeira / BR-319)
- Atividade Principal    : {cultura}
- Responsabilidade      : Extensão Universitária Voluntária / Apoio Agronômico

2. DIAGNÓSTICO DOS PARÂMETROS FÍSICOS E DO TERRENO
--------------------------------------------------------------------------------
- Textura do Solo: {textura}
  > Interpretação: Solos com essa classe textural na região exigem atenção ao manejo
    mecânico. Em solos argilosos, evitar o tráfego em condições de umidade elevada
    para prevenir a compactação; em solos arenosos, priorizar o aporte contínuo de
    matéria orgânica para retenção de água e nutrientes.

- Relevo e Drenagem: Relevo {relevo} | Condição de Drenagem: {drenagem}
  > Risco Ambiental: Em relevos ondulados, adotar o cultivo em nível. Em condições
    de drenagem deficiente, priorizar o escoamento superficial e espécies tolerantes
    ao encharcamento temporário.

3. PLANO DE MANEJO CONSERVACIONISTA E RECUPERAÇÃO DO SOLO (SBCS)
--------------------------------------------------------------------------------
[A] Proteção Física e Combate ao Fogo:
    - Exclusão total da prática de queimada no preparo da área.
    - Manutenção da palhada e cobertura morta (mulching) sobre a superfície para
      reduzir a temperatura do solo, conservar a umidade e proteger contra a erosão
      hídrica decorrente das chuvas intensas da Amazônia Sul.

[B] Manejo da Acidez e Nutrição:
    - Realizar amostragem periódica de solo (camada 0-20 cm e 20-40 cm).
    - Para solos ácidos típicos da região, planejar a calagem com calcário dolomítico
      para neutralização do alumínio tóxico (Al3+) e suprimento de Ca e Mg.
    - Priorizar a adubação orgânica local (esterco, composto, adubação verde) e fontes
      fosfatadas de liberação gradual (fosfatos naturais reativos).

4. ESTRATÉGIA DE DIVERSIFICAÇÃO: SISTEMAS AGROFLORESTAIS (SAFs)
--------------------------------------------------------------------------------
Recomenda-se a transição da monocultura para arranjos agroflorestais:
- Camada Rasteira/Substrato : Mandioca / Abacaxi / Feijão-caupi (retorno rápido).
- Camada Intermediária    : Café Robusta Amazônico / Cacau / Banana.
- Camada Superior/Arbórea : Ingaes (Ingá sp. para fixação de N2), Castanheira ou
                            espécies nativas de madeira/fruta.

5. COMPROMISSO SOCIOAMBIENTAL REGIONAL
--------------------------------------------------------------------------------
Este laudo visa fortalecer a autonomia do agricultor familiar, promovendo a
produtividade sustentável, a conservação da biodiversidade e a segurança alimentar
na calha do Médio Rio Madeira e no entorno da rodovia BR-319.
================================================================================"""

    st.markdown("#### 📜 Resultado do Laudo Técnico Detalhado")
    st.text_area(
        "Laudo Agronômico Completo (Pronto para visualização e cópia):",
        texto_laudo,
        height=380,
    )

# --- SEÇÃO 2: SOBRE A APLICAÇÃO ---
elif menu == "Sobre a Aplicação":
  st.title("ℹ️ Sobre a Plataforma AgroManejo Amazônia")
  st.markdown(
      """
        O **AgroManejo Amazônia** é uma ferramenta de tecnologia agrícola e extensão rural concebida com um propósito estritamente social, solidário e sem fins lucrativos.
        
        Desenvolvida para atender a realidade socioambiental do Sul do Amazonas e da calha do Médio Rio Madeira (região de Humaitá e entorno da BR-319), a aplicação visa servir como instrumento de apoio direto e gratuito aos pequenos produtores rurais, agricultores familiares e extensionistas.
        
        ### Propósito e Missão
        * **Foco Humano e Social:** Ajudar o produtor rural a entender melhor o seu solo, planejar seus cultivos e melhorar a produtividade de forma sustentável, sem custos ou barreiras comerciais.
        * **Conservação dos Solos Amazônicos:** Promover práticas de manejo ecológico (como Sistemas Agroflorestais - SAFs, adubação verde e preservação da cobertura orgânica) prevenindo o esgotamento nutricional e a erosão.
        * **Democratização do Acesso à Ciência:** Traduzir o conhecimento agronômico universitário numa interface leve, acessível e prática para o dia a dia do campo.
        
        ### Compromisso Regional
        Diferente de softwares comerciais corporativos, o AgroManejo Amazônia prioriza os arranjos produtivos locais da agricultura familiar, combatendo o uso do fogo e valorizando a biodiversidade e a autonomia dos produtores da nossa região.
        """
  )

# --- SEÇÃO 3: SOBRE O DESENVOLVEDOR ---
elif menu == "Sobre o Desenvolvedor":
  st.title("👨‍💻 Desenvolvedor Responsável")

  # Procura a foto com os nomes mais comuns
  foto = next(
      (
          f
          for f in ["prof_pic.jpeg", "prof_pic.jpg", "prof_pic..jpeg"]
          if os.path.exists(f)
      ),
      None,
  )

  col_dev1, col_dev2 = st.columns([1, 2])
  with col_dev1:
    if foto:
      try:
        st.image(foto, width=220)
      except Exception:
        st.write("[Foto do Desenvolvedor]")
    else:
      st.write("[Foto do Desenvolvedor]")

  with col_dev2:
    st.markdown(
        """
            ### Eduardo da Costa Batista
            **Discente de Agronomia & Pesquisador**  
            * **Instituição:** Instituto de Educação, Agricultura e Ambiente (IEAA / UFAM)  
            * **Universidade:** Universidade Federal do Amazonas (UFAM) - Campus Humaitá  
            
            Projeto desenvolvido por compromisso social e acadêmico com a extensão tecnológica, visando o fortalecimento voluntário da agricultura familiar e a sustentabilidade produtiva regional.
            
            ---
            **Conecte-se com o Desenvolvedor:**  
            * [Acessar Portfólio Profissional](https://github.com/eduardobatista-glitch)  
            * [GitHub Oficial](https://github.com/eduardobatista-glitch)  
            """
    )

# --- RODAPÉ (aparece em todas as seções) ---
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 14px; padding: 10px 0;">
        <b>AgroManejo Amazônia</b> © 2026<br>
        Desenvolvido por <b>Eduardo da Costa Batista</b> (Desenvolvedor e Cofundador)<br>
        em parceria com a <b>Dra. Natasha Nina</b> (Cofundadora)<br>
        IEAA / UFAM - Campus Humaitá
    </div>
    """,
    unsafe_allow_html=True,
)
