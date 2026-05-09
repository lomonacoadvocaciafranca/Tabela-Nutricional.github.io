import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Gerador de Tabela Nutricional", layout="centered")

# --- INICIALIZAÇÃO DO BANCO DE DADOS NA SESSÃO ---
if "banco_categorias" not in st.session_state:
    st.session_state.banco_categorias = {
        "🥩 Proteínas": {
            "Frango (Peito, sem pele)": {"kj": 690, "kcal": 165, "fat": 3.6, "sat": 1.0, "carb": 0.0, "sugar": 0.0,
                                         "prot": 31.0, "salt": 0.18, "unidade": "g"},
            "Carne Bovina (Patinho)": {"kj": 556, "kcal": 133, "fat": 4.5, "sat": 1.5, "carb": 0.0, "sugar": 0.0,
                                       "prot": 21.6, "salt": 0.15, "unidade": "g"},
            "Ovo (Inteiro)": {"kj": 595, "kcal": 143, "fat": 9.5, "sat": 3.1, "carb": 0.7, "sugar": 0.4, "prot": 12.6,
                              "salt": 0.35, "unidade": "unid", "peso_unid": 50},
            "Salmão (Cru)": {"kj": 862, "kcal": 206, "fat": 13.0, "sat": 3.1, "carb": 0.0, "sugar": 0.0, "prot": 22.0,
                             "salt": 0.15, "unidade": "g"},
            "Soja (Grão Cozido)": {"kj": 724, "kcal": 173, "fat": 9.0, "sat": 1.3, "carb": 9.9, "sugar": 3.0,
                                   "prot": 16.6, "salt": 0.01, "unidade": "g"},
            "Lombo Suíno (Assado)": {"kj": 598, "kcal": 143, "fat": 3.5, "sat": 1.2, "carb": 0.0, "sugar": 0.0,
                                     "prot": 26.0, "salt": 0.13, "unidade": "g"},
            "Tilápia (Filé Cru)": {"kj": 401, "kcal": 96, "fat": 1.7, "sat": 0.6, "carb": 0.0, "sugar": 0.0,
                                   "prot": 20.0, "salt": 0.10, "unidade": "g"},
            "Atum (Enlatado em Água)": {"kj": 485, "kcal": 116, "fat": 0.8, "sat": 0.2, "carb": 0.0, "sugar": 0.0,
                                        "prot": 25.5, "salt": 0.80, "unidade": "g"},
            "Camarão (Cozido)": {"kj": 414, "kcal": 99, "fat": 0.3, "sat": 0.1, "carb": 0.2, "sugar": 0.0, "prot": 24.0,
                                 "salt": 1.00, "unidade": "g"},
            "Queijo Cottage": {"kj": 410, "kcal": 98, "fat": 4.3, "sat": 1.7, "carb": 3.4, "sugar": 2.7, "prot": 11.0,
                               "salt": 0.80, "unidade": "g"}
        },
        "🍚 Carboidratos": {
            "Arroz Branco (Cozido)": {"kj": 544, "kcal": 130, "fat": 0.3, "sat": 0.1, "carb": 28.0, "sugar": 0.1,
                                      "prot": 2.7, "salt": 0.01, "unidade": "g"},
            "Arroz Integral (Cozido)": {"kj": 460, "kcal": 110, "fat": 0.9, "sat": 0.2, "carb": 22.8, "sugar": 0.3,
                                        "prot": 2.6, "salt": 0.01, "unidade": "g"},
            "Batata Doce (Cozida)": {"kj": 360, "kcal": 86, "fat": 0.1, "sat": 0.0, "carb": 20.1, "sugar": 4.2,
                                     "prot": 1.6, "salt": 0.14, "unidade": "g"},
            "Batata Inglesa (Cozida)": {"kj": 364, "kcal": 87, "fat": 0.1, "sat": 0.0, "carb": 20.1, "sugar": 0.9,
                                        "prot": 1.9, "salt": 0.01, "unidade": "g"},
            "Macarrão (Cozido)": {"kj": 661, "kcal": 158, "fat": 0.9, "sat": 0.2, "carb": 31.0, "sugar": 0.6,
                                  "prot": 5.8, "salt": 0.01, "unidade": "g"},
            "Mandioca (Cozida)": {"kj": 470, "kcal": 112, "fat": 0.3, "sat": 0.1, "carb": 26.9, "sugar": 1.7,
                                  "prot": 1.4, "salt": 0.03, "unidade": "g"},
            "Pão Francês": {"kj": 1251, "kcal": 299, "fat": 3.1, "sat": 0.6, "carb": 58.0, "sugar": 3.5, "prot": 9.3,
                            "salt": 1.20, "unidade": "unid", "peso_unid": 50},
            "Goma de Tapioca": {"kj": 1447, "kcal": 346, "fat": 0.0, "sat": 0.0, "carb": 86.0, "sugar": 0.0,
                                "prot": 0.0, "salt": 0.01, "unidade": "g"},
            "Milho Verde (Enlatado)": {"kj": 343, "kcal": 82, "fat": 1.2, "sat": 0.2, "carb": 14.3, "sugar": 4.5,
                                       "prot": 2.6, "salt": 0.60, "unidade": "g"},
            "Quinoa (Cozida)": {"kj": 502, "kcal": 120, "fat": 1.9, "sat": 0.2, "carb": 21.3, "sugar": 0.9, "prot": 4.4,
                                "salt": 0.02, "unidade": "g"}
        },
        "🌾 Fibras e Grãos": {
            "Aveia em Flocos": {"kj": 1625, "kcal": 389, "fat": 6.9, "sat": 1.2, "carb": 66.3, "sugar": 0.0,
                                "prot": 16.9, "salt": 0.01, "unidade": "g"},
            "Semente de Chia": {"kj": 2034, "kcal": 486, "fat": 30.7, "sat": 3.3, "carb": 42.1, "sugar": 0.0,
                                "prot": 16.5, "salt": 0.04, "unidade": "g"},
            "Linhaça": {"kj": 2234, "kcal": 534, "fat": 42.2, "sat": 3.7, "carb": 28.9, "sugar": 1.5, "prot": 18.3,
                        "salt": 0.07, "unidade": "g"},
            "Semente de Abóbora": {"kj": 2397, "kcal": 574, "fat": 49.0, "sat": 8.5, "carb": 14.7, "sugar": 1.3,
                                   "prot": 29.8, "salt": 0.04, "unidade": "g"},
            "Semente de Girassol": {"kj": 2443, "kcal": 584, "fat": 51.5, "sat": 4.5, "carb": 20.0, "sugar": 2.6,
                                    "prot": 20.8, "salt": 0.02, "unidade": "g"},
            "Grão de Bico (Cozido)": {"kj": 686, "kcal": 164, "fat": 2.6, "sat": 0.3, "carb": 27.4, "sugar": 4.8,
                                      "prot": 8.9, "salt": 0.02, "unidade": "g"},
            "Lentilha (Cozida)": {"kj": 485, "kcal": 116, "fat": 0.4, "sat": 0.1, "carb": 20.1, "sugar": 1.8,
                                  "prot": 9.0, "salt": 0.01, "unidade": "g"},
            "Feijão Carioca (Cozido)": {"kj": 318, "kcal": 76, "fat": 0.5, "sat": 0.1, "carb": 13.6, "sugar": 0.0,
                                        "prot": 4.8, "salt": 0.01, "unidade": "g"},
            "Feijão Preto (Cozido)": {"kj": 381, "kcal": 91, "fat": 0.5, "sat": 0.1, "carb": 16.3, "sugar": 0.3,
                                      "prot": 6.0, "salt": 0.01, "unidade": "g"},
            "Ervilha (Cozida)": {"kj": 343, "kcal": 82, "fat": 0.4, "sat": 0.1, "carb": 14.8, "sugar": 5.4, "prot": 5.4,
                                 "salt": 0.01, "unidade": "g"}
        },
        "🥦 Legumes e Verduras": {
            "Brócolis (Cozido)": {"kj": 146, "kcal": 35, "fat": 0.4, "sat": 0.1, "carb": 7.2, "sugar": 1.4, "prot": 2.4,
                                  "salt": 0.04, "unidade": "g"},
            "Cenoura (Crua)": {"kj": 173, "kcal": 41, "fat": 0.2, "sat": 0.0, "carb": 9.6, "sugar": 4.7, "prot": 0.9,
                               "salt": 0.17, "unidade": "unid", "peso_unid": 120},
            "Alface": {"kj": 63, "kcal": 15, "fat": 0.2, "sat": 0.0, "carb": 2.9, "sugar": 0.8, "prot": 1.4,
                       "salt": 0.07, "unidade": "g"},
            "Tomate": {"kj": 75, "kcal": 18, "fat": 0.2, "sat": 0.0, "carb": 3.9, "sugar": 2.6, "prot": 0.9,
                       "salt": 0.01, "unidade": "unid", "peso_unid": 100},
            "Abobrinha (Cozida)": {"kj": 63, "kcal": 15, "fat": 0.3, "sat": 0.1, "carb": 2.7, "sugar": 1.7, "prot": 1.1,
                                   "salt": 0.01, "unidade": "g"},
            "Espinafre (Cru)": {"kj": 96, "kcal": 23, "fat": 0.4, "sat": 0.1, "carb": 3.6, "sugar": 0.4, "prot": 2.9,
                                "salt": 0.20, "unidade": "g"},
            "Couve-flor (Cozida)": {"kj": 96, "kcal": 23, "fat": 0.5, "sat": 0.1, "carb": 4.1, "sugar": 2.1,
                                    "prot": 1.8, "salt": 0.04, "unidade": "g"},
            "Cebola (Crua)": {"kj": 167, "kcal": 40, "fat": 0.1, "sat": 0.0, "carb": 9.3, "sugar": 4.2, "prot": 1.1,
                              "salt": 0.01, "unidade": "unid", "peso_unid": 100},
            "Alho (Cru)": {"kj": 623, "kcal": 149, "fat": 0.5, "sat": 0.1, "carb": 33.1, "sugar": 1.0, "prot": 6.4,
                           "salt": 0.04, "unidade": "g"},
            "Pimentão Vermelho": {"kj": 109, "kcal": 26, "fat": 0.3, "sat": 0.0, "carb": 6.0, "sugar": 4.2, "prot": 1.0,
                                  "salt": 0.01, "unidade": "unid", "peso_unid": 150}
        },
        "🍎 Frutas": {
            "Maçã (com casca)": {"kj": 218, "kcal": 52, "fat": 0.2, "sat": 0.0, "carb": 13.8, "sugar": 10.4,
                                 "prot": 0.3, "salt": 0.0, "unidade": "unid", "peso_unid": 150},
            "Banana (Prata)": {"kj": 372, "kcal": 89, "fat": 0.3, "sat": 0.1, "carb": 22.8, "sugar": 12.2, "prot": 1.1,
                               "salt": 0.0, "unidade": "unid", "peso_unid": 100},
            "Morango": {"kj": 134, "kcal": 32, "fat": 0.3, "sat": 0.0, "carb": 7.7, "sugar": 4.9, "prot": 0.7,
                        "salt": 0.0, "unidade": "g"},
            "Laranja": {"kj": 197, "kcal": 47, "fat": 0.1, "sat": 0.0, "carb": 11.8, "sugar": 9.4, "prot": 0.9,
                        "salt": 0.0, "unidade": "unid", "peso_unid": 130},
            "Mamão Papaya": {"kj": 179, "kcal": 43, "fat": 0.3, "sat": 0.1, "carb": 10.8, "sugar": 7.8, "prot": 0.5,
                             "salt": 0.02, "unidade": "unid", "peso_unid": 300},
            "Melancia": {"kj": 125, "kcal": 30, "fat": 0.2, "sat": 0.0, "carb": 7.6, "sugar": 6.2, "prot": 0.6,
                         "salt": 0.0, "unidade": "g"},
            "Abacate": {"kj": 670, "kcal": 160, "fat": 14.7, "sat": 2.1, "carb": 8.5, "sugar": 0.7, "prot": 2.0,
                        "salt": 0.02, "unidade": "unid", "peso_unid": 200},
            "Uva (Verde)": {"kj": 288, "kcal": 69, "fat": 0.2, "sat": 0.1, "carb": 18.1, "sugar": 15.5, "prot": 0.7,
                            "salt": 0.0, "unidade": "g"},
            "Manga": {"kj": 251, "kcal": 60, "fat": 0.4, "sat": 0.1, "carb": 15.0, "sugar": 13.7, "prot": 0.8,
                      "salt": 0.0, "unidade": "unid", "peso_unid": 200},
            "Pera": {"kj": 238, "kcal": 57, "fat": 0.1, "sat": 0.0, "carb": 15.2, "sugar": 9.8, "prot": 0.4,
                     "salt": 0.0, "unidade": "unid", "peso_unid": 130}
        },
        "🥑 Gorduras e Óleos": {
            "Azeite de Oliva": {"kj": 3700, "kcal": 884, "fat": 100.0, "sat": 14.0, "carb": 0.0, "sugar": 0.0,
                                "prot": 0.0, "salt": 0.0, "unidade": "ml"},
            "Manteiga": {"kj": 2999, "kcal": 717, "fat": 81.0, "sat": 51.0, "carb": 0.1, "sugar": 0.1, "prot": 0.9,
                         "salt": 1.5, "unidade": "g"},
            "Óleo de Soja": {"kj": 3700, "kcal": 884, "fat": 100.0, "sat": 16.0, "carb": 0.0, "sugar": 0.0, "prot": 0.0,
                             "salt": 0.0, "unidade": "ml"},
            "Óleo de Coco": {"kj": 3607, "kcal": 862, "fat": 100.0, "sat": 87.0, "carb": 0.0, "sugar": 0.0, "prot": 0.0,
                             "salt": 0.0, "unidade": "ml"},
            "Castanha de Caju": {"kj": 2314, "kcal": 553, "fat": 43.8, "sat": 7.8, "carb": 30.2, "sugar": 5.9,
                                 "prot": 18.2, "salt": 0.03, "unidade": "g"},
            "Castanha do Pará": {"kj": 2744, "kcal": 656, "fat": 66.4, "sat": 15.1, "carb": 12.3, "sugar": 2.3,
                                 "prot": 14.3, "salt": 0.01, "unidade": "unid", "peso_unid": 5},
            "Amêndoa": {"kj": 2408, "kcal": 579, "fat": 49.9, "sat": 3.8, "carb": 21.6, "sugar": 4.4, "prot": 21.2,
                        "salt": 0.01, "unidade": "g"},
            "Amendoim (Torrado)": {"kj": 2438, "kcal": 583, "fat": 49.2, "sat": 6.8, "carb": 16.1, "sugar": 4.0,
                                   "prot": 25.8, "salt": 0.04, "unidade": "g"},
            "Pasta de Amendoim (Integral)": {"kj": 2460, "kcal": 588, "fat": 50.0, "sat": 10.0, "carb": 20.0,
                                             "sugar": 9.0, "prot": 25.0, "salt": 0.0, "unidade": "g"},
            "Maionese (Tradicional)": {"kj": 2845, "kcal": 680, "fat": 75.0, "sat": 12.0, "carb": 0.6, "sugar": 0.6,
                                       "prot": 1.0, "salt": 1.5, "unidade": "g"}
        },
        "🧂 Outros": {
            "Sal de Cozinha": {"kj": 0, "kcal": 0, "fat": 0.0, "sat": 0.0, "carb": 0.0, "sugar": 0.0, "prot": 0.0,
                               "salt": 100.0, "unidade": "g"},
            "Açúcar Refinado": {"kj": 1619, "kcal": 387, "fat": 0.0, "sat": 0.0, "carb": 100.0, "sugar": 100.0,
                                "prot": 0.0, "salt": 0.0, "unidade": "g"},
            "Açúcar Mascavo": {"kj": 1590, "kcal": 380, "fat": 0.0, "sat": 0.0, "carb": 98.0, "sugar": 97.0,
                               "prot": 0.1, "salt": 0.07, "unidade": "g"},
            "Mel": {"kj": 1272, "kcal": 304, "fat": 0.0, "sat": 0.0, "carb": 82.4, "sugar": 82.1, "prot": 0.3,
                    "salt": 0.01, "unidade": "g"},
            "Cacau em Pó (100%)": {"kj": 954, "kcal": 228, "fat": 13.7, "sat": 8.1, "carb": 57.9, "sugar": 1.8,
                                   "prot": 19.6, "salt": 0.05, "unidade": "g"},
            "Chocolate ao Leite": {"kj": 2240, "kcal": 535, "fat": 29.7, "sat": 18.5, "carb": 59.4, "sugar": 51.5,
                                   "prot": 7.6, "salt": 0.24, "unidade": "g"},
            "Molho de Soja (Shoyu)": {"kj": 222, "kcal": 53, "fat": 0.1, "sat": 0.0, "carb": 4.9, "sugar": 0.4,
                                      "prot": 8.1, "salt": 14.5, "unidade": "ml"},
            "Vinagre de Maçã": {"kj": 88, "kcal": 21, "fat": 0.0, "sat": 0.0, "carb": 0.9, "sugar": 0.4, "prot": 0.0,
                                "salt": 0.01, "unidade": "ml"},
            "Mostarda (Molho)": {"kj": 276, "kcal": 66, "fat": 3.3, "sat": 0.2, "carb": 4.9, "sugar": 2.5, "prot": 4.1,
                                 "salt": 2.80, "unidade": "g"},
            "Ketchup": {"kj": 406, "kcal": 97, "fat": 0.1, "sat": 0.0, "carb": 24.1, "sugar": 20.6, "prot": 1.0,
                        "salt": 2.20, "unidade": "g"}
        }
    }

