# ArticleAI
Write articles in bulk with Python and ChatGPT. Opensource project for generating articles, blog posts, SEO optimized texts, and much more!

Bulk Content Creation With ChatGPT: Generate multiple blog posts simultaneously, ensuring a steady stream of content for your audience.
- Customizable Prompts: Tailor ChatGPT's responses to your specific content needs and preferences, ensuring each blog post aligns with your brand voice and objectives.
- Time-Efficient: Say goodbye to writer's block and time-consuming content creation processes. With ArticleAI, produce high-quality blog posts in a fraction of the time.
- Versatile Applications: Ideal for bloggers, digital marketers, content agencies, and businesses seeking to enhance their online presence through compelling blog content.

Open Source: As a GitHub project, ArticleAI encourages collaboration and innovation, allowing users to contribute to its development and customization.
# Setup
- Run `pip install -r requirements.txt`
- Create a .txt file for your subjects, each line is a new subject. For each subject, one article (or blog post) will be written
- Create a .txt file for your custom instructions to pre-load ChatGPT with context. You can also pass in custom instructions here. Each line is a new message.

# Usage
- Run `python3 run.py --keywords_file keywords.txt --output_dir your_output_dir --messages_file messages.txt`
