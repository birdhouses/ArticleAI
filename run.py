import argparse
from src.write_articles import BlogPostGenerator

def main():
    parser = argparse.ArgumentParser(description='Generate blog posts from keywords (subjects for articles).')
    parser.add_argument('--keywords_file', type=str, required=True, help='Text file with the keywords')
    parser.add_argument('--output_dir', type=str, required=True, help='Directory to save blog posts')
    parser.add_argument('--messages_file', type=str, required=True, help='Text file containing messages for OpenAI')

    args = parser.parse_args()

    with open(args.messages_file, 'r', encoding='utf-8') as messages_file:
        messages_content = messages_file.readlines()

    messages = [{"role": "system", "content": message.strip()} for i, message in enumerate(messages_content)]

    with open(args.keywords_file, 'r', encoding='utf-8') as keywords_file:
        keywords = keywords_file.readlines()


    generator = BlogPostGenerator(messages=messages, keywords=keywords, output_directory=args.output_dir)
    generator.write_articles()

if __name__ == "__main__":
    main()
