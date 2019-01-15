from flask import Flask, render_template, request, session, redirect
from models.character import Character
import mlab
from models.user import User 

mlab.connect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "NA3FkHgHQFcFdZby7FAuhgzBFP8nR3X3"

@app.route('/')
def home():
    return "HomePage"

@app.route('/character')
def character():
    return render_template("character.html")

@app.route('/add_character', methods=["GET", "POST"])
def add_character():
    #1. Gui form (GET)
    if request.method == "GET":
        return render_template("character_form.html")
    elif request.method == "POST":
    #4. Nhan form => Luu
        form = request.form
        print(form)
        name = form["name"]
        image = form["image"]
        rate = form["rate"]
        new_character = Character(name=name, image=image, rate=rate)
        new_character.save()
        return "GOTCHA"

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login_form.html")
    else:
        form = request.form 
        username = form["username"]
        password = form ["password"]
        
        found_user = User.objects(username=username).first()
        if found_user is None:
            return "User not found"
        elif found_user.password != password:
            return "Invalid password"
        else:
            session["token"] = username
            next = request.args.get("next")
            if next is None or next == "":
                return "Login successful !"
            else:
                return redirect(next)

@app.route('/logout')
def logout():
    del session["token"]
    return redirect("/login")

@app.route('/characters')
def characters():
    if "token" in session:
        character_list = Character.objects() #Get all data
        
        #Render: template + data
        return render_template("characters.html", character_list=character_list)
    else:
        return redirect("/login?next=/characters")

@app.route('/character/<given_id>')
def character_detail(given_id):
    #1. Get one character, based on id
    character = Character.objects().with_id(given_id)
    if character is None:
        return "Not found"
    else: #2. Render
        return render_template("character_detail.html", character=character)

@app.route('/character/delete/<given_id>')
def character_delete(given_id):
    character_del = Character.objects(id__exact=given_id)
    character_del.delete()
    return 'The id ' + given_id + ' was deleted'

# @app.route('/posts/')
# def posts():
#     if "token" not in session:
#         return redirect('/login?next=/posts')
#     else:
#         # Lam not

if __name__ == '__main__':
  app.run(debug=True)