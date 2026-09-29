import os
import re
import requests
import streamlit as st

from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_STACK_API_KEY")

st.set_page_config(
    page_title="WeatherAI Agent",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =========================================================
# VISIBILITY-FIRST CSS
# =========================================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8fbff 0%, #eef6ff 50%, #f8faff 100%) !important;
    color: #0f172a !important;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

html, body, [class*="css"] {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
                 Helvetica, Arial, sans-serif !important;
}

.main p,
.main li,
.main label {
    color: #0f172a;
}

.stMarkdown,
.stMarkdown p,
.stMarkdown li {
    color: #0f172a !important;
}

/* HERO */
.hero-box {
    background: linear-gradient(135deg, #0f172a 0%, #172554 50%, #1e3a5f 100%);
    padding: 42px;
    border-radius: 26px;
    margin-bottom: 30px;
    color: #ffffff !important;
    box-shadow: 0 18px 45px rgba(15, 23, 42, 0.18);
}

.hero-title {
    font-size: 44px;
    font-weight: 800;
    color: #ffffff !important;
    margin-bottom: 10px;
    line-height: 1.2;
}

.hero-subtitle {
    font-size: 18px;
    color: #dbeafe !important;
    line-height: 1.6;
}

/* FEATURE CARDS */
.feature-card {
    background: #ffffff !important;
    padding: 26px;
    border-radius: 20px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 8px 25px rgba(15, 23, 42, 0.07);
    min-height: 175px;
}

.feature-icon {
    font-size: 36px;
    margin-bottom: 12px;
}

.feature-title {
    font-size: 20px;
    font-weight: 700;
    color: #0f172a !important;
    margin-bottom: 8px;
}

.feature-description {
    font-size: 15px;
    color: #475569 !important;
    line-height: 1.6;
}

/* HEADINGS */
.section-heading {
    font-size: 27px;
    font-weight: 750;
    color: #0f172a !important;
    margin-top: 35px;
    margin-bottom: 15px;
}

/* SIDEBAR */
section[data-testid="stSidebar"],
section[data-testid="stSidebar"] > div {
    background: #0f172a !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] h4,
section[data-testid="stSidebar"] .stMarkdown,
section[data-testid="stSidebar"] .stMarkdown p,
section[data-testid="stSidebar"] .stMarkdown li {
    color: #ffffff !important;
}

section[data-testid="stSidebar"] small {
    color: #cbd5e1 !important;
}

/* SIDEBAR BUTTONS */
section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    background: #1e293b !important;
    color: #f8fafc !important;
    border: 1px solid #334155 !important;
    border-radius: 12px;
    font-weight: 600;
}

section[data-testid="stSidebar"] .stButton > button p,
section[data-testid="stSidebar"] .stButton > button span {
    color: #f8fafc !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: #334155 !important;
    color: #ffffff !important;
}

/* MAIN BUTTONS */
.stButton > button {
    border-radius: 12px;
    font-weight: 600;
}

.stButton > button p,
.stButton > button span {
    color: #0f172a !important;
}

/* CHAT - explicit high-contrast text colors */
[data-testid="stChatMessage"] {
    border-radius: 18px;
    margin-bottom: 10px;
}

/* Assistant messages: dark text on the light page background. */
[data-testid="stChatMessage"] .stMarkdown,
[data-testid="stChatMessage"] .stMarkdown p,
[data-testid="stChatMessage"] .stMarkdown li,
[data-testid="stChatMessage"] .stMarkdown ul,
[data-testid="stChatMessage"] .stMarkdown ol,
[data-testid="stChatMessage"] .stMarkdown span,
[data-testid="stChatMessage"] .stMarkdown div {
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
}

[data-testid="stChatMessage"] strong,
[data-testid="stChatMessage"] b {
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
}

[data-testid="stChatMessage"] em,
[data-testid="stChatMessage"] i {
    color: #334155 !important;
    -webkit-text-fill-color: #334155 !important;
}

[data-testid="stChatMessage"] h1,
[data-testid="stChatMessage"] h2,
[data-testid="stChatMessage"] h3,
[data-testid="stChatMessage"] h4,
[data-testid="stChatMessage"] h5,
[data-testid="stChatMessage"] h6 {
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
}

/* Keep user messages readable against their gray bubble. */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) .stMarkdown,
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) .stMarkdown p,
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) .stMarkdown li,
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) .stMarkdown span,
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) .stMarkdown div {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

[data-testid="stChatMessage"] code {
    background: #e2e8f0 !important;
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
}

[data-testid="stChatMessage"] pre {
    background: #0f172a !important;
    color: #f8fafc !important;
    border-radius: 10px;
    padding: 15px;
}

[data-testid="stChatMessage"] pre code {
    background: transparent !important;
    color: #f8fafc !important;
    -webkit-text-fill-color: #f8fafc !important;
}

[data-testid="stChatMessage"] a {
    color: #1d4ed8 !important;
    -webkit-text-fill-color: #1d4ed8 !important;
}

/* CHAT INPUT */
[data-testid="stChatInput"] {
    background: transparent !important;
}

[data-testid="stChatInput"] textarea {
    background: #ffffff !important;
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 15px !important;
    font-size: 16px !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #64748b !important;
    -webkit-text-fill-color: #64748b !important;
    opacity: 1 !important;
}

[data-testid="stChatInput"] button,
[data-testid="stChatInput"] button svg {
    color: #0f172a !important;
}

/* STATUS */
[data-testid="stStatus"] {
    border-radius: 14px !important;
}

[data-testid="stStatus"] p,
[data-testid="stStatus"] span {
    color: #334155 !important;
}

/* DIVIDER */
hr {
    border-color: #e2e8f0 !important;
}

/* FOOTER */
.footer {
    text-align: center;
    color: #64748b !important;
    margin-top: 50px;
    padding-top: 25px;
    border-top: 1px solid #e2e8f0;
    line-height: 1.6;
}

.footer b {
    color: #334155 !important;
}

/* MOBILE */
@media (max-width: 768px) {
    .hero-box {
        padding: 28px;
        border-radius: 20px;
    }

    .hero-title {
        font-size: 32px;
    }

    .hero-subtitle {
        font-size: 16px;
    }

    .feature-card {
        margin-bottom: 15px;
    }

    .section-heading {
        font-size: 23px;
    }
}
</style>
""", unsafe_allow_html=True)

if not GEMINI_API_KEY or not WEATHER_API_KEY:
    st.error(
        "API keys are missing. Please configure "
        "GEMINI_API_KEY (or GOOGLE_API_KEY) and WEATHER_STACK_API_KEY."
    )
    st.stop()


@tool
def get_weather_data(city: str) -> str:
    """
    Get current weather information for a city.
    Use this tool for current weather, temperature, humidity,
    wind, weather conditions, feels-like temperature and UV index.
    """
    try:
        url = (
            "http://api.weatherstack.com/current"
            f"?access_key={WEATHER_API_KEY}"
            f"&query={city}"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "error" in data:
            error_info = data.get("error", {})
            return (
                "Weather API error: "
                + error_info.get(
                    "info",
                    "Unable to retrieve weather data."
                )
            )

        location = data.get("location", {})
        current = data.get("current", {})

        descriptions = current.get(
            "weather_descriptions",
            ["Unknown"]
        )

        description = descriptions[0] if descriptions else "Unknown"

        return f"""
City: {location.get("name", city)}
Country: {location.get("country", "Unknown")}

Temperature: {current.get("temperature", "N/A")}°C
Feels Like: {current.get("feelslike", "N/A")}°C
Condition: {description}
Humidity: {current.get("humidity", "N/A")}%
Wind Speed: {current.get("wind_speed", "N/A")} km/h
Wind Direction: {current.get("wind_dir", "N/A")}
UV Index: {current.get("uv_index", "N/A")}
"""

    except requests.exceptions.Timeout:
        return "The weather service took too long to respond. Please try again."

    except requests.exceptions.RequestException as e:
        return f"Unable to connect to the weather service: {str(e)}"

    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


@st.cache_resource
def initialize_agent():
    # Gemini Developer API has a free tier for eligible models/projects.
    # We use Gemini 2.5 Flash-Lite because it is lightweight and well-suited
    # to a simple weather agent.
    chat_model = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        google_api_key=GEMINI_API_KEY,
        temperature=0,
    )

    prompt = PromptTemplate.from_template(
        """Answer the following question as a helpful weather assistant.

You have access to the following tool:

{tools}

Use the following format:

Question: the input question you must answer
Thought: think about what you need to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (repeat Thought/Action/Action Input/Observation as needed)
Thought: I now know the final answer
Final Answer: the answer to the user

Important rules:
- For current weather questions, use get_weather_data before answering.
- Do not invent weather values.
- Give a concise, natural-language answer using the tool result.
- If the tool reports an error, explain that error instead of making up data.

Question: {input}
Thought: {agent_scratchpad}"""
    )

    agent = create_react_agent(
        llm=chat_model,
        tools=[get_weather_data],
        prompt=prompt,
        stop_sequence=False,
    )

    return AgentExecutor(
        agent=agent,
        tools=[get_weather_data],
        verbose=False,
        handle_parsing_errors=True,
        max_iterations=5,
    )


try:
    agent_executor = initialize_agent()
except Exception as e:
    st.error(f"Failed to initialize the AI agent: {str(e)}")
    st.stop()


if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center; padding:10px 0 20px 0;">
            <div style="font-size:45px;">🌤️</div>
            <h2 style="color:#ffffff !important; margin:0;">
                WeatherAI
            </h2>
            <p style="color:#cbd5e1 !important;">
                AI-powered weather assistant
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<h3 style="color:#ffffff !important;">📍 Quick Cities</h3>',
        unsafe_allow_html=True,
    )

    for city in [
        "Patna",
        "Delhi",
        "Mumbai",
        "Bangalore",
        "Kolkata",
        "Hyderabad",
    ]:
        if st.button(city, use_container_width=True):
            st.session_state.quick_city = city

    st.markdown("---")

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown(
        """
        <div style="
            margin-top:25px;
            padding:15px;
            background:#1e293b;
            border-radius:12px;
            color:#cbd5e1 !important;
            font-size:13px;
        ">
            <b style="color:#ffffff !important;">🤖 AI Agent</b>
            <br><br>
            Powered by:
            <br>• LangChain
            <br>• Google Gemini
            <br>• WeatherStack
            <br>• Streamlit
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# HERO
# =========================================================

st.html("""
<div class="hero-box">
    <div class="hero-title">🌤️ WeatherAI Agent</div>
    <div class="hero-subtitle">
        Ask about the current weather of any city
        and let an AI agent fetch the latest
        weather information for you.
    </div>
</div>
""")


# =========================================================
# FEATURES
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.html("""
    <div class="feature-card">
        <div class="feature-icon">🌍</div>
        <div class="feature-title">Any City</div>
        <div class="feature-description">
            Get current weather information
            for cities around the world.
        </div>
    </div>
    """)

with col2:
    st.html("""
    <div class="feature-card">
        <div class="feature-icon">🤖</div>
        <div class="feature-title">AI Agent</div>
        <div class="feature-description">
            LangChain decides when to use
            the weather tool and generates
            a natural-language response.
        </div>
    </div>
    """)

with col3:
    st.html("""
    <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <div class="feature-title">Live Data</div>
        <div class="feature-description">
            Weather information is retrieved
            directly from the WeatherStack API.
        </div>
    </div>
    """)


st.markdown(
    '<div class="section-heading">💬 Ask WeatherAI</div>',
    unsafe_allow_html=True,
)


# =========================================================
# CHAT HISTORY
# =========================================================

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


quick_city = st.session_state.pop("quick_city", None)

user_prompt = st.chat_input(
    "Ask about the weather... e.g. What's the weather in Patna?"
)

if quick_city:
    user_prompt = f"What is the current weather in {quick_city}?"


# =========================================================
# PROCESS QUERY
# =========================================================

if user_prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        try:
            with st.spinner("🌤️ Checking the weather..."):
                result = agent_executor.invoke(
                    {"input": user_prompt}
                )

            output = result.get(
                "output",
                "Sorry, I couldn't generate a response."
            )

            # Keep the model response intact.
            # The CSS above controls its text color for reliable visibility.
            output = str(output).strip()

            st.markdown(output)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": output,
                }
            )

        except Exception as e:
            error_message = (
                "Sorry, something went wrong while "
                f"processing your request.\n\n"
                f"Error: {str(e)}"
            )

            st.error(error_message)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_message,
                }
            )


# =========================================================
# FOOTER
# =========================================================

st.html("""
<div class="footer">
    Built with ❤️ using
    <b>LangChain</b>,
    <b>Google Gemini</b>,
    <b>WeatherStack</b>
    and
    <b>Streamlit</b>.
    <br><br>
    Weather data provided by WeatherStack.
</div>
""")
