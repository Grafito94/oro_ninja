from flask import Flask, render_template, request,  redirect, session
import random

app = Flask(__name__)
app.secret_key = "llave secreta"


@app.route('/')
def view():
    if "total_gold" and "activities" not in session:
        session['total_gold'] = 0
        session['activities'] = " "

    else:
        print(session['total_gold'])
    return render_template("index.html", total = session['total_gold'], activities = session['activities'])

@app.route('/process_money', methods = ['POST'])
def money():

    cas = random.randint(0,1)
    casr = random.randint(0,50)
    if request.form['send'] == 'farm':
        session['total_gold'] = session['total_gold'] + random.randint(10,20)
        session['activities'] = " haz ganado " + str(session['total_gold'])
    elif request.form['send'] == 'cave':
        session['total_gold'] = session['total_gold'] + random.randint(5,10)
        session['activities'] = " haz ganado " + str(session['total_gold'])
    elif request.form['send'] == 'house':
        session['total_gold'] = session['total_gold'] + random.randint(2,5)
        session['activities'] = " haz ganado " + str(session['total_gold'])
    else:
        if cas == 1:
            session['total_gold'] = session['total_gold'] + random.randint(0,50)
            session['activities'] = " haz ganado " + str(session['total_gold'])
        else:
            session['total_gold'] = session['total_gold'] - casr
            session['activities'] = " haz perdido " + str(casr)
    return redirect('/')

@app.route("/destroy_session", methods=['POST'])
def destroy():
    if 'reset' not in session:
        session['reset'] = request.form['reset']
        session.clear()
    return redirect('/')

if __name__=="__main__":       
    app.run(debug=True) 