# --- CSS (Fundo Verde Musgo apenas na tela inicial) ---
estilo_customizado = """
<style>
/* Altera o fundo principal da aplicação para verde musgo */
[data-testid="stAppViewContainer"], .stApp {
    background-color: #8A9A5B !important; 
}
[data-testid="stHeader"] {
    background-color: transparent !important;
}
</style>
"""
st.markdown(estilo_customizado, unsafe_allow_html=True)

st.title("🇮🇪 Gerador de Tabela Nutricional")

with st.expander("➕ Adicionar Novo Ingrediente (Simplificado)", expanded=False):
    st.write("Insira os valores nutricionais básicos **por 100g**. Os kJ (Joules) serão calculados automaticamente.")

    with st.form("form_novo_ingrediente", clear_on_submit=True):
        nova_categoria = st.selectbox("Categoria", list(st.session_state.banco_categorias.keys()))
        novo_nome = st.text_input("Nome do Ingrediente")

        col1, col2 = st.columns(2)
        with col1:
            n_kcal = st.number_input("Energia (kcal)", min_value=0.0, format="%.1f")
            n_fat = st.number_input("Gorduras Totais (g)", min_value=0.0, format="%.1f")
            n_carb = st.number_input("Carboidratos (g)", min_value=0.0, format="%.1f")
            n_prot = st.number_input("Proteínas (g)", min_value=0.0, format="%.1f")
            n_unid = st.selectbox("Forma de Medida", ["g", "ml", "unid"])

        with col2:
            n_sat = st.number_input("Gorduras Saturadas (g)", min_value=0.0, format="%.1f")
            n_sug = st.number_input("Açúcares (g)", min_value=0.0, format="%.1f")
            n_salt = st.number_input("Sal (g)", min_value=0.0, format="%.1f", help="Calcule como: Sódio(g) x 2.5")
            n_peso_unid = st.number_input("Se for 'unid', qual o peso de 1 unidade? (g)", min_value=1, value=100)

        salvar_ingrediente = st.form_submit_button("Salvar Ingrediente")

        if salvar_ingrediente:
            if novo_nome.strip() == "":
                st.error("Dê um nome ao ingrediente!")
            else:
                n_kj = n_kcal * 4.184
                st.session_state.banco_categorias[nova_categoria][novo_nome] = {
                    "kj": n_kj, "kcal": n_kcal, "fat": n_fat, "sat": n_sat,
                    "carb": n_carb, "sugar": n_sug, "prot": n_prot, "salt": n_salt,
                    "unidade": n_unid, "peso_unid": n_peso_unid
                }
                st.success(f"✅ '{novo_nome}' adicionado com sucesso na categoria {nova_categoria}!")

