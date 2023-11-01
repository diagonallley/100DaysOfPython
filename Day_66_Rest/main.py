from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import choice
import json
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):  # This is a dictionary comprehension function created inside the Cafe class definition. It will be used to turn rows into a dictionary before sending it to jsonify.
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
# with app.create_contect():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    res = db.session.execute(db.select(Cafe))
    all_cafes = res.scalars().all()
    random_cafe_ = choice(all_cafes)

    return jsonify(
        cafe={
            "id": random_cafe_.id,
            "name": random_cafe_.name,
            "map_uri": random_cafe_.map_url,
            "img_uri": random_cafe_.img_url,
            "location": random_cafe_.location,
            "seats": random_cafe_.seats,
            "has_toilet": random_cafe_.has_toilet,
            "has_wifi": random_cafe_.has_wifi,
            "has_sockets": random_cafe_.has_sockets,
            "can_take_calls": random_cafe_.can_take_calls,
            "coffee_price": random_cafe_.coffee_price
        }
    )


@app.route("/all")
def all_cafes():
    res = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes = res.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

    # result = db.session.execute(db.select(Cafe).order_by(Cafe.name))
    # all_cafes = result.scalars().all()
    # # This uses a List Comprehension but you could also split it into 3 lines.
    # return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    # return res


@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")
    res = db.session.execute(db.select(Cafe).where(
        Cafe.location == query_location))

    all_cafes = res.scalars().all()

    if all_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])
    else:
        return jsonify(error={"Not found": "Sorry, we don't have a cafe at that location"}), 404
# HTTP POST - Create Record


@app.route("/add", methods=["POST"])
def add_new_cafe():
    new_cafe = Cafe(
        name=request.json.get("name"),
        map_url=request.json.get("map_url"),
        img_url=request.json.get("img_url"),
        location=request.json.get("loc"),
        has_sockets=bool(request.json.get("sockets")),
        has_toilet=bool(request.json.get("toilet")),
        has_wifi=bool(request.json.get("wifi")),
        can_take_calls=bool(request.json.get("calls")),
        seats=request.json.get("seats"),
        coffee_price=request.json.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"Success": "Successfully added the new cafe"})
# HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"Success": "Successfully update the price"}), 200
    else:
        return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database"}), 404
# @app.route("")
# HTTP DELETE - Delete Record


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def del_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key == "thisKey":
        cafe = db.get_or_404(Cafe, cafe_id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database"}), 200
        else:
            return jsonify(error={"Not found": "Sorry a cafe with that id was not found in the database"}), 400
    else:
        return jsonify(error={
            "Forbidden": "Sorry, that is not allowed. Make sure you enter the correct api_key"
        }), 403


if __name__ == '__main__':
    app.run(debug=True)
