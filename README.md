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
## 📂 Project Structure

ai-content-agent/
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


'''
## ⚙️ Setup Instructions

### 1️⃣ Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-content-agent.git
cd ai-content-agentd
