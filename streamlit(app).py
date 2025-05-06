import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="chef-GPT",
    page_icon="🧑‍🍳",
    layout="centered",
)

# --- Sidebar Navigation ---
st.sidebar.title("🍴 Chef-GPT Menu")
page = st.sidebar.radio(
    "Navigate",
    ["🍳 Home", "📜 Recipes", "📝 Saved Chats", "📦 Ingredients", "⚙ Settings"]
)

# --- Styling ---
st.markdown(
    """
    <style>
        .main-title {
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            color: #4CAF50;
        }
        .subtitle {
            font-size: 1.2em;
            text-align: center;
            color: #666;
        }
        .chat-box {
            background-color: #f1f1f1;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Page Header ---
st.markdown('<div class="main-title">Welcome to Chef-GPT 🧑‍🍳</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your friendly AI assistant, always ready to chat!</div>', unsafe_allow_html=True)
st.markdown("---")

# --- Show content based on sidebar selection ---
if page == "🍳 Home":
    # --- Chatbot UI ---

    # --- Initialize chat history ---
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # --- Display chat history ---
    for msg in st.session_state.messages:
        with st.container():
            role = "🧑 You" if msg["role"] == "user" else "🤖 Bot"
            st.markdown(f'<div class="chat-box"><strong>{role}:</strong> {msg["content"]}</div>', unsafe_allow_html=True)

    # --- Chat Input Area ---
    st.markdown("*Chat with Chef-GPT:*")
    input_col, mic_col, send_col = st.columns([10, 1, 1])

    with input_col:
        user_input = st.text_input("Type your message...", key="input_text", label_visibility="collapsed")

    with mic_col:
        mic_clicked = st.button("🎙", help="Voice input coming soon")

    with send_col:
        send_clicked = st.button("▶", help="Send message")

    # --- Handle Send Button ---
    if send_clicked:
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            bot_response = f"You said: {user_input}"  # Placeholder response
            st.session_state.messages.append({"role": "bot", "content": bot_response})
            st.session_state.input_text = ""

    # --- Handle Mic Button ---
    if mic_clicked:
        st.info("🎤 Voice input feature coming soon!")

elif page == "📜 Recipes":
    st.subheader("🍽 Your AI Recipes")
    st.info("Feature coming soon: Chef-GPT will help you generate and store your custom recipes!")

elif page == "📝 Saved Chats":
    st.subheader("💬 Saved Chats")
    st.warning("No chats saved yet. This feature is coming soon!")

elif page == "📦 Ingredients":
    st.subheader("🧂 Ingredient Manager")
    st.info("Soon you’ll be able to manage your pantry and let Chef-GPT generate recipes based on what you have!")

elif page == "⚙ Settings":
    st.subheader("⚙ App Settings")
    st.info("Customize your experience here — dark mode, language, preferences... coming soon!")

# --- Footer ---
st.markdown("---")
st.markdown("© 2025 Chef-GPT. Powered by Streamlit + AI", unsafe_allow_html=True)