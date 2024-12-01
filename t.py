import streamlit as st

# Inicializa o histórico de mensagens e feedback
if "messages" not in st.session_state:
    st.session_state.messages = []

if "feedback" not in st.session_state:
    st.session_state.feedback = {}

# Exibe as mensagens anteriores
for idx, message in enumerate(st.session_state.messages):
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

    # Exibe botões de feedback para as respostas do chatbot
    if message["role"] == "assistant":
        feedback_options = ["👍 Bom", "👎 Ruim"]
        feedback = st.radio(f"Dê seu feedback para a resposta {idx + 1}:", feedback_options, key=f"feedback_{idx}")
        
        # Armazena o feedback na sessão
        if feedback:
            st.session_state.feedback[idx] = feedback
            st.write(f"Feedback recebido: {feedback}")

# Aceita a entrada do usuário
if user_input := st.chat_input("Digite sua mensagem"):
    # Exibe a mensagem do usuário
    with st.chat_message("user"):
        st.markdown(user_input)

    # Adiciona ao histórico
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Resposta do chatbot (aqui está apenas ecoando a entrada do usuário)
    bot_response = f"Você disse: {user_input}"
    with st.chat_message("assistant"):
        st.markdown(bot_response)

    # Adiciona a resposta do chatbot ao histórico
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
