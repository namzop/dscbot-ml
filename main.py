from flask import Flask, request, send_file, send_from_directory, render_template, redirect
import json
import time
import datetime
import os
# import sqlite3
import database
import random




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


@app.route('/create',methods = ['POST', 'GET'])
def createforthem():
    if request.method == "POST":
        name=request.form.get('name')
        url=request.form.get('url')
        key = request.form.get('key')
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
