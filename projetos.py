import streamlit as st

def meus_projetos():
    # --- SEÇÃO DE PROJETOS ---
    with st.container():
        st.markdown("<a id='projetos'></a>", unsafe_allow_html=True) # Âncora
        st.markdown("## Meus Projetos")
        
        # --- Projeto 1 ---
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://placehold.co/400x400/161b22/8b949e?text=Imagem+Projeto+1", width=200)
            st.markdown("**[NOME DO PROJETO 1]**")
            st.markdown("**Tecnologias:** Python, Pandas, Matplotlib")
            st.write("Link:", "[GitHub](https://github.com/seu-usuario/seu-repositorio)")
            
        with col2:
            st.write(
                """
                Descrição detalhada do projeto 1. Fale sobre o desafio, o processo de desenvolvimento e os resultados alcançados. 
                Adicione capturas de tela, gráficos ou qualquer outra visualização que ajude a ilustrar seu trabalho.
                """
            )
        st.write("---")

        # --- Projeto 2 ---
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://placehold.co/400x400/161b22/8b949e?text=Imagem+Projeto+2", width=200)
            st.markdown("**[NOME DO PROJETO 2]**")
            st.markdown("**Tecnologias:** JavaScript, React, Node.js")
            st.write("Link:", "[GitHub](https://github.com/seu-usuario/seu-repositorio)")
            
        with col2:
            st.write(
                """
                Descrição detalhada do projeto 2. Mostre como você aplicou suas habilidades para resolver um problema específico. 
                Destaque os principais recursos e a arquitetura da solução.
                """
            )
        st.write("---")
        
        # --- Projeto 3 ---
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image("https://placehold.co/400x400/161b22/8b949e?text=Imagem+Projeto+3", width=200)
            st.markdown("**[NOME DO PROJETO 3]**")
            st.markdown("**Tecnologias:** Streamlit, Python, CSS")
            st.write("Link:", "[GitHub](https://github.com/seu-usuario/seu-repositorio)")
            
        with col2:
            st.write(
                """
                Descrição detalhada do projeto 3. Mostre como você aplicou suas habilidades para resolver um problema específico. 
                Destaque os principais recursos e a arquitetura da solução.
                """
            )
        st.write("---")