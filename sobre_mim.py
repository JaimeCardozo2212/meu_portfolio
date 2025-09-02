import streamlit as st

def sobre_mim():
    # --- SEÇÃO SOBRE MIM ---
    with st.container():
        st.markdown("<a id='sobre-mim'></a>", unsafe_allow_html=True) # Âncora
        st.markdown("## 💻 Sobre Mim")
        
        left_column, right_column = st.columns([2, 1])
        with left_column:
            st.write(
                """
                **Desenvolvedor backend Python** com foco em automação, cursando o último semestre de Análise e Desenvolvimento de Sistemas. 
                Desde 2021, minha paixão é construir soluções que otimizam processos e resolvem problemas de forma eficiente. 
                Sou especialista na criação de automações e robôs para extração de dados e bots para jogos. 
                Busco continuamente novas tecnologias para aprimorar cada projeto, motivado pela constante inovação na área. 
                Estou pronto para aplicar minhas habilidades em novos desafios e continuar crescendo profissionalmente.
                """
            )

        with right_column:
            # Você pode substituir este link por uma imagem sua
            st.image("https://media.licdn.com/dms/image/v2/D4D03AQFCnXsS5rxtDg/profile-displayphoto-scale_400_400/B4DZj7yZsYH4Ao-/0/1756570952510?e=1759363200&v=beta&t=XavipDcipHwPHKdWwFVYC4-ujN_pzg6OD6ndDmbEHjc", width=300)

        st.write("---")