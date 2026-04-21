from crewai import Crew

from agents import content_writer
from tasks import blog_writing_task

# Define the Crew with agents and tasks
crew = Crew(
    agents=[content_writer],
    tasks=[blog_writing_task]
)

# Input
topic = "How AI is transforming Indian startups"

# Run
result = crew.kickoff(inputs={"topic": topic})

print("Response:\n", result)