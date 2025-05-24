from flask import Flask, render_template
from sql import get_items_list_by_category
app = Flask(__name__, static_folder = 'css')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/page2.html')
def catgory():
    return render_template('page2.html', products=get_items_list_by_category(1))
@app.route('/item.html')
def home_():
    return render_template('item.html')

app.run(debug=True)