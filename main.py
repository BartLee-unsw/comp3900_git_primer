from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculator')
def calculator():
<<<<<<< HEAD
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
        except ValueError:
            result = "Invalid input. Please enter numbers only."
    return render_template('calculator.html', result=result)
=======
    return render_template('calculator.html')
>>>>>>> origin/incorrect_branch_name

if __name__ == '__main__':
    app.run(debug=True)
