from flask import Flask, render_template, redirect, request, url_for
import requests
import os





app = Flask(__name__)






# home route
@app.route('/')
def index():
    # display only



    return render_template('index.html',) #home page



@app.route('/sendImageBack', methods=['GET', 'POST'])
def imageRoute():
    # display only

    memeImage = request.form.get("memeImage")
    first =  request.form.get("first")
    second =  request.form.get("second")
    # print(f'Image memeImage')


    return render_template('index.html', transferImage = memeImage, first=first, second=second ) #home page





# main module page
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

# Todo:
    # Error handle code
    # progress Hud
    # Specific Directory location to download file to
