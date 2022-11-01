import streamlit
import pandas

streamlit.title("Mr Aru's Kitchen")  
streamlit.header("Breakfast Favourites")
streamlit.text("🍞 Cheese Bread Omlette")
streamlit.text("🍞 Plain Bread Omlette")
streamlit.text("🥣 Creamy Mushroom Soup")
streamlit.text("🥑 Avacado Juice")
streamlit.text("🥗 Broccoli Soup")
streamlit.text("🐔 Hard Boied Egg")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