st.write("---")
st.write(
    "Dica: Selecione todos os ingredientes desejados e use a tecla **TAB** para preencher rapidamente as quantidades!")

# --- ENTRADA DE DADOS DA RECEITA ---
pesos_inseridos = {}
ingredientes_selecionados = {}

for categoria, alimentos in st.session_state.banco_categorias.items():
    with st.expander(f"{categoria}", expanded=False):
        opcoes = list(alimentos.keys())
        selecionados_na_categoria = st.multiselect(
            "Selecione os ingredientes:",
            opcoes,
            key=f"ms_{categoria}",
            label_visibility="collapsed",
            placeholder="Clique para escolher..."
        )

        if selecionados_na_categoria:
            st.write("Quantidades:")
            for ingrediente in selecionados_na_categoria:
                col_nome, col_input = st.columns([3, 2])
                with col_nome:
                    st.write("")
                    st.write(f"• {ingrediente}")
                with col_input:
                    info = alimentos[ingrediente]
                    unidade = info.get("unidade", "g")

                    if unidade == "unid":
                        texto_placeholder = "Ex: 2 unidades"
                    elif unidade == "ml":
                        texto_placeholder = "Ex: 150 ml"
                    else:
                        texto_placeholder = "Ex: 150 g"

                    qtd_texto = st.text_input(
                        label=f"Qtd {ingrediente}",
                        placeholder=texto_placeholder,
                        key=f"peso_{ingrediente}",
                        label_visibility="collapsed"
                    )

                    try:
                        if qtd_texto.strip() == "":
                            pesos_inseridos[ingrediente] = 0.0
                        else:
                            valor_numerico = float(qtd_texto.replace(",", "."))
                            pesos_inseridos[ingrediente] = valor_numerico
                            ingredientes_selecionados[ingrediente] = info
                    except ValueError:
                        st.error("Digite apenas números.")
                        pesos_inseridos[ingrediente] = 0.0

