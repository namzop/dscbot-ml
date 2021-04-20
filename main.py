from flask import Flask, request, send_file, send_from_directory, render_template, redirect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
import time
import datetime
import os
# import sqlite3
import database
import random




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
    k  = database.get_link(linklol)
    if k == "Not Found":
        return render_template('notfound.html')
    else:
        return redirect(k)
    # f=open('data.json')
    # thedata = json.load(f)
    # try:
    #     thefinallink=thedata[linklol][0]['url']
    #     return redirect(thefinallink)
    # except:
    #     return render_template('notfound.html')
    # return redirect(thelink)

@app.route("/hehe", methods=['POST', 'GET'])
@limiter.limit("1/day;15/month")
def hehebruv():
    if request.method == "POST":
        abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"]
        cap_abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "W", "X", "Y", "Z"]
        k = random.randint(1,9)
        kk = random.randint(11, 19)
        kkk = random.randint(21, 29)
        kkkk = random.randint(31, 39)
        number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        random_abc_small = random.choice(abc)
        random_abc_cap = random.choice(cap_abc)
        open("uwu.txt", 'w').write(f'{random_abc_small}{k}{kkkk}{kkk}{random_abc_cap}{kk}')
        return f"{random_abc_small}{k}{kkkk}{kkk}{random_abc_cap}{kk}"
    else:
        return "You need to POST not GET and btw you exhausted your 1 request of today. Try Again Tommorow!"

@app.route('/create',methods = ['POST', 'GET'])
def createforthem():
    if request.method == "POST":

        name=request.form.get('name')
        url=request.form.get('url')
        key = request.form.get('key')
        f = open("uwu.txt", 'r')
        # f.close()
        if key == f.read():
            f.close()
            k = open('uwu.txt', 'w')
            k.write('barryisgay')
            k.close()
            if 'https://discord.com' in url:
                owo = database.get_link(url)
                if owo == "Not Found":
                    uwu = database.make_new_link(name, url)
                    if uwu == "Done!":
                        return redirect("/success")
                    else:
                        return redirect('/success?error=error')
                else:
                    return redirect('/success?error=taken')
            else:
                return redirect("/success?error=notdiscord")
        else:
            return redirect('/success?error=invalidkey')
        """
        try:
            c.execute("SELECT * FROM links WHERE name={}".format(str(name)))
            k = c.fetchone()
            return k
            # return "This name is already taken!"
        except:
            c.execute(f'INSERT INTO links VALUES ("lmao", "lmfao")')
            return "Thanks for using !"
        """
        # try:
        #     f = open('data.json', 'r')
        #     da_guy = json.loads(f.read())
        #     kk = da_guy[name]
        #     return redirect('/success?success=false')
        # except:
        #     k = open('requests.txt', 'a')
        #     k.write("Name: {} URL: {} \n".format(name,url))
        #     k.close()
        #     return redirect('/success')


    else:
        return render_template('register.html')

@app.route('/success')
def yay():
    if 'error' in request.args:
        error=request.args['error']
        if error=='taken':
            return "This name is already taken by someone ;-;"
        elif error == "error":
            return "Some Unknown Error occured while creating it!"
        elif error == "notdiscord":
            return "That was not a discord link bruv!"
        elif error=="invalidkey":
            return "The key you entered was invalid"
        else:
            return " An error is encountered!"
    else:
        return "Thanks for using registering! Your vanity url will start working soon!"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
