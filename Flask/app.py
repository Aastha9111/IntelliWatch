from flask import Flask, render_template
app = Flask(__name__)




@app.route('/')
def hello_world():
    
    return render_template('flask/index.html')

@app.route('/products')
def products(): 
    return 'This is a new product'

if __name__ == "__main__":
    app.run(debug=True)