st.write("")
gerar_tabela = st.button("Calcular e Exibir Tabelas na Tela", use_container_width=True)

# --- EXIBIÇÃO E CÁLCULOS DAS TABELAS ON CLICK ---
if gerar_tabela:
    ingredientes_validos = {ing: qtd for ing, qtd in pesos_inseridos.items() if qtd > 0}

    if len(ingredientes_validos) == 0:
        st.error("Por favor, preencha a quantidade de pelo menos um ingrediente para gerar a tabela.")
    else:
        st.divider()

        # Preparando os dados da receita para exibição amigável
        dados_receita_view = []
        peso_total_gramas = 0.0

        for ing, qtd in ingredientes_validos.items():
            info = ingredientes_selecionados[ing]
            unidade = info.get("unidade", "g")

            if unidade == "unid":
                str_qtd = f"{qtd:g} unid"
                peso_real_g = qtd * info.get("peso_unid", 100)
            elif unidade == "ml":
                str_qtd = f"{qtd:g} ml"
                peso_real_g = qtd
            else:
                str_qtd = f"{qtd:g} g"
                peso_real_g = qtd

            peso_total_gramas += peso_real_g
            dados_receita_view.append({"Ingrediente": ing, "Quantidade": str_qtd})

        st.subheader("Receita: Ingredientes Utilizados")
        df_receita = pd.DataFrame(dados_receita_view)
        st.table(df_receita)
        st.write(f"Peso Total da Receita (aprox.): **{peso_total_gramas:g} g**")

        st.write("")

        # 2. CÁLCULO DA TABELA NUTRICIONAL E VALORES DIÁRIOS (% RI)
        totais = {"kj": 0.0, "kcal": 0.0, "fat": 0.0, "sat": 0.0, "carb": 0.0, "sugar": 0.0, "prot": 0.0, "salt": 0.0}
        valores_diarios = {"kj": 8400, "kcal": 2000, "fat": 70, "sat": 20, "carb": 260, "sugar": 90, "prot": 50,
                           "salt": 6}

        for ing, qtd in ingredientes_validos.items():
            info_nutri = ingredientes_selecionados[ing]
            unidade = info_nutri.get("unidade", "g")

            if unidade == "unid":
                peso_real_g = qtd * info_nutri.get("peso_unid", 100)
            else:
                peso_real_g = qtd

            fator = peso_real_g / 100.0
            for nutriente in totais.keys():
                totais[nutriente] += info_nutri[nutriente] * fator

        fator_final = 100.0 / peso_total_gramas
        valores_100g = {k: v * fator_final for k, v in totais.items()}


        def calc_vd(valor, referencia):
            return f"{(valor / referencia) * 100:.1f}%" if referencia > 0 else "-"


        # Preparação dos dados para inserir no HTML customizado
        linhas_html = ""
        linhas = [
            ("Energy", f"{valores_100g['kj']:.0f} kJ / {valores_100g['kcal']:.0f} kcal",
             f"{calc_vd(valores_100g['kj'], valores_diarios['kj'])} / {calc_vd(valores_100g['kcal'], valores_diarios['kcal'])}"),
            ("Fat", f"{valores_100g['fat']:.1f} g", calc_vd(valores_100g['fat'], valores_diarios['fat'])),
            ("&nbsp;&nbsp;of which saturates", f"{valores_100g['sat']:.1f} g",
             calc_vd(valores_100g['sat'], valores_diarios['sat'])),
            ("Carbohydrate", f"{valores_100g['carb']:.1f} g", calc_vd(valores_100g['carb'], valores_diarios['carb'])),
            ("&nbsp;&nbsp;of which sugars", f"{valores_100g['sugar']:.1f} g",
             calc_vd(valores_100g['sugar'], valores_diarios['sugar'])),
            ("Protein", f"{valores_100g['prot']:.1f} g", calc_vd(valores_100g['prot'], valores_diarios['prot'])),
            ("Salt", f"{valores_100g['salt']:.2f} g", calc_vd(valores_100g['salt'], valores_diarios['salt']))
        ]

        for nome, per100, ri in linhas:
            linhas_html += f"<tr><td>{nome}</td><td>{per100}</td><td>{ri}</td></tr>"

        # --- HTML E CSS EXCLUSIVO DA NUTRITION DECLARATION COM BOTÃO DE IMPRESSÃO ---
        html_nutrition_table = f"""
        <style>
        /* Estilos da Tabela do Rótulo */
        .nutrition-table {{
            width: 100%;
            border-collapse: collapse;
            border: 3px solid black !important; /* Moldura externa mais larga e preta */
            background-color: white !important;
            color: black !important;
            font-family: sans-serif;
            margin-bottom: 5px;
        }}
        .nutrition-table th, .nutrition-table td {{
            border: 1px solid black !important; /* Grade interna fina preta */
            padding: 8px;
            text-align: left;
            color: black !important;
        }}
        .nutrition-table th {{
            font-weight: bold;
        }}

        /* Estilos do Botão de Imprimir */
        .btn-imprimir {{
            background-color: #2e7d32;
            color: white;
            border: none;
            padding: 12px 20px;
            text-align: center;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            margin-top: 15px;
        }}
        .btn-imprimir:hover {{
            background-color: #1b5e20;
        }}

        /* Regras Especiais para quando o botão de Imprimir for acionado */
        @media print {{
            /* Esconde toda a interface do Streamlit (fundo verde, menus, botões) */
            body * {{
                visibility: hidden;
            }}
            /* Torna visível apenas a área da tabela */
            #area-impressao, #area-impressao * {{
                visibility: visible;
            }}
            /* Posiciona a tabela perfeitamente na página do PDF */
            #area-impressao {{
                position: absolute;
                left: 0;
                top: 0;
                width: 100%;
            }}
            /* Esconde o próprio botão na hora de gerar o PDF */
            .btn-imprimir {{
                display: none !important;
            }}
        }}
        </style>

        <div id="area-impressao">
            <h3 style="color: black; font-family: sans-serif; margin-bottom: 10px;">Nutrition Declaration (FSAI / UE)</h3>
            <table class="nutrition-table">
                <thead>
                    <tr>
                        <th>Typical Values</th>
                        <th>Per 100g</th>
                        <th>% RI* (Per 100g)</th>
                    </tr>
                </thead>
                <tbody>
                    {linhas_html}
                </tbody>
            </table>
            <p style="color: black; font-size: 12px; font-family: sans-serif; margin-top: 5px;">* Reference Intake (RI) of an average adult (8400 kJ / 2000 kcal).</p>
        </div>

        <button class="btn-imprimir" onclick="window.print()">🖨️ Gerar PDF / Imprimir Rótulo</button>
        """

        # st.markdown injeta a tabela, o CSS customizado e o botão no aplicativo
        st.markdown(html_nutrition_table, unsafe_allow_html=True)