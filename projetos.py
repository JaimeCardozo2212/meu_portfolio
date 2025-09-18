import streamlit as st

def meus_projetos():
    # --- SEÇÃO DE PROJETOS ---
    with st.container():
        st.markdown("<a id='projetos'></a>", unsafe_allow_html=True) # Âncora
        st.markdown("## Meus Projetos")
        st.write("---")
        
        # --- Projeto 1 ---
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("### Este Portfólio")
            st.image(r"img/meu_portfolio.png", width=350)
            st.markdown("**Tecnologias:** Python, CSS")
            st.write("Link:", "[GitHub](https://github.com/JaimeCardozo2212/meu_portfolio.git)")
            
        with col2:
            st.write("---")
            st.write(
                """
                Criei meu portfolio com Streamlit, é um framework Python de código aberto A ferramenta é conhecida pela sua simplicidade, possibilitando o desenvolvimento de dashboards e interfaces complexas com poucas linhas de código, sem a necessidade de conhecimentos aprofundados em desenvolvimento web
                """
            )
        st.write("---")

        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("### App consulta de unidade de saúde Secretaria da Saúde de Joinville")
            st.image(r"img/consulta_ubsf.png", width=300)
            st.markdown("**Tecnologias:** Python, Streamlit, selenium")
            st.write("Link:", "[GitHub](https://github.com/JaimeCardozo2212/consulta_mapa_ubsf_referencia.git)")
            
        with col2:
            st.write("---")
            st.write(
                """
                Este aplicativo foi desenvolvido para facilitar a consulta de unidades de saúde (UBSF) em Joinville. 
                Ao digitar um endereço, o app informa a qual unidade de saúde e distrito ele pertence, 
                além de fornecer dados de contato, como telefone, endereço e horário de funcionamento.
                """
            )
            st.link_button(url="https://consultamapa.streamlit.app/",label="Link do App", type='primary', width='content')
        st.write("---")

        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("### Robo Criado para Secretaria da Saúde de Joinville")
            st.image(r"img/robo_obitos.png", width=300)
            st.markdown("**Tecnologias:** Python, TKinter, opencv, PIL")
            st.write("Link:", "[GitHub](https://github.com/JaimeCardozo2212/Robo_Baixa_de_obitos_ses_.git)")
            
        with col2:
            st.write("---")
            st.write(
                """
                Projeto: Automação da Baixa de Óbitos na Secretaria de Saúde de Joinville-SC\n
                O Desafio: A Secretaria de Saúde de Joinville enfrentava um processo manual e demorado para a baixa de óbitos. 
                A tarefa exigia que uma pessoa consultasse e processasse, manualmente, uma lista com mais de 5.000 endereços, 
                resultando em um trabalho extenso e propenso a erros.
                Minha Solução: Criei um robô que automatizou a pesquisa de endereços e a baixa dos dados. A solução eliminou a necessidade de interação 
                humana, otimizando o fluxo de trabalho e garantindo maior precisão.
                Resultados: A automação reduziu drasticamente o tempo de conclusão da tarefa. 
                O processo, que antes levava dias para ser finalizado, passou a ser concluído em menos de 3 horas, 
                demonstrando um ganho significativo em eficiência e produtividade para a Secretaria.
                """
            )
        st.write("---")

        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("### Controle de Ordem de Serviço")
            st.image(r"img/painel_chamados.png", width=350)
            st.markdown("**Tecnologias:**Streamlit, Python, CSS")
            st.write("Link:", "[GitHub](https://github.com/JaimeCardozo2212/controle_de_chamados.git)")
            
        with col2:
            st.write("---")
            st.write(
                """
                Este projeto é um painel de controle (dashboard) desenvolvido para otimizar o gerenciamento de Ordens de Serviço. 
                A aplicação centraliza as informações e permite uma visualização clara dos chamados, 
                com funcionalidades de filtragem avançada por técnico, status, categoria e nível de urgência.
                O fluxo de dados é totalmente automatizado: 
                um bot de extração coleta as informações de um sistema externo, as processa e as armazena em um banco de dados, 
                que por sua vez alimenta o dashboard em tempo real.
                """
            )
        st.write("---")
        
        # --- Projeto 4 ---
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("### Robo para extração de dados")
            st.image(r"img/robo_api.png", width=300)
            st.markdown("**Tecnologias:** Streamlit, Pandas, Python, CSS")
            st.write("Link:", "[GitHub](https://github.com/JaimeCardozo2212/Robo-extra-o-de-dados-ordem-de-servi-o.git)")
            
        with col2:
            st.write("---")
            st.write(
                """
                Robo criado para extrair dados de um sistema de ordens de serviço,
                utilizando a biblioteca Selenium para automação do navegador.
                O robô faz login no sistema, navega até a seção de ordens de serviço,
                aplica filtros específicos e extrai os dados relevantes.
                Os dados extraídos são então processados e armazenados em um banco de dados para análise posterior.
                """
            )
        st.write("---")

        # --- Projeto 5 ---
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("### Bot para jogo (TIBIA)")
            st.image(r"img/bot_runas_tibia.png", width=300)
            st.markdown("**Tecnologias:** Python, TKinter, opencv, PIL")
            st.write("Link:", "[GitHub](https://github.com/JaimeCardozo2212/Bot_Fazer_Runa.git)")
            
        with col2:
            st.write("---")
            st.write(
                """
                Bot criado para automatizar tarefas no jogo Tibia, especificamente para produzir runas.
                Utiliza bibliotecas como OpenCV para reconhecimento de imagens e PIL para manipulação de imagens.
                O bot é capaz de identificar elementos na tela do jogo, como ícones de runas e reagir a mudanças no ambiente do jogo.
                A interface gráfica foi desenvolvida com Tkinter, permitindo ao usuário configurar parâmetros como intervalo entre
                ações e quantidade de runas a serem produzidas.
                """
            )
        st.write("---")

        # --- Projeto 5 ---
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("### Bot para Curar (TIBIA)")
            st.image(r"img/bot_cura_tibia.png", width=300)
            st.markdown("**Tecnologias:** Python, TKinter, opencv, PIL")
            st.write("Link:", "[GitHub](https://github.com/JaimeCardozo2212/Bot_Curar_Tibia.git)")
            
        with col2:
            st.write("---")
            st.write(
                """
                Bot criado para automatizar a cura do personagem no jogo Tibia.
                Utiliza bibliotecas como OpenCV para reconhecimento de imagens e PIL para manipulação de imagens.
                O bot monitora a vida do personagem e utiliza poções de cura automaticamente quando a vida cai abaixo de um determinado nível.
                A interface gráfica foi desenvolvida com Tkinter, permitindo ao usuário configurar parâmetros como o nível de vida para acionar a cura e o intervalo entre verificações.
                """
            )
        st.write("---")

         