from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return BeautifulSoup(file, 'html.parser')

@app.route('/dashboard')
def home():
    header = read_html_file('frontend/components/header.html')
    sidebar = read_html_file('frontend/components/sidebar.html')
    body = read_html_file('frontend/components/sidebar.html')
    footer = read_html_file('frontend/components/sidebar.html')
    # footer_html = read_html_file('organisms/footer.html')
    return render_template('dashboard.html',sidebar=sidebar)

def main():
    app.run(debug=True,port=8625)