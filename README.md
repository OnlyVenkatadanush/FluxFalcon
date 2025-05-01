
<h1 align="center">🐦‍🔥FluxFalcon</h1>
<p align="center">
  <img src="https://img.shields.io/badge/status-live-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Powered%20By-Groq%20%26%20OpenRouter-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/Built%20With-Streamlit-orange?style=flat-square" />
</p>

<p align="center">
  <img src="https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif" width="200" alt="AI Falcon">
</p>

<h3 align="center">🦅 Fly through models at the speed of thought.</h3>
<p align="center">An ultra-fast, dynamic AI interface that lets you fly between LLMs with zero lag and max control.</p>

<p align="center">
  <a href="https://fluxfalcon.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/Launch%20App-Click%20Here-critical?style=for-the-badge&logo=streamlit&logoColor=white" />
  </a>
  &nbsp;
  <a href="https://github.com/OnlyVenkatdanush/FluxFalcon" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-Repo-333?style=for-the-badge&logo=github" />
  </a>
</p>

---

## ✨ Features

- **Real-Time Model Switching** — Swap between OpenRouter and Groq models instantly.
- **User-Controlled Keys** — No stored data. Bring your own API keys at runtime.
- **Responsive Chat Interface** — Smooth UI built with Streamlit for optimal user experience.
- **Supports Multiple LLMs** — Test, compare, and explore various models side by side.
- **Sleek, Intuitive UI** — Styled for clarity, speed, and aesthetics.

---

## 🚀 How to Use

1. **Launch the app** → [FluxFalcon](https://fluxfalcon.streamlit.app/)
2. **Select your LLM provider** → Choose from `Groq` or `OpenRouter`.
3. **Enter your API key** (only you see it, it's not stored).
4. **Pick a model** → Like `mixtral-8x7b`, `gemma-7b-it`, `llama3`, etc.
5. **Chat away** → And if needed, switch providers without losing momentum.

---

## 🛠️ Tech Stack

| Tool       | Description                        |
|------------|------------------------------------|
| **Streamlit** | Interactive web app framework |
| **Groq API**   | Blazing-fast LLM backend      |
| **OpenRouter**| Unified access to multiple models |
| **Python**     | Backend logic and model handling |

---

## ⚙️ Local Setup

```bash
# Clone the repo
git clone https://github.com/OnlyVenkatdanush/FluxFalcon.git
cd FluxFalcon

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🔐 Security

- **No API keys are stored** — Keys are entered during runtime and used only for the session.
---

## 💡 Future Plans

- Chat history with local storage  
- Multi-user sessions  
- Voice-to-text and speech response  
- Auto model performance comparison  
- Plugin-based model extension system  

---

## 🤝 Contributing

Got ideas? Found bugs? Want to add a new model support?  
Pull requests are welcome — let’s build something epic.

```bash
# Fork it
# Create your feature branch
git checkout -b feature/new-model

# Commit your changes
git commit -m 'Add something cool'

# Push to the branch
git push origin feature/new-model

# Open a PR
```