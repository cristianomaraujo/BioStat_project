import streamlit as st
import openai
from streamlit_chat import message as msg

import os

SENHA_OPEN_AI = os.getenv("SENHA_OPEN_AI")

openai.api_key = SENHA_OPEN_AI

# URL da imagem do logo no repositório do GitHub

logo_url = "https://github.com/cristianomaraujo/BioStatBot/blob/main/Capa.jpg?raw=true"
logo_url_p = "https://github.com/cristianomaraujo/BioStatBot/blob/main/capa_p.jpg?raw=true"
logo_url_e = "https://github.com/cristianomaraujo/BioStatBot/blob/main/capa_e.jpg?raw=true"
logo_url3 = "https://github.com/cristianomaraujo/BioStatBot/blob/main/capa2.jpg?raw=true"

# Exibindo a imagem de logo
st.sidebar.image(logo_url3, use_column_width=True)

idioma = st.sidebar.radio("Idioma/Language:", ("English", "Português", "Español"))


# Defina os textos e botões com base no idioma selecionado
if idioma == "English":
    st.image(logo_url, use_column_width=True)
    abertura = st.write("Hello! I'm an AI-powered chatbot ready to assist you with Biostatistics. To start our conversation, please enter some information in the field below, or simply type 'Hi'.")
    st.sidebar.title("Tell me")
    text_input_center = st.chat_input("Chat with me")
    condicoes = ("Answer only questions related to biostatistics and statistical tests applied in health studies."
    "Ensure all questions fall within the chatbot's scope and provide guidance otherwise."
    "Ensure responses are pertinent to the user's question context and offer relevant information about statistical tests in health."
    "Utilize natural language processing (NLP) techniques to understand users' question intentions and respond accordingly."
    "Provide clear instructions on how users can interact with the chatbot and ask questions about biostatistics."
    "When appropriate, offer additional references and useful resources related to biostatistics and statistical tests in health studies."
    "Request feedback from users regularly and use this information to continuously improve the chatbot's performance and relevance."
    "Your name is Inferentia. Ask the user's name and address them by name."
    "Always before answering, check if the comparison is pre-post or between groups."
    "Always confirm whether the variable is numerical or categorical, explaining simply what each one entails."
    "Always explain with examples from health when presenting concepts."
    "When mentioned, always explain how to test assumptions."
    "Limit the response to a maximum of 3800 output tokens.")

    st.sidebar.markdown(
    """
    <style>
    .footer {
        font-size: 9px;
        text-align: center;
    }
    </style>
    <div class="footer">Project developed by the University Tuiuti do Paraná (PPGSCH/PPGO-UTP)<br>
    Developed by: Amanda Cristina Agador and Cristiano Miranda de Araujo<br>
    Contact: cristiano.araujo@utp.br<br>
    Project supported by the Coordination for the Improvement of Higher Education Personnel (CAPES)<br><br><br><br><br><br><br><br><br><br></div>
    """,
    unsafe_allow_html=True
    )

elif idioma == "Português":
    st.image(logo_url_p, use_column_width=True)
    abertura = st.write("Olá! Sou um chatbot com inteligência artificial pronto para ajudá-lo com Biostatística. Para iniciar nossa conversa, por favor, insira alguma informação no campo abaixo, ou simplesmente escreva 'Oi'.")
    st.sidebar.title("Conte-me")
    text_input_center = st.chat_input("Converse comigo")
    condicoes =  ("Responda apenas perguntas relacionadas à bioestatística e testes estatísticos aplicados em estudos de saúde."
    "Certifique-se de que todas as perguntas estejam dentro do escopo do chatbot e forneça orientações caso contrário."
    "Garanta que as respostas sejam pertinentes ao contexto da pergunta do usuário e ofereçam informações relevantes sobre testes estatísticos em saúde."
    "Utilize técnicas de processamento de linguagem natural (NLP) para entender as intenções das perguntas dos usuários e responder adequadamente."
    "Forneça instruções claras sobre como os usuários podem interagir com o chatbot e fazer perguntas sobre bioestatística."
    "Quando apropriado, ofereça referências adicionais e recursos úteis relacionados à bioestatística e testes estatísticos em estudos de saúde."
    "Solicite feedback dos usuários regularmente e use essas informações para melhorar continuamente o desempenho e a relevância do chatbot."
    "Seu nome é Inferentia. Pergunte o nome do usuário e dirija-se a ele pelo nome."
    "Sempre antes de responder, verifique se a comparação é pré-pós ou entre grupos."
    "Sempre confirme se a variável é numérica ou categórica, explicando de maneira simples o que é cada uma delas."
    "Sempre explique com exemplos da área de saúde ao apresentar conceitos."
    "Quando mencionado, sempre explique como testar pressupostos."
    "Limite a resposta a um máximo de 3800 tokens de saída.")

    ##condicoes = f"Siga essas regras durante toda nossa conversa: 1) Este chatbot está programado para responder apenas perguntas relacionadas a BIOESTATÍSTICA; 2) Aja como um chatbot, fazendo perguntas para dar a melhor orientação. 3) Se a pergunta não for relacionada com bioestatística, peça desculpas e explique que você está programado apenas para conversar sobre questões estatísticas; 4) Pergunte o nome do usuário e o chame pelo nome;  5) Utilize os termos, linguagem e exemplos apropriados para área de saúde;  6) Seu nome é Inferentia. Se apresente ao iniciar a conversa; 7) Inicie a conversa após saber o nome do usuário, se o usuário não te informar uma resposta para o tamanho da amostra planejada, a quantidade de grupos, a variável (se categórica ou numérica) que pretende utilizar para a comparação estatística, e a principal dúvida, por favor solicite a informação. 8) É aceitável o usuário não saber ainda o tamanho da amostra. Contudo, as outras informações são essenciais."

    st.sidebar.markdown(
    """
    <style>
    .footer {
        font-size: 9px;
        text-align: center;
    }
    </style>
    <div class="footer">Projeto desenvolvido pela Universidade Tuiuti do Paraná (PPGSCH/PPGO-UTP)<br>
    Desenvolvido por: Amanda Cristina Agador e Cristiano Miranda de Araujo<br>
    Contato: cristiano.araujo@utp.br<br>
    Projeto apoiado pela Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES)<br><br><br><br><br><br><br><br><br><br></div>
    """,
    unsafe_allow_html=True
    )

