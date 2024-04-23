from flask import Flask, render_template, jsonify
import json
# from models import db  # Import db (SQLAlchemy instance) from models
import os
app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('instance/config.py', silent=True)
# Update the database URI

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path
# # Initialize the SQLAlchemy instance with the Flask app
# db.init_app(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/property/')
def property_view():
    # buildings = db.session.query(Building).all()  # Query all Building objects from the database
    f=open('./data.json')
    buildings=json.load(f)
    print(buildings)
    return render_template('property.html', buildings=buildings)

@app.route('/property/<int:prop_id>/')
def property_details(prop_id):
    # property = db.session.query(Building).get_or_404(prop_id)  # Query a specific Building object by ID
    print("prop_id",prop_id)
    f=open('./data.json')
    buildings=json.load(f)
    property={}
    for i in buildings:
        if i["prop_id"]==prop_id:
            property=i
            break
    return render_template('prop1.html', property=property)

@app.route('/property/details/<int:prop_id>/')
def get_property_details(prop_id):
    # building_obj = db.session.query(Building).get_or_404(prop_id)
    building_data = {
        'prop_id': building_obj.prop_id,
        'prop_name': building_obj.prop_name,
        'prop_addr': building_obj.prop_addr,
        'Latitude': building_obj.latitude,
        'Longitude': building_obj.longitude,
        'price': building_obj.price,
        'sqft': building_obj.sqft,
        'bhk': building_obj.bhk,
        'rent': building_obj.rent,
        'sale_type': building_obj.sale_type,
        'furnishing_type': building_obj.furnishing_type,
        'reserved_parking': building_obj.reserved_parking,
        'kids_play_area': building_obj.kids_play_area,
        'gym': building_obj.gym,
        'swimming_pool': building_obj.swimming_pool,
        'club_house': building_obj.club_house,
    }
    return jsonify(building_data)

@app.route('/fin/')
def fw():
    return render_template('fw.html')

if __name__ == '__main__':
    app.run(debug=True)