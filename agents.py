import os
from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Setup LLM (OpenRouter)
llm = LLM(
    model="openai/gpt-4o-mini",  # fast + cheap
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Define Content Writer Agent
content_writer = Agent(
    role="Content Writer",
    goal="Create engaging and informative blog posts on various topics",
    backstory=(
        "You are an experienced content writer with expertise in SEO-friendly writing. "
        "You simplify complex topics and make them engaging for readers."
    ),
    llm=llm,
    verbose=True
)