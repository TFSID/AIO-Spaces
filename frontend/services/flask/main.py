from flask import Flask, render_template
from bs4 import BeautifulSoup
from waitress import serve


# app = Flask(__name__, static_url_path='/static')

app = Flask(__name__,template_folder='../../view',static_url_path='/public',static_folder='../../public')

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
@app.route('/event-create')
def create_event():
    
    navbar = render_template('components/navbar.html')
    header = render_template('components/header.html')
    sidebar = render_template('components/sidebar.html')
    footer = render_template('components/footer.html')
    content = render_template('pages/asset-and-event/event-create.html')
    # import dashboard pages
    template = render_template('pages/layout.html',sidebar=sidebar, header=header, navbar=navbar,footer=footer,content=content)
    return template

@app.route('/discord-create')
def create_event_discord():
    
    navbar = render_template('components/navbar.html')
    header = render_template('components/header.html')
    sidebar = render_template('components/sidebar.html')
    footer = render_template('components/footer.html')
    content = render_template('pages/asset-and-event/discord-create.html')
    # import dashboard pages
    template = render_template('pages/layout.html',sidebar=sidebar, header=header, navbar=navbar,footer=footer,content=content)
    return template

@app.route('/attack')
def generate_attack_report():
    
    navbar = render_template('components/navbar.html')
    header = render_template('components/header.html')
    sidebar = render_template('components/sidebar.html')
    footer = render_template('components/footer.html')
    content = render_template('pages/generate-report/attack.html')
    js = render_template('components/chart.html')
    # import dashboard pages
    template = render_template('pages/layout.html',sidebar=sidebar, header=header, navbar=navbar,content=content,footer=footer,js=js)
    return template

# @app.route('/dns')
# def generate_dns_report():
    
#     navbar = render_template('components/navbar.html')
#     header = render_template('components/header.html')
#     sidebar = render_template('components/sidebar.html')
#     footer = render_template('components/footer.html')
#     content = render_template('pages/generate-report/dns.html')
#     js = render_template('components/dns-chart.html')
#     # import dashboard pages
#     template = render_template('pages/layout.html',sidebar=sidebar, header=header, navbar=navbar,content=content,footer=footer,js=js)
#     return template

@app.route('/malware')
def generate_malware_report():
    
    navbar = render_template('components/navbar.html')
    header = render_template('components/header.html')
    sidebar = render_template('components/sidebar.html')
    footer = render_template('components/footer.html')
    content = render_template('pages/generate-report/malware.html')
    # import dashboard pages
    template = render_template('pages/layout.html',sidebar=sidebar, header=header, navbar=navbar,footer=footer,content=content)
    return template

@app.route('/chart')
def chart():
    
    navbar = render_template('components/navbar.html')
    header = render_template('components/header.html')
    sidebar = render_template('components/sidebar.html')
    footer = render_template('components/footer.html')
    content = render_template('pages/testing/chart.html')
    # import dashboard pages
    template = render_template('pages/layout.html',sidebar=sidebar, header=header, navbar=navbar,footer=footer,content=content)
    return template

def main():
    app.run(debug=True,port=8625)
    print(f'server running on port: 8625')
    # serve(app, host='0.0.0.0', port=8625,url_scheme='https', threads=4, channel_timeout=120, cleanup_interval=30)
    # serve(app, host='0.0.0.0', port=8625)
