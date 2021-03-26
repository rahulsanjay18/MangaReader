from flask import Flask, flash, redirect, render_template, request, session, abort, g
from random import randint
import os
app = Flask(__name__)
filename = "../Documents/Manga"
ch_list = []
ch_title = ""
manga_list = []
manga_title = ""
page_list = []
@app.route("/")
def index():
    return "Index!"


"""
@app.route("/chooseFolder/", methods=["POST"])
def chooseMangaFolder():

    reload()
"""

def reload():
    img_path = None

    if(filename != None and ch_title != "" and manga_title != ""):
        img_path = filename + "/" + manga_title + "/" + ch_title

    return render_template("reader.html", **locals())

@app.route("/choose_manga/", methods=["POST"])
def choose_manga():
    print("hello:choose_manga")
    manga_title = request.get_json()
    print(manga_title)
    #ch_list = os.listdir(filename + "/" + manga_title)
    #print(ch_list)
    #return render_template("reader.html", manga_list = manga_list, ch_list = ch_list)

@app.route("/reader")
def start_reader():
    manga_list = os.listdir(filename)
    return render_template("reader.html", manga_list=manga_list)
    #reload()




if __name__ == "__main__":
    app.run()

