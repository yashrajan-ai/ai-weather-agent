# 🌤️ AI Weather Agent

> 🤖 **Your intelligent weather assistant — ask about any city and get real-time weather information.**

An AI-powered weather agent that understands natural-language queries, identifies the requested city, fetches **current weather information**, and presents the result in a simple conversational format.

🚀 **My First AI Agent Project**

---

## ✨ Live Demo

🔗 **Try the AI Weather Agent:**
👉 **[Live Demo]([https://ai-weather-agent.streamlit.app/](https://ai-weather-agent.streamlit.app/))**

---

## 🎥 What Can It Do?

Instead of searching through a weather website, simply ask:

```text
🌦️ What's the weather in Patna?
```

or

```text
☀️ Tell me the current weather in Delhi
```

or

```text
🌧️ Is it raining in Mumbai right now?
```

The agent processes your request and provides the relevant weather information.

---

## 🧠 How It Works

```text
          👤 User
             │
             ▼
      💬 Natural Language
             │
             ▼
      🤖 AI Weather Agent
             │
       ┌─────┴─────┐
       │           │
       ▼           ▼
   Understand    Identify
     Query        City
       │           │
       └─────┬─────┘
             ▼
       🛠️ Weather Tool
             │
             ▼
       🌐 Weather API
             │
             ▼
       📊 Current Data
             │
             ▼
       🤖 AI Response
             │
             ▼
          👤 User
```

---

## 🚀 Features

| Feature             | Description                                  |
| ------------------- | -------------------------------------------- |
| 🤖 AI Agent         | Uses an AI model to understand user requests |
| 🌍 Any City         | Ask about weather in different cities        |
| 🌡️ Current Weather | Retrieves current weather conditions         |
| 💬 Natural Language | No fixed commands required                   |
| 🛠️ Tool Calling    | Agent uses a weather tool when needed        |
| ⚡ Fast Response     | Quickly processes weather queries            |
| 🖥️ Interactive UI  | Simple and user-friendly Streamlit interface |
| 🔐 Secure API Keys  | Secrets are stored securely                  |

---

## 🛠️ Tech Stack

### 🤖 AI / Agent

* Python
* LangChain
* Large Language Model
* Tool Calling

### 🌐 Weather

* Weather API
* Real-time weather data

### 🖥️ Frontend

* Streamlit

### 🔧 Development

* Git
* GitHub
* VS Code / PyCharm

---

## 📂 Project Structure

```text
ai-weather-agent/
│
├── app.py                 # 🌐 Streamlit application
├── weather_agent.py       # 🤖 AI agent logic
├── requirements.txt       # 📦 Project dependencies
├── README.md              # 📖 Documentation
│
├── .streamlit/
│   └── secrets.toml       # 🔐 API keys
│
└── .gitignore             # 🚫 Ignored files
```

> 📌 Your actual structure may differ depending on how you organized the project.

---

## 💬 Example Queries

Try asking:

```text
🌤️ What's the weather in Patna?
```

```text
🌡️ What is the temperature in Delhi?
```

```text
🌧️ What's the current weather in Mumbai?
```

```text
☁️ Is it cloudy in Bangalore?
```

```text
🌍 Tell me the weather conditions in London.
```

---

## 🧪 Example Response

**User:**

> What's the weather in Patna?

**AI Weather Agent:**

```text
🌤️ Current Weather in Patna

🌡️ Temperature: 32°C
☁️ Condition: Partly Cloudy
💧 Humidity: 58%
💨 Wind Speed: 5 km/h
🧭 Wind Direction: East
```

---

## 🔄 Agent Workflow

The project follows a simple agentic workflow:

### 1️⃣ User Query

The user asks a weather-related question.

### 2️⃣ Query Understanding

The LLM analyzes the request and determines what information is required.

### 3️⃣ Tool Selection

The agent decides whether it needs to call the weather tool.

### 4️⃣ API Call

The weather tool retrieves current weather information.

### 5️⃣ Response Generation

The AI interprets the returned data and generates a human-readable response.

---

## 🔐 Environment Variables

Create a `.env` file for local development:

```env
OPENAI_API_KEY=your_api_key
WEATHER_API_KEY=your_weather_api_key
```

If you're using Streamlit Cloud, store your credentials in:

```text
Settings → Secrets
```

⚠️ **Never upload API keys to GitHub.**

---

## ⚙️ Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yashrajan-ai/ai-weather-agent.git
```

### 2️⃣ Move into the project

```bash
cd ai-weather-agent
```

### 3️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Add your API keys

Configure your environment variables or Streamlit secrets.

### 6️⃣ Run the application

```bash
streamlit run app.py
```

Then open the local URL shown by Streamlit.

---

## ☁️ Deployment

This project can be deployed easily using **Streamlit Community Cloud**.

```text
GitHub Repository
       │
       ▼
Streamlit Cloud
       │
       ▼
   Deploy 🚀
       │
       ▼
 Live AI Weather Agent 🌤️
```

---

## 📈 Future Improvements

I'm planning to extend the project with:

* 📅 Weather forecasting
* 🌧️ Rain probability
* 🌡️ Temperature forecasts
* 🌍 Weather comparison between cities
* 📊 Interactive weather charts
* 🗺️ Location-based weather
* 💬 Conversation memory
* 🎙️ Voice input
* 🌐 Multi-language support
* 🤖 More advanced agentic workflows

---

## 🎯 Why I Built This

This project was built as my **first practical AI Agent project** to understand how AI models can interact with external tools and real-world APIs.

Through this project, I explored concepts such as:

```text
LLMs
  ↓
Prompting
  ↓
Agents
  ↓
Tool Calling
  ↓
APIs
  ↓
Real-Time Data
  ↓
AI Application
```

The goal was to move beyond simply using an LLM and build an application where an AI agent can **reason about a request and use an external tool to retrieve real-world information.**

---

## 📚 What I Learned

### 🤖 AI & LLM

* LLM integration
* Prompt engineering
* Agent workflows
* Tool calling

### 🐍 Python

* API integration
* Environment variables
* Error handling
* Application structure

### 🌐 Deployment

* Streamlit
* Git & GitHub
* Cloud deployment
* Secrets management

---

## 👨‍💻 About Me

Hi! I'm **Yash Rajan**, an aspiring **AI/ML Engineer** passionate about building practical AI applications.

I'm currently exploring:

```text
🤖 Artificial Intelligence
🧠 Machine Learning
🔗 LLMs
🛠️ AI Agents
📚 RAG
🐍 Python
💻 Data Structures & Algorithms
```

I enjoy turning AI concepts into real-world projects and continuously learning new technologies.

---

## 🌐 Connect With Me

<p align="center">

<a href="https://github.com/yashrajan-ai">
<img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

<a href="https://www.linkedin.com/in/yashrajan1">
<img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

</p>

---

## ⭐ Support

If you found this project interesting:

⭐ **Star the repository**

🍴 **Fork the project**

💡 **Share your feedback**

---

<div align="center">

### 🌤️ Ask. Analyze. Get the Weather.

**Built with ❤️ and 🤖 by Yash Rajan**

⭐ If you like this project, consider giving it a star!

</div>

