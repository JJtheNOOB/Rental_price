import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
import pickle

#title
st.title("Toronto Housing Price Evaluation")

#add pictures
image = "https://wp-tid.zillowstatic.com/trulia/wp-content/uploads/sites/3/2019/05/how-to-rent-out-your-house-e14146.png"
st.image(image, caption='Rental Image',use_column_width=True)

#input features
features = []

#load the model
model = pickle.load(open('thresh_3000_model.pkl', 'rb'))

#Get address and return a map
address = st.text_input("1. Please enter your address")
geolocator = Nominatim(user_agent="haha@hotmail.com")
location = geolocator.geocode(address)
if location is not None:  # If failed to get right address, insert a new address
    features.insert(0, location.longitude)
    features.insert(0, location.latitude)
else:
    st.write("Wrong Format of Address Entered! Please try modify the address. ")
    features.insert(0, -79.1)
    features.insert(0, 46)

#Plot the location
if st.checkbox('Show Map'):
    map_data = pd.DataFrame(
         [features],
        columns=['lat', 'lon'])
    st.write("Here is your approximate location:")
    st.map(map_data)

num_bedroom = st.number_input("2. Please enter number of bedrooms", 1)
features.append(num_bedroom)
op_1 = st.selectbox('3. Air Conditioning Available?',('Yes', 'No'))
if op_1 == "yes":
    features.append(1)
else:
    features.append(0)
op_2 = st.selectbox('4. Are Water Bills Free?',('Yes', 'No'))
if op_2 == "yes":
    features.append(1)
else:
    features.append(0)
op_3 = st.selectbox('5. Are Storage Rooms / Lockers Available?',('Yes', 'No'))
if op_3 == "yes":
    features.append(1)
else:
    features.append(0)
op_4 = st.selectbox('6. Are Parking Spaces Available?',('Yes', 'No'))
if op_4 == "yes":
    features.append(1)
else:
    features.append(0)
op_5 = st.selectbox('7. Is the parking space underground?',('Yes', 'No'))
if op_5 == "yes":
    features.append(1)
else:
    features.append(0)
op_6 = st.selectbox('8. Is gym / exercise room Available?',('Yes', 'No'))
if op_6 == "yes":
    features.append(1)
else:
    features.append(0)
op_7 = st.selectbox('9. Are laundry rooms / facilities Available?',('Yes', 'No'))
if op_7 == "yes":
    features.append(1)
else:
    features.append(0)

df = pd.DataFrame([features], columns = ['latitude', 'longtitude', 'bedroom_num', 'AirConditioning',
                                            'Water', 'StorageLockers', 'Parking', 'UndergroundParking',
                                            'ExerciseRoom', 'LaundryFacilities'])

def run_result():
    prediction = model.predict(df)[0]

    if prediction <= 1600 or prediction >= 3000:
        message = "We are not so confident on our price evaluation in this case"
    elif (prediction > 1600 and prediction <= 2100) or (prediction >= 2450 and prediction < 3000):
        message = "We are very confidence that about our price evaluation within range {} to {}".format(
            (prediction - 150), (prediction + 150))
    else:
        message = "There is something wrong in the address input, please retry"

    st.write("------------------------------------------")

    st.title("**{}**".format(message))


if st.button("Click here to calculate"):
    run_result()
	
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")





