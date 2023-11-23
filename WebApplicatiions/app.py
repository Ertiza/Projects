from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# df is defined in your test.py file
from test import df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    formula_name = request.form['formulaName']

    # the formula_name is in the DataFrame
    if formula_name in df['Name of the Chemical Compound'].values:
        # Get the corresponding formula from the DataFrame
        result_formula = df[df['Name of the Chemical Compound'] == formula_name]['Formula'].values[0]

        return render_template('result.html', formula_name=formula_name, result_formula=result_formula)
    else:
        return render_template('result.html', formula_name=formula_name, result_formula='Formula not found')

if __name__ == '__main__':
    app.run(debug=True)


