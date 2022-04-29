from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import randint
import json

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
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

	def to_dict(self):
		#Method 1. 
		dictionary = {}
		# Loop through each column in the data record
		for column in self.__table__.columns:
			#Create a new dictionary entry;
			# where the key is the name of the column
			# and the value is the value of the column
			dictionary[column.name] = getattr(self, column.name)
		return dictionary
		
		#Method 2. Altenatively use Dictionary Comprehension to do the same thing.
		# return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def get_random_cafe():  
    num = randint(1,21)
    random_cafe = Cafe.query.filter_by(id=num).first()
    
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():  
    cafes_dict = []
    all_cafes = Cafe.query.all()
    
    for cafe in all_cafes:
        cafe = cafe.to_dict()
        cafes_dict.append(cafe)
        
    return jsonify(cafes=cafes_dict)

@app.route("/search", methods=['GET'])
def search_cafe():
	args = request.args.to_dict()
    
    # print(args['loc'])
    
	cafes_dict = []
	all_cafes = Cafe.query.filter_by(location=args["loc"]).all()
    
	if all_cafes:
		for cafe in all_cafes:
			cafe = cafe.to_dict()
			cafes_dict.append(cafe)
	else:
		cafes_dict = {
			"error": {
				"Not Found": "Sorry, we don't have a cafe at that location."
			}
		}
        
	return jsonify(cafes=cafes_dict)

@app.route("/add", methods=['POST'])
def add():
	try:
		new_cafe = Cafe(
			name=request.form.get("name"),
			map_url=request.form.get("map_url"),
			img_url=request.form.get("img_url"),
			location=request.form.get("loc"),
			has_sockets=bool(request.form.get("sockets")),
			has_toilet=bool(request.form.get("toilet")),
			has_wifi=bool(request.form.get("wifi")),
			can_take_calls=bool(request.form.get("calls")),
			seats=request.form.get("seats"),
			coffee_price=request.form.get("coffee_price")
    	)
		return jsonify(response={"success": "Successfully added new cafe."})
	except:
		return jsonify(response={"error": "Something went wrong."})


@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def patch_new_price(cafe_id):
	price = request.form.get("new_price")
	cafe = Cafe.query.get(cafe_id)
	if cafe:
		cafe.coffee_price = price
		# db.session.add()
		db.session.commit()
		return jsonify(response={"success": "Successfully added new cafe."})
	else:
		return jsonify(response={"error": "Something went wrong."})


@app.route("/report-closed/<cafe_id>", methods=['POST', 'DELETE'])
def delete(cafe_id):
	key = request.form.get("api_key")
	if key == 'TopSecretAPIKey':
		Cafe.query.filter_by(id=cafe_id).delete()
		db.session.commit()
		return jsonify(response={"success": "Successfully deleted cafe."})
	else:
		return jsonify(error={"Not Found": "Incorrect api key."})




     
    
    

## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
