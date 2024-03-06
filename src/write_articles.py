import openai
import os
import re
from dotenv import load_dotenv

class BlogPostGenerator:
    def __init__(self, messages, keywords, output_directory):
        self.messages = messages
        self.keywords = keywords
        self.output_directory = output_directory

        os.makedirs(self.output_directory, exist_ok=True)
        load_dotenv()

        self.api_key = os.getenv('OPENAI_API_KEY')
        self.language = os.getenv('LANGUAGE')
        self.model = os.getenv('OPENAI_MODEL')

    def normalize_filename(self, title):
        filename = title.replace(' ', '_')
        filename = re.sub(r'[<>:"/\\|?*]', '', filename)
        max_length = 255
        if len(filename) > max_length:
            filename = filename[:max_length]
        return filename + '.txt'

    def generate_blog_post(self, keyword, messages = []):
        messages.append({"role": "system", "content": "You are a content writer expert in writing SEO-optimized blog posts."})
        messages.append({"role": "system", "content": "Respond only with the blog post. Your output should NEVER contain your own output."})
        messages.append({"role": "user", "content": f"Write an SEO-optimized 1000-word blog post in {self.language}, with SEO keyword: {keyword}."})

        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        content = response.choices[0].message.content
        return content

    def write_articles(self):
        for keyword in self.keywords:
            blog_post_content = self.generate_blog_post(keyword, messages=self.messages)

            file_name = self.normalize_filename(keyword)

            file_path = os.path.join(self.output_directory, file_name)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"# {keyword}\n\n{blog_post_content}")

            print(f"Blog post for '{keyword}' saved to {file_path}")

        print("All blog posts have been saved.")

