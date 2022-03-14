from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.survey import Survey

@app.route('/')
def show_form():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def check_and_save():
    print(request.form)
    if not Survey.validate_survey(request.form):
        return redirect('/')
    Survey.create(request.form)
    return redirect('/result')

@app.route('/result')
def show_results():
    return render_template('result.html')