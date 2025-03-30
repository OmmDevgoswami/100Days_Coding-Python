from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

# with app.app_context():
#     db.create_all()

# with app.app_context():
#     new_cafe = Cafe(
#         name="Cafe 2",
#         map_url="https://www.google.com/maps/place/Cafe+1/@37.7749",
#         img_url="https://www.google.com/maps/place/Cafe+1/@37.7749",
#         location = "Bhubaneswar",
#         seats = "25",
#         has_toilet = True,
#         has_wifi = True,
#         has_sockets = True,
#         can_take_calls = True,
#         coffee_price = "$3.00"
#     )
#     db.session.add(new_cafe)
#     db.session.commit()
    
#     new_cafe1 = Cafe(
#         name="Cafe 3",
#         map_url="https://www.google.com/maps/place/Cafe+1/@37.7749",
#         img_url="https://www.google.com/maps/place/Cafe+1/@37.7749",
#         location = "Bhubaneswar",
#         seats = "25",
#         has_toilet = True,
#         has_wifi = True,
#         has_sockets = True,
#         can_take_calls = True,
#         coffee_price = "$5.00"
#     )
#     db.session.add(new_cafe1)
#     db.session.commit()
    
#     new_cafe2 = Cafe(
#         name="Cafe 4",
#         map_url="https://www.google.com/maps/place/Cafe+1/@37.7749",
#         img_url="https://www.google.com/maps/place/Cafe+1/@37.7749",
#         location = "Bhubaneswar",
#         seats = "25",
#         has_toilet = True,
#         has_wifi = True,
#         has_sockets = True,
#         can_take_calls = True,
#         coffee_price = "$7.00"
#     )
#     db.session.add(new_cafe2)
#     db.session.commit()
    
#     new_cafe3 = Cafe(
#         name="Cafe 5",
#         map_url="https://www.google.com/maps/place/Cafe+1/@37.7749",
#         img_url="https://www.google.com/maps/place/Cafe+1/@37.7749",
#         location = "Bhubaneswar",
#         seats = "25",
#         has_toilet = True,
#         has_wifi = True,
#         has_sockets = True,
#         can_take_calls = True,
#         coffee_price = "$3.00"
#     )
#     db.session.add(new_cafe3)
#     db.session.commit()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods = ["GET"])
def data():
    cafe = db.session.execute(db.select(Cafe))
    cafes = cafe.scalars().all()
    
    if not cafes:
        return jsonify({"error": "No cafes available"}), 404
    
    cafe_choice = random.choice(cafes)
    
    cafe_data = {"Name": cafe_choice.name, 
                  "Map" : cafe_choice.map_url,
                  "Img" : cafe_choice.img_url,
                  "Locatiion" : cafe_choice.location,
                  "ameties" : {"seats" :  cafe_choice.seats,
                                "toilets" :  cafe_choice.has_toilet,
                                "wifi" :  cafe_choice.has_wifi,
                                "sockets" : cafe_choice.has_sockets,
                                "Take Calls" : cafe_choice.can_take_calls},
                  "Coffee Price" : cafe_choice.coffee_price}
    return jsonify(cafe_data)

@app.route("/all", methods = ["GET"])
def all():
    cafe = db.session.execute(db.select(Cafe))
    cafes = cafe.scalars().all()
    
    if not cafes:
        return jsonify({"error": "No cafes available"}), 404
    
    cafe_data = [{"Name": val.name, 
                  "Map" : val.map_url,
                  "Img" : val.img_url,
                  "Locatiion" : val.location,
                  "ameties" : {"seats" :  val.seats,
                                "toilets" :  val.has_toilet,
                                "wifi" :  val.has_wifi,
                                "sockets" : val.has_sockets,
                                "Take Calls" : val.can_take_calls},
                  "Coffee Price" : val.coffee_price} for val in cafes]
    return jsonify(cafe_data)

@app.route("/search/<loc>", methods = ["GET"])
def search(loc):
    cafe = db.session.execute(db.select(Cafe).where(Cafe.location == loc))
    cafes = cafe.scalars().all()
    
    if not cafes:
        return jsonify({"error": "Searched Cafe is not Avaiable"}), 404
    
    cafe_data = [{"Name": val.name, 
                  "Map" : val.map_url,
                  "Img" : val.img_url,
                  "Locatiion" : val.location,
                  "ameties" : {"seats" :  val.seats,
                                "toilets" :  val.has_toilet,
                                "wifi" :  val.has_wifi,
                                "sockets" : val.has_sockets,
                                "Take Calls" : val.can_take_calls},
                  "Coffee Price" : val.coffee_price} for val in cafes]
    return jsonify(cafe_data)

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url", ""),
        location=request.form.get("loc", ""),
        has_sockets=True if request.form.get("sockets") == "True" else False,
        has_toilet=True if request.form.get("toilet") == "True" else False,
        has_wifi=True if request.form.get("wifi") == "True" else False,
        can_take_calls=True if request.form.get("calls") == "True" else False,
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

from flask import Flask, request, jsonify

@app.route("/update/<int:id>", methods=["PATCH"])
def update(id):
    # cafe = db.session.execute(db.select(Cafe).where(Cafe.id == id)).scalar_one_or_none()
    cafe_val = request.args.get(id)
    cafe = db.get_or_404(Cafe, cafe_val)

    # if not cafe:
    #     return jsonify({"error": "Searched Cafe is not available"}), 404

    data = request.get_json()

    new_price = data.get("new_price")
    if new_price is None:
        return jsonify({"error": "No price provided"}), 400 
    
    cafe.coffee_price = new_price
    db.session.commit()

    return jsonify({"success": f"Successfully updated the coffee price for cafe ID {id}."})

@app.route("/report-update/<int:id>", methods=["GET", "DELETE"])
def delete(id):
    cafe = db.get_or_404(Cafe, id)
    
    if not cafe:
        return jsonify({"error": "Searched Cafe is not available"}), 404

    data = request.get_json()
    api_key = request.get_json().get("API_KEY")
    
    if api_key != "TopSecretKey":
        return jsonify({"error": "Wrong API Key provided."}), 403
    
    db.session.delete(cafe)
    db.session.commit()
    return jsonify({"success": f"Successfully updated the coffee price for cafe ID {id}."})



if __name__ == '__main__':
    app.run(debug=True)
