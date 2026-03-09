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
                    Desenvolvedor **Back-End Python** com experiência em projetos **full-stack**.\n 
                    Especializo-me na criação de soluções robustas e automatizadas (RPA),\n 
                    incluindo sistemas de bots para jogos,\n 
                    ferramentas de extração de dados (web scraping) e desenvolvimento web.\n
                    Minha transição de carreira para a tecnologia, iniciada em 2020,\n 
                    foi impulsionada por uma paixão genuína pela área.\n 
                    Sou um profissional autodidata, com grande capacidade de aprendizado e focado em aplicar conhecimentos\n 
                    teóricos em desafios práticos e resultados concretos.
                    
                """
            )

        with right_column:
            # Você pode substituir este link por uma imagem sua
            st.image("img/minha_foto.png", width=300)

        st.write("---")
