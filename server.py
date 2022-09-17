from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secret counter"

@app.route('/')
def index():
    if 'visit' in session:
        session['visit'] += 1
    else:
        session['visit'] = 0
    return render_template('index.html')

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    session['visit'] = 0
    session['count'] = 0
    return redirect('/')

@app.route('/increment-by-two')
def increment_by_two():
    session['count'] += 2
    return redirect('/')

@app.route('/add', methods=['POST'])
def add():
    session['count'] += int(request.form['specify-count'])
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)