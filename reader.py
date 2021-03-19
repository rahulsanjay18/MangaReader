from flask import Flask, flash, redirect, render_template, request, session, abort, g
from random import randint
import os
app = Flask(__name__)
filename = ""
ch_list = []
ch_num = 0
@app.route("/")
def index():
    return "Index!"

@app.route("/members")
def members():
    return "Members"

@app.route("/members/<string:name>/")
def getMember(name):
    return '%s'% name

@app.route("/hello")
@app.route("/hello/<string:name>")
def hello(name="None"):
   quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
             "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
             "'To understand recursion you must first understand recursion..' -- Unknown",
             "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
             "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
             "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
   randomNumber = randint(0,len(quotes)-1)
   quote = quotes[randomNumber]

   return render_template(
           'test.html',**locals()
   )

@app.route("/chooseFolder/", methods=["POST"])
def chooseMangaFolder():
    filename = filedialog.askdirectory(title="Select Folder")
    ch_list = os.listdir(filename)
    ch_num = 1
    reload()


def reload():
    img_path = None
    if(filename != None and ch_num != 0):
        img_path = filename + ch_list[ch_num]

    return render_template("reader.html", ch_list = ch_list, img_path = img_path)



@app.route("/reader")
def start_reader():
    return render_template("reader.html")




if __name__ == "__main__":
    app.run()

