import streamlit as st
from saindbar import minha_sidebar
from projetos import meus_projetos
from contato import meu_contato
from sobre_mim import sobre_mim

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Portfólio de Jaime",
    page_icon=":computer:",
    layout="wide"
)

# --- CSS PERSONALIZADO ---

# Injeta CSS do arquivo externo
try:
    with open("style.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("Arquivo 'style.css' não encontrado. Certifique-se de que ele está na mesma pasta que 'app.py'.")

# Adiciona o container de partículas (usando apenas HTML/CSS)
st.markdown('''
<div class="particles-container">
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
    <div class="particle"></div>
</div>
''', unsafe_allow_html=True)


minha_sidebar()

# --- SEÇÃO DE CABEÇALHO ---
with st.container():
    st.markdown("<a id='inicio'></a>", unsafe_allow_html=True) # Âncora
    st.markdown("### Olá! Eu sou:")
    st.markdown("# Jaime José Cardozo Junior")
    # st.write("---")
    
    left_column, right_column = st.columns([2, 1])
    with left_column:
        st.image("https://www.citypng.com/public/uploads/preview/hd-python-logo-symbol-transparent-png-735811696257415dbkifcuokn.png",width=35)
        st.write(
            """
                **Desenvolvedor backend Python**\n
                **Conhecimetos framework** : *Django, Streamlit*\n
                **Demais tecnologias** : *Selenium , Requests , Scrapy , Pandas , PyAutoGUI , LangChain , PyODBC*

            """
        )


sobre_mim()

meus_projetos()

meu_contato()
