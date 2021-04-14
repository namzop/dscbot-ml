from flask import Flask, request, send_file, send_from_directory, render_template, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
import time
import datetime
import os



app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address
)

@app.route('/')
def lol():
    return render_template('vanity.html')

@app.route('/<linklol>')
def notfunny(linklol):
    f=open('data.json')
    thedata = json.load(f)
    try:
        thefinallink=thedata[linklol][0]['url']
        return redirect(thefinallink)
    except:
        return render_template('notfound.html')
    # return redirect(thelink)

@app.route('/create',methods = ['POST', 'GET'])
def createforthem():
    if request.method == "POST":
        name=request.form.get('name')
        url=request.form.get('url')
        try:
            f = open('data.json', 'r')
            da_guy = json.loads(f.read())
            kk = da_guy[name]
            return redirect('/success?success=false')
        except:
            k = open('requests.txt', 'a')
            k.write("Name: {} URL: {} \n".format(name,url))
            k.close()
            return redirect('/success')

    else:
        return render_template('register.html')

@app.route('/success')
def yay():
    if 'error' in request.args:
        error=request.args['error']
        if error=='taken':
            return "This name is already taken by someone ;-;"
        else:
            return " An error is encountered!"
    else:
        return "Thanks for using registering! Your vanity url will start working soon!"

if __name__ == "__main__":
    app.run(port=8080)
