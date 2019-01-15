from flask import Flask, render_template, request
import mlab
from models.bikes import Bike

app = Flask(__name__)
mlab.connect()

@app.route('/new_bike', methods=["GET", "POST"])
def buy_bike():
    if request.method == "GET":
        return render_template("buy_bike.html")
    else:
        form = request.form 
        model = form["model"]
        fee = form["fee"]
        img = form["img"]
        year = form["year"]
        new_bike = Bike(model=model,
                        fee=fee,
                        img=img,
                        year=year)
        new_bike.save()

        return render_template("request_form.html", model=model,
                                                    fee=fee,
                                                    img=img,
                                                    year=year)

if __name__ == '__main__':
  app.run(debug=True)