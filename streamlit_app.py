import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized


streamlit.header("Fruityvice Fruit Advice!")
try:
  #user input for fruit advice
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    #return value from get function get_fruityvice_data 
    ret_value=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(ret_value)
except URLError as e:
  streamlit.error()

streamlit.header("The Fruit Load list contains:")
#snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from FRUIT_LOAD_LIST")
    return  my_cur.fetchall()
  
#add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

#user input for fruit add
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into FRUIT_LOAD_LIST values ('"+ new_fruit +"')")
    streamlit.write('Thanks for adding ', new_fruit)
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  return_value=insert_row_snowflake(add_my_fruit)
  my_cnx.close()
  streamlit.text(return_value)


