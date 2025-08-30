import streamlit as st

def minha_saindbar():
    # --- BARRA DE NAVEGAÇÃO LATERAL ---
    st.sidebar.header("Navegação")
    st.sidebar.markdown("🏠 [Início](#inicio)")
    st.sidebar.markdown("🧑‍💻 [Sobre Mim](#sobre-mim)")
    st.sidebar.markdown("📂 [Projetos](#projetos)")
    st.sidebar.markdown("✉️ [Contato](#contato)")
    # --- NOVO TESTE DE DIAGNÓSTICO: INJETANDO O CSS DIRETAMENTE ---