else:
    st.image(logo_url_e, use_column_width=True)
    abertura = st.write("¡Hola! Soy un chatbot con inteligencia artificial listo para ayudarte con Biostadística. Para comenzar nuestra conversación, por favor, ingresa alguna información en el campo a continuación, o simplemente escribe 'Hola'.")
    st.sidebar.title("Cuéntame")
    text_input_center = st.chat_input("Charla conmigo")
    condicoes = ("Responde solo preguntas relacionadas con bioestadística y pruebas estadísticas aplicadas en estudios de salud."
    "Asegúrate de que todas las preguntas estén dentro del alcance del chatbot y proporciona orientación en caso contrario."
    "Asegúrate de que las respuestas sean pertinentes al contexto de la pregunta del usuario y ofrece información relevante sobre las pruebas estadísticas en salud."
    "Utiliza técnicas de procesamiento de lenguaje natural (NLP) para comprender la intención detrás de las preguntas de los usuarios y responde en consecuencia."
    "Proporciona instrucciones claras sobre cómo los usuarios pueden interactuar con el chatbot y hacer preguntas sobre bioestadística."
    "Cuando sea apropiado, ofrece referencias adicionales y recursos útiles relacionados con la bioestadística y las pruebas estadísticas en estudios de salud."
    "Solicita comentarios de los usuarios regularmente y utiliza esta información para mejorar continuamente el rendimiento y la relevancia del chatbot."
    "Tu nombre es Inferentia. Pregunta el nombre del usuario y dirígete a él por su nombre."
    "Siempre antes de responder, verifique si la comparación es pre-post o entre grupos. "
    "Siempre confirma si la variable es numérica o categórica, explicando de manera simple qué significa cada una."
    "Siempre explique con ejemplos de salud al presentar conceptos."
    "Cuando se mencione, siempre explique cómo probar los supuestos."
    "Limite la respuesta a un máximo de 3800 tokens de salida.")

    st.sidebar.markdown(
    """
    <style>
    .footer {
        font-size: 9px;
        text-align: center;
    }
    </style>
    <div class="footer">Proyecto desarrollado por la Universidad Tuiuti do Paraná (PPGSCH/PPGO-UTP)<br>
    Desarrollado por: Amanda Cristina Agador y Cristiano Miranda de Araujo<br>
    Contacto: cristiano.araujo@utp.br<br>
    Proyecto apoyado por la Coordinación de Perfeccionamiento del Personal de Nivel Superior (CAPES)<br><br><br><br><br><br><br><br><br><br></div>
    """,
    unsafe_allow_html=True
    )

# Criação da função para renderizar a conversa com barra de rolagem
def render_chat(hst_conversa):
    for i in range(1, len(hst_conversa)):
        if i % 2 == 0:
            msg("**BSBot**:" + hst_conversa[i]['content'])
        else:
            msg("**Você**:" + hst_conversa[i]['content'], is_user=True)

    # Código para a barra de rolagem
    st.session_state['rendered'] = True
    if st.session_state['rendered']:
        script = """
        const chatElement = document.querySelector('.streamlit-chat');
        chatElement.scrollTop = chatElement.scrollHeight;
        """
        st.session_state['rendered'] = False
        st.write('<script>{}</script>'.format(script), unsafe_allow_html=True)
#########################

st.write("***")


if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = [{"role": "user", "content": condicoes}]

if text_input_center:
    st.session_state.hst_conversa.append({"role": "user", "content": text_input_center})
    retorno_openai = openai.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=st.session_state.hst_conversa,
        max_tokens=500,
        n=1
    )
    st.session_state.hst_conversa.append({"role": "assistant", "content": retorno_openai['choices'][0]['message']['content']})



######RENDERIZAÇÃO DA CONVERSA
if len(st.session_state.hst_conversa) > 1:
    render_chat(st.session_state.hst_conversa)
