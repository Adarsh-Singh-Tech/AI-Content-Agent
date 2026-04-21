from crewai import Task
from agents import content_writer

blog_writing_task = Task(
    description=(
        "Write a high-quality blog post about {topic}.\n\n"
        "Requirements:\n"
        "- 800 to 1000 words\n"
        "- Engaging and attention-grabbing introduction\n"
        "- Clear and informative subheadings\n"
        "- Use simple and easy-to-understand language\n"
        "- Include real-world examples where possible\n"
        "- Strong conclusion with key takeaways\n\n"
        "Make the blog SEO-friendly and engaging for readers."
    ),
    expected_output=(
        "A complete blog post in markdown format with:\n"
        "- Title\n"
        "- Introduction\n"
        "- Multiple sections with headings\n"
        "- Conclusion"
    ),
    agent=content_writer,
)