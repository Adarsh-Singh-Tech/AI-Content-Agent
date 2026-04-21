# 🧠 AI Content Writer Agent (CrewAI + OpenRouter)

An AI-powered content generation system built using CrewAI and OpenRouter.  
This project uses autonomous agents to generate high-quality, structured blog content.

---

## 🚀 Features

- 🤖 AI Content Writer Agent
- 🧩 CrewAI-based multi-agent architecture (extensible)
- ✍️ Generates 800–1000 word blog posts
- 📄 Outputs saved automatically in Markdown (.md)
- ⚡ Fast & cost-efficient using OpenRouter (GPT-4o-mini)

---

## 🛠 Tech Stack

- Python 3.11
- CrewAI
- OpenRouter API
- dotenv

---
### 📂 Project Structure

'''ai-content-agent/
│
├── app/
│   ├── main.py              # Entry point
│   ├── agents/
│   │   └── content_writer.py
│   ├── tasks/
│   │   └── blog_task.py
│
├── outputs/
│   └── blog_*.md            # Generated blogs
│
├── config/
│   └── settings.py          # Future configs (optional)
│
├── .env                     # API keys (ignored)
├── .gitignore
├── requirements.txt
├── README.md
└── mainbk.py                # Backup (optional)

<img width="481" height="395" alt="Screenshot 2026-04-21 at 11 11 16 PM" src="https://github.com/user-attachments/assets/33a5a5e9-5038-4670-ad18-4274d4c173df" />

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo

bash
git clone https://github.com/YOUR_USERNAME/ai-content-agent.git
cd ai-content-agentd

### Create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate

### Install dependencies
pip install crewai openai python-dotenv

### Setup environment variables
Create a .env file:
OPENROUTER_API_KEY=your_api_key_here

### Run the project
python main.py

### Output
Blog is generated and saved as:
blog_YYYYMMDD_HHMMSS.md

### Cost Efficiency
Uses gpt-4o-mini (low cost model)
Approx ₹0.2 – ₹1 per blog generation

### Future Improvements
🔍 Research Agent (multi-agent system)
📝 Editor/Proofreading Agent
🌐 Web UI (Streamlit / React)
🚀 API deployment (FastAPI)
💼 SaaS integration

## ⚠️ Notes
.env file is excluded for security
Do not expose API keys publicly

### Author

Adarsh Singh Gautam
Building AI-powered SaaS applications

### If you like this project
Give it a star ⭐ on GitHub!
