from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.survey import Survey

@app.route('/')
def show_form():
    return render_template('index.html')

@app.route('/create/survey', methods = ['POST'])
def create_survey():
    print(request.form)
    if Survey.validate_survey(request.form):
        Survey.create(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def show_results():
    return render_template('result.html', survey = Survey.get_last())