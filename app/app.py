from flask import Flask, render_template, abort
import markdown
import os
import frontmatter
from datetime import datetime

app = Flask(__name__)

def get_markdown_content(file_path):
    try:
        post = frontmatter.load(file_path)
        content = markdown.markdown(post.content, extensions=['extra'])
        metadata = post.metadata
        return content, metadata
    except Exception as e:
        print(f"Error loading markdown file: {e}")
        return None, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/knowledge')
def knowledge():
    articles = []
    knowledge_dir = os.path.join(app.root_path, 'content', 'knowledge')
    
    for filename in os.listdir(knowledge_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(knowledge_dir, filename)
            content, metadata = get_markdown_content(file_path)
            if content and metadata:
                articles.append({
                    'slug': filename[:-3],
                    'title': metadata.get('title', 'Untitled'),
                    'description': metadata.get('description', ''),
                    'date': metadata.get('date', datetime.now().strftime('%Y-%m-%d')),
                    'category': metadata.get('category', 'General')
                })
    
    return render_template('knowledge.html', articles=articles)

@app.route('/knowledge/<slug>')
def article(slug):
    file_path = os.path.join(app.root_path, 'content', 'knowledge', f'{slug}.md')
    if not os.path.exists(file_path):
        abort(404)
    
    content, metadata = get_markdown_content(file_path)
    if not content:
        abort(404)
    
    return render_template('article.html', content=content, metadata=metadata)

@app.route('/emotion')
def emotion():
    return render_template('coming_soon.html', title='宠物表情识别')

@app.route('/map')
def map():
    return render_template('coming_soon.html', title='宠物地图')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)