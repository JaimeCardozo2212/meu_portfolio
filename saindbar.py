import streamlit as st

def minha_sidebar():
    # Estilo CSS personalizado para a sidebar
    st.markdown("""
    <style>
    /* Variáveis para cores */
    :root {
        --sidebar-bg: linear-gradient(180deg, #000000 0%, #020038 100%);
        --sidebar-border: #30363d;
        --sidebar-text: #c9d1d9;
        --sidebar-text-hover: #ffffff;
        --sidebar-accent: #58a6ff;
        --sidebar-highlight: #1f6feb;
    }
    
    /* Estilização geral da sidebar */
    [data-testid="stSidebar"] {
        background-image: var(--sidebar-bg) !important;
        border-right: 1px solid var(--sidebar-border) !important;
        box-shadow: 4px 0 12px rgba(0, 0, 0, 0.15) !important;
    }
    
    /* Cabeçalho da sidebar */
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
        color: var(--sidebar-text-hover) !important;
        text-align: center !important;
        margin-bottom: 2rem !important;
        position: relative !important;
        padding-bottom: 15px !important;
    }
    
    [data-testid="stSidebar"] h1:after {
        content: '' !important;
        position: absolute !important;
        bottom: 0 !important;
        left: 50% !important;
        transform: translateX(-50%) !important;
        width: 50px !important;
        height: 3px !important;
        background: linear-gradient(90deg, var(--sidebar-accent), var(--sidebar-highlight)) !important;
        border-radius: 3px !important;
    }
    
    /* Links de navegação */
    .sidebar-link {
        display: flex !important;
        align-items: center !important;
        padding: 12px 20px !important;
        border-radius: 8px !important;
        margin: 8px 0 !important;
        color: var(--sidebar-text) !important;
        background-color: #020038 !important;
        transition: all 0.3s ease !important;
        text-decoration: none !important;
        position: relative !important;
        overflow: hidden !important;
        border-left: 4px solid transparent !important;
        font-weight: 500 !important;
    }
    
    .sidebar-link:before {
        content: '' !important;
        position: absolute !important;
        top: 0 !important;
        left: 0 !important;
        width: 4px !important;
        height: 100% !important;
        background: linear-gradient(to bottom, var(--sidebar-accent), var(--sidebar-highlight)) !important;
        opacity: 0 !important;
        transition: opacity 0.3s ease !important;
    }
    
    .sidebar-link:hover {
        color: var(--sidebar-text-hover) !important;
        background-color: rgba(33, 38, 45, 0.7) !important;
        transform: translateX(5px) !important;
    }
    
    .sidebar-link:hover:before {
        opacity: 1 !important;
    }
    
    .sidebar-link.active {
        color: var(--sidebar-text-hover) !important;
        background-color: rgba(33, 38, 45, 0.9) !important;
        border-left: 4px solid var(--sidebar-highlight) !important;
        font-weight: 600 !important;
    }
    
    .sidebar-link.active:before {
        opacity: 1 !important;
    }
    
    /* Ícones */
    .sidebar-icon {
        margin-right: 12px !important;
        font-size: 18px !important;
        width: 24px !important;
        text-align: center !important;
    }
    
    /* Seção de redes sociais */
    .sidebar-social {
        display: flex !important;
        justify-content: center !important;
        gap: 16px !important;
        margin-top: 2rem !important;
        padding-top: 2rem !important;
        border-top: 1px solid var(--sidebar-border) !important;
    }
    
    .sidebar-social a {
        color: var(--sidebar-text) !important;
        transition: all 0.3s ease !important;
        font-size: 20px !important;
    }
    
    .sidebar-social a:hover {
        color: var(--sidebar-accent) !important;
        transform: translateY(-3px) !important;
    }
    
    /* Informações de contato na sidebar */
    .sidebar-contact {
        margin-top: 1.5rem !important;
        padding: 1rem !important;
        background-color: rgba(33, 38, 45, 0.5) !important;
        border-radius: 8px !important;
        border-left: 3px solid var(--sidebar-accent) !important;
    }
    
    .sidebar-contact p {
        margin: 5px 0 !important;
        font-size: 14px !important;
        color: var(--sidebar-text) !important;
    }
    
    .sidebar-contact i {
        margin-right: 8px !important;
        color: var(--sidebar-accent) !important;
        width: 16px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # --- BARRA DE NAVEGAÇÃO LATERAL ---
    st.sidebar.header("Navegação")
    
    # Usando HTML personalizado para os links
    st.sidebar.markdown("""
    <div class="sidebar-links">
        <a href="#inicio" class="sidebar-link">
            <span class="sidebar-icon">🏠</span>
            <span>Início</span>
        </a>
        <a href="#sobre-mim" class="sidebar-link">
            <span class="sidebar-icon">🧑‍💻</span>
            <span>Sobre Mim</span>
        </a>
        <a href="#projetos" class="sidebar-link">
            <span class="sidebar-icon">📂</span>
            <span>Projetos</span>
        </a>
        <a href="#contato" class="sidebar-link">
            <span class="sidebar-icon">✉️</span>
            <span>Contato</span>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Seção de informações de contato

    st.sidebar.markdown("""
    <div class="sidebar-contact">
        <p><i class="fas fa-map-marker-alt"></i> Joinville - SC, Brasil</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Seção de redes sociais
    st.sidebar.markdown("""
    <div class="sidebar-social">
        <a href="https://github.com/JaimeCardozo2212" target="_blank"><i class="fab fa-github"></i></a>
        <a href="https://www.linkedin.com/in/jaime-cardozo-2838052a1/" target="_blank"><i class="fab fa-linkedin"></i></a>
    </div>
    """, unsafe_allow_html=True)
    
    # Botão de download de currículo
    # st.sidebar.markdown("---")
    # Link para o currículo
    st.sidebar.markdown("[jaimecardozo.junior@gmail.com](mailto:jaimecardozo.junior@gmail.com)")
    st.sidebar.markdown(
        """
        <div style="text-align: center;">
            <a href="https://drive.google.com/file/d/1oPOnUUacOaZhyPFcShkCtNKaAA_27Ysy/view?usp=sharing" 
               target="_blank" class="sidebar-link" style="display: inline-block; text-align: center;">
                <span class="sidebar-icon">📄</span>
                <span>Baixar Currículo</span>
            </a>
        </div>
        """, 
        unsafe_allow_html=True
    )
    