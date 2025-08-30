import streamlit as st

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


# --- BARRA DE NAVEGAÇÃO LATERAL ---
st.sidebar.header("Navegação")
st.sidebar.markdown("🏠 [Início](#inicio)")
st.sidebar.markdown("🧑‍💻 [Sobre Mim](#sobre-mim)")
st.sidebar.markdown("📂 [Projetos](#projetos)")
st.sidebar.markdown("✉️ [Contato](#contato)")
# --- NOVO TESTE DE DIAGNÓSTICO: INJETANDO O CSS DIRETAMENTE ---


# --- SEÇÃO DE CABEÇALHO ---
with st.container():
    st.markdown("<a id='inicio'></a>", unsafe_allow_html=True) # Âncora
    st.markdown("### Olá! Eu sou:")
    st.markdown("# Jaime José Cardozo Junior 👋")
    st.write("---")
    
    left_column, right_column = st.columns([2, 1])
    with left_column:
        st.write(
            """
            Um profissional apaixonado por **[PREENCHA SUA ÁREA DE ATUAÇÃO]** e pela criação de soluções inovadoras.
            Este é o meu portfólio digital, onde você pode explorar meus projetos e a jornada de desenvolvimento por trás deles.
            """
        )

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

# --- SEÇÃO DE CONTATO ---
with st.container():
    st.markdown("<a id='contato'></a>", unsafe_allow_html=True)
    st.header("📬 Conecte-se Comigo")
    st.write("Sinta-se à vontade para me contatar através de qualquer um dos links abaixo!")
    
    # --- 1. DEFINA SUAS INFORMAÇÕES DE CONTATO AQUI ---
    LINKEDIN_URL = "https://www.linkedin.com/in/jaime-cardozo-2838052a1/"
    EMAIL_ADDRESS = "jaimecardozo.junior@gmail.com"
    GITHUB_URL = "https://github.com/JaimeCardozo2212"
    # MUDANÇA 1: Variável renomeada. Use o formato internacional com o sinal de '+'
    PHONE_NUMBER = "+5547997037331" 


    # --- 2. DEFINIÇÕES DOS ÍCONES (SVGs) ---
    ICON_LINKEDIN = """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20.5 2h-17A1.5 1.5 0 002 3.5v17A1.5 1.5 0 003.5 22h17a1.5 1.5 0 001.5-1.5v-17A1.5 1.5 0 0020.5 2zM8 19H5v-9h3zM6.5 8.25A1.75 1.75 0 118.25 6.5 1.75 1.75 0 016.5 8.25zM19 19h-3v-4.74c0-1.42-.6-1.93-1.38-1.93A1.62 1.62 0 0013 14.19V19h-3v-9h2.9v1.3a3.11 3.11 0 012.7-1.4c1.55 0 3.36.93 3.36 4.42V19z"></path>
        </svg>
    """
    ICON_GMAIL = """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
            <path d="M22 5.889V18a2 2 0 01-2 2H4a2 2 0 01-2-2V6c0-.3.13-.58.35-.78L12 12l9.65-6.78A.93.93 0 0122 5.89zM12 10.11L2.35 3.22A.93.93 0 013.11 3H21a1 1 0 01.78.38L12 10.11z"></path>
        </svg>
    """
    ICON_GITHUB = """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C6.477 2 2 6.477 2 12c0 4.418 2.865 8.165 6.839 9.489.5.092.682-.217.682-.482 0-.237-.009-.868-.014-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.03-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.82c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.378.203 2.398.1 2.65.64.7 1.028 1.595 1.028 2.688 0 3.848-2.338 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.578.688.482A10.001 10.001 0 0022 12c0-5.523-4.477-10-10-10z"></path>
        </svg>
    """
    # MUDANÇA 2: O SVG do WhatsApp foi trocado pelo do telefone
    ICON_PHONE = """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor">
            <path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"></path>
        </svg>
    """

    # --- 3. COMBINA TUDO EM UM BLOCO HTML FINAL ---
    links_html = f"""
    <div class="social-icons">
        <a href="{LINKEDIN_URL}" target="_blank" title="LinkedIn">{ICON_LINKEDIN}</a>
        <a href="mailto:{EMAIL_ADDRESS}" target="_blank" title="Gmail">{ICON_GMAIL}</a>
        <a href="{GITHUB_URL}" target="_blank" title="GitHub">{ICON_GITHUB}</a>
        <a href="https://wa.me/{PHONE_NUMBER}" target="_blank" title="WhtasApp">{ICON_PHONE}</a>
    </div>
    """

    # --- 4. RENDERIZA O HTML NA PÁGINA ---
    st.markdown(links_html, unsafe_allow_html=True)