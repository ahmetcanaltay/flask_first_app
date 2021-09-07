from flask import Flask, render_template, url_for

app=Flask(__name__)


@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html')
@app.route('/login')
def login():
    return '<h1>Not Ready! Come back Later</h1>'

@app.route('/register')
def register():
    return '<h1>Not Ready! Come back Later</h1>'

@app.route('/about')
def about():
    return render_template('about.html', title='About')
@app.route('/<name>')
def index(name):
    return '<h1>Hello! We couldnt find this page ,  {} </h1>'.format(name)

if __name__=='__main__':
    app.run(debug=True)