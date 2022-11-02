import streamlit
import pandas

streamlit.title("Mr Aru's Kitchen")  
streamlit.header("Breakfast Favourites")
streamlit.text("🍞 Cheese Bread Omlette")
streamlit.text("🍞 Plain Bread Omlette")
streamlit.text("🥣 Creamy Mushroom Soup")
streamlit.text("🥑 Avacado Juice")
streamlit.text("🥗 Broccoli Soup")
streamlit.text("🐔 Hard Boiled Egg")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#Reads the fruits list from the AWS S3 text file
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#Select options for user to choose their fruit list for smoothie
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#Dispay only user selected fruits 
streamlit.dataframe(fruits_to_show)

import requests

streamlit.header("Fruityvice Fruit Advice!")
#API request to get Fruityvice details for watermelon
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response.json())
# Normalize json response 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# Display the normaized data as dataframe
streamlit.dataframe(fruityvice_normalized)

#user input for fruit advice
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
