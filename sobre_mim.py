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
                - Sou **[PREENCHA SUA PROFISSÃO OU TÍTULO]** com experiência em **[PREENCHA SUA HABILIDADE PRINCIPAL]**.
                - Minha jornada em **[PREENCHA SUA ÁREA]** começou com **[PREENCHA SUA PAIXÃO OU MOTIVAÇÃO]**.
                - Sou um entusiasta por **[PREENCHA TECNOLOGIAS OU HOBBIES]** e adoro solucionar problemas complexos de forma criativa.
                - Quando não estou programando, você pode me encontrar **[PREENCHA SEUS HOBBIES]**.
                """
            )

        with right_column:
            # Você pode substituir este link por uma imagem sua
            st.image("https://media.licdn.com/dms/image/v2/D4D03AQEX_pdKr_1VAg/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1701186530760?e=1759363200&v=beta&t=9ChyTeMmgKnk15z-2kH4yCRI9tqQp-9oskBzQ3usifw", width=300)

        st.write("---")