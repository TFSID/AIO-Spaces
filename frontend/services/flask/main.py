from flask import Flask, render_template
from bs4 import BeautifulSoup

# app = Flask(__name__, static_url_path='/static')

app = Flask(__name__,template_folder='../../view',static_url_path='/frontend/public')

@app.route('/')
def hello():
    return 'Hello, World!'

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return BeautifulSoup(file, 'html.parser')

@app.route('/dashboard')
def home():
    
    navbar = render_template('components/navbar.html')
    header = render_template('components/header.html')
    sidebar = render_template('components/sidebar.html')
    footer = render_template('components/footer.html')
    # import dashboard pages
    template = render_template('pages/dashboard.html',sidebar=sidebar, header=header, navbar=navbar,footer=footer)
    return template
@app.route('/asset-pelindo')
def assetpelindo():
    
    navbar = render_template('components/navbar.html')
    header = render_template('components/header.html')
    sidebar = render_template('components/sidebar.html')
    footer = render_template('components/footer.html')
    content = render_template('pages/asset-and-event/asset-pelindo.html')
    # import dashboard pages
    template = render_template('pages/layout.html',sidebar=sidebar, header=header, navbar=navbar,footer=footer,content=content)
    return template

def main():
    app.run(debug=True,port=8625)