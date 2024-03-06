# ArticleAI
# Setup
- Run `pip install -r requirements.txt`
- Create a .txt file for your subjects, each line is a new subject. For each subject, one article (or blog post) will be written
- Create a .txt file for your custom instructions to pre-load ChatGPT with context. You can also pass in custom instructions here. Each line is a new message.

# Usage
- Run `python3 run.py --keywords_file keywords.txt --output_dir your_output_dir --messages_file messages.txt`