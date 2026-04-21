from crewai import Crew
from agents import content_writer
from tasks import blog_writing_task
import datetime

crew = Crew(
    agents=[content_writer],
    tasks=[blog_writing_task]
)

topic = "How AI is transforming Indian startups"

result = crew.kickoff(inputs={"topic": topic})

# Print output
print("\nFINAL OUTPUT:\n")
print(result)

# Create dynamic filename
filename = f"blog_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

# Save as Markdown file
with open(filename, "w", encoding="utf-8") as f:
    f.write(str(result))

print(f"\n✅ Blog saved as {filename}")