# READ ME!

# This is a heavily censored version of the server code used for the Smart Industry project with Apollo Tyres. Instead of using the retrieved JSON data
# to call the needed model and retrieve the output, a simple hardcoded reply is returned.
# This was done to both adhere to the NDA as well as protect Apollo Tyres intellectual property

# Imports
import pandas as pd
from flask import Flask, request
from flask_cors import CORS
from flask_restx import Api, Resource, fields

#Create a flask object and enable Cross Origin Resource Sharing (CORS)
app = Flask(__name__)
CORS(app)

#Create the API and needed models used for the Swagger specification that creates an interface for describing web services.
api = Api(app, version='1.0', title='Tyre API', description='API for predicting tyre measurements')

diameter_model = api.model('DiameterModel', {
    'test_pressure_psi': fields.Float(required=True, description='Attribute 1', default=1.8),
    'belt1_material': fields.String(required=True, description='Attribute 1', default="SA01"),
    'belt1_angle': fields.Integer(required=True, description='Attribute 1', default=1),
    'capply': fields.String(required=True, description='Attribute 1', default="NB01"),
    'ply1': fields.Integer(required=True, description='Attribute 1', default=10),
    'bead_height': fields.Integer(required=True, description='Attribute 1', default=20),
    'cap_strip_layup': fields.String(required=True, description='Attribute 1', default="1-1-1"),
    'number_of_plies': fields.Integer(required=True, description='Attribute 1', default=1),
    'mould_overall_diameter' : fields.Integer(required=True, description='Attribute 1', default=500),
    'rim_protector': fields.Integer(required=True, description='Attribute 1', default=1),
    'sidewall_type': fields.String(required=True, description='Attribute 2', default="S5"),
    'mould_section_width': fields.Integer(required=True, description='Attribute 1', default=199),
    'mould_based_width': fields.Integer(required=True, description='Attribute 1', default=10),
    'sw_target_exc': fields.Integer(required=True, description='Attribute 1', default=120),
    'diameter_target_exc': fields.Integer(required=True, description='Attribute 1', default=10),
    'aspect_ratio': fields.Integer(required=True, description='Attribute 1', default=30)
    
})

max_width_model = api.model('MaxWidthModel', {
    'test_pressure_psi': fields.Float(required=True, description='Attribute 1', default=1.8),
    'belt1_material': fields.String(required=True, description='Attribute 1', default="SA01"),
    'belt1_angle': fields.Integer(required=True, description='Attribute 1', default=1),
    'capply': fields.String(required=True, description='Attribute 1', default="NB01"),
    'ply1': fields.Integer(required=True, description='Attribute 1', default=10),
    'bead_height': fields.Integer(required=True, description='Attribute 1', default=20),
    'cap_strip_layup': fields.String(required=True, description='Attribute 1', default="1-1-1"),
    'number_of_plies': fields.Integer(required=True, description='Attribute 1', default=1),
    'mould_overall_diameter' : fields.Integer(required=True, description='Attribute 1', default=500),
    'rim_protector': fields.Integer(required=True, description='Attribute 1', default=1),
    'sidewall_type': fields.String(required=True, description='Attribute 2', default="S5"),
    'mould_section_width': fields.Integer(required=True, description='Attribute 1', default=199),
    'mould_based_width': fields.Integer(required=True, description='Attribute 1', default=10),
    'sw_target_exc': fields.Integer(required=True, description='Attribute 1', default=120),
    'diameter_target_exc': fields.Integer(required=True, description='Attribute 1', default=10),
    'aspect_ratio': fields.Integer(required=True, description='Attribute 1', default=30)
    
})

# The first route, diameterpredict, which is used to predict the tyre diameter whenever it is called
# It formats the retrieved JSON to a Pandas dataframe and calls the correct model using the predict function
# It returns the two predicted values in the correct format for the javascript to format on the webpage
@api.route('/diameterpredict')
class DiameterPrediction(Resource):
    @api.expect(diameter_model)
    def post(self):
        data = request.json
        data = pd.json_normalize(data)
        data = pd.DataFrame(data=data, index=[0])  

        #predicted_difference_diameter_to_mould_od, predicted_tyrediameter = predict_tyre_diameter(data)
        return "{0},{1}".format(1, 2)

# The second route, maxwidthpredict, which is used to predict the tyre diameter whenever it is called
# It formats the retrieved JSON to a Pandas dataframe and calls the correct model using the predict function
# It returns the two predicted values in the correct format for the Javascript to format on the webpage
@api.route('/maxwidthpredict')
class MaxWidthPrediction(Resource):
    @api.expect(max_width_model)
    def post(self):
        data = request.json
        data = pd.json_normalize(data)
        data = pd.DataFrame(data=data, index=[0])  
      
        #predicted_maximum_tyre_width, predicted_difference_wmax_to_etrto_target = predict_tyre_width(data)
        return "{0},{1}".format(1, 2)

# The heartbeat endpoint which is called in regular intervals by the Javascript to check whether the server
# connection is still available
@api.route('/heartbeat')
class Heartbeat(Resource):
    def get(self):
        return 'OK', 200

# Starts the server whenever the program is started from the command line
if __name__ == '__main__':
    app.run(debug=True)



