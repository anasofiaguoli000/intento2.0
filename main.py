import streamlit as st
import requests

st.set_page_config(
    page_title="SuperMarket Express",
    page_icon="🛒",
    layout="centered"
)

API_KEY = "sk-6549f06fb6b941cea7442e5451561a58"
API_URL = "https://api.deepseek.com/v1/chat/completions"


def enviar_mensaje(mensaje):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": "Eres el asistente virtual de SuperMarket Express. Ayuda a los clientes con productos, precios, promociones y domicilios."
            },
            {
                "role": "user",
                "content": mensaje
            }
        ]
    }

    try:
        respuesta = requests.post(
            API_URL,
            headers=headers,
            json=data,
            timeout=30
        )

        if respuesta.status_code != 200:
            return "❌ Ocurrió un error al conectar con el chatbot."

        return respuesta.json()["choices"][0]["message"]["content"]

    except requests.exceptions.Timeout:
        return "⏰ El servidor tardó demasiado. Intenta nuevamente."

    except requests.exceptions.RequestException:
        return "🔌 No se pudo conectar con el servidor."


def main():

    st.title("🛒 SuperMarket Express")
    st.subheader("🤖 Asistente virtual")

    st.write(
        "Hola 👋 Soy el asistente de SuperMarket Express. "
        "Puedo ayudarte con productos, precios, promociones y domicilios."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    mensaje = st.chat_input("Escribe tu pregunta...")

    if mensaje:

        st.session_state.messages.append({
            "role": "user",
            "content": mensaje
        })

        with st.chat_message("user"):
            st.markdown(mensaje)

        with st.chat_message("assistant"):

            with st.spinner("Pensando..."):
                respuesta = enviar_mensaje(mensaje)

            st.markdown(respuesta)

        st.session_state.messages.append({
            "role": "assistant",
            "content": respuesta
        })

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Botón</title>

    <style>
        .boton {
            background-color: #2e8b57;
            color: white;
            padding: 12px 25px;
            text-decoration: none;
            border-radius: 10px;
            font-size: 18px;
            font-family: Arial, sans-serif;
            display: inline-block;
        }

        .boton:hover {
            background-color: #246b45;
        }
    </style>
</head>

<body>

    <a href="https://intento20-trlaontnnre6jxcbz2kigy.streamlit.app/" 
       class="boton" target="_blank">
        Abrir Chatbot 🤖
    </a>

</body>
</html>


if __name__ == "__main__":
    main()
