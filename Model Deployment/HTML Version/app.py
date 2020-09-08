import flask
import pickle
import pandas as pd
from geopy.geocoders import Nominatim

# Use pickle to load in the pre-trained model.
model = pickle.load(open('thresh_3000_model.pkl', 'rb'))
app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        features = [x for x in flask.request.form.values()]
        address = features[0]
        others = [float(x) for x in features[1:]]
        print(features)
        ####
        geolocator = Nominatim(user_agent="haha@hotmail.com")
        location = geolocator.geocode(address)
        if location is not None:  #If failed to get right address, insert a new address
            others.insert(0, location.longitude)
            others.insert(0, location.latitude)
            Error_message = "No Error in input"
        else:
            Error_message = "Wrong Format of Address Entered!"
            others.insert(0, -79.1)
            others.insert(0, 46)
        ####
        df = pd.DataFrame([others], columns = ['latitude', 'longtitude', 'bedroom_num', 'AirConditioning',
                                            'Water', 'StorageLockers', 'Parking', 'UndergroundParking',
                                            'ExerciseRoom', 'LaundryFacilities'])
        prediction = model.predict(df)[0]
        if prediction <= 1600 or prediction >= 3000:
            message = "We are not so confident on our price evaluation in this case"
        elif (prediction > 1600 and prediction <= 2100) or (prediction >= 2450 and prediction < 3000):
            message = "We are very confidence that about our price evaluation within range {} to {}".format((prediction - 150), (prediction + 150))
        else:
            message = "We are very confident in our prediction"
        return flask.render_template('main.html',
                                     original_input = {},
                                     Error_message=Error_message,
                                     result=prediction,
                                     confidence = message,
                                     )
if __name__ == '__main__':
    app.run()