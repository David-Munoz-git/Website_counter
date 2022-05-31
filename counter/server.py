from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'fskdmfoaisjefms65168135164'

@app.route('/')
def counter():
  if 'visits' not in session:
    session['visits'] = 0
  session['visits'] += 1
  print(f" your visits {session['visits']}")
  return render_template('index.html')


@app.route('/destroy_session')
def clear():
  session.clear()
  return redirect('/')










if __name__=="__main__":
    app.run(debug=True)
