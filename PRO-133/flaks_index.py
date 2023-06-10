from flask import Flaks, render_template
app = Flask(__name__)
# in the function return_template('index.html')
@app.route("/index")
def first_webpage():
    #create a variable
    name = 'Flask'
    #pass the variable in the template
    return render_template('index.html', index_variable = name)
app.run(debug=True)
