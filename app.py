import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import openai

basedir = os.path.abspath(os.path.dirname(__file__))
openai.api_key = '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'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'MLXH243rjBDIBibiBIbibIUBImmfrdTWS7FDhdwYF56wPj8'

db = SQLAlchemy(app)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime)
    
    def __init__(self, image_url):
        self.image_url = image_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('generateQuery')
        response = openai.Image.create(prompt=query,n=3,size="1024x1024")
        image_url = response['data'][0]['url']
        newImage = Image(image_url=image_url)
        db.session.add(newImage)
        db.session.commit()
        return render_template('index.html', image_url=image_url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='80')