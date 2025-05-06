#Importing streamlit, will be used to build the dashboard
import streamlit as st

# Pandas will be used to work with the CSV data
import pandas as pd

#Importing Matplotlib to visualise charts 
import matplotlib.pyplot as plt

#Naming our dashboard US food imports 
st.title("US Food Imports Dashboard")

#Adding a short description of what the users can do with the dashboard
st.write("This is a simple dashboard to help you explore US food import data.")
st.write("You can look at the data by food category, country, or specific commodity.")

#Loading the CSV file
# The file must be in the same folder as this app.py file
data = pd.read_csv("FoodImports.csv", encoding='latin1')

#Showing the user how the dataset looks like 
st.subheader("📄 Preview of the Data")
st.dataframe(data.head()) #Only shows the first few rows 

#Let the user choose what they want to explore
#Ensuring the user can only pick one option at a time, hence, 'st.radio' is used
st.subheader("🔍 Filter the Data")

filter_type = st.radio(
    "Choose a filter:",
    ("Category", "Country", "Commodity")
)

#Show the output (menu) of what the user has shown to choose
#Filters out the dataset to retrieve the appropriate and relevant outputs

if filter_type == "Category":
    #Retrieves the info and shows the output to the user
    selected_category = st.selectbox("Choose a food category:", data['Category'].unique())
    
    filtered_data = data[data['Category'] == selected_category]
    
    #Title for the chart that will be displayed to the user
    chart_title = f"Import Trends for Food Category: {selected_category}"

elif filter_type == "Country":
    #Shows countries if the user chose another option (Specific countries)
    selected_country = st.selectbox("Choose a country:", data['Country'].unique())
    
    #Shows the relevant output from the country selected
    filtered_data = data[data['Country'] == selected_country]
    
    #The title for the charts for the country the user has selected
    chart_title = f"Import Trends for Country: {selected_country}"

elif filter_type == "Commodity":
    #Show the dropdown of commodity when chosen by the user
    selected_commodity = st.selectbox("Choose a commodity:", data['Commodity'].unique())
    
    #Filters the data
    filtered_data = data[data['Commodity'] == selected_commodity]
    
    #Create a title for the commodity chart
    chart_title = f"Import Trends for Commodity: {selected_commodity}"

#Shows only the filtered data
st.subheader("📋 Filtered Data Preview")
st.dataframe(filtered_data)

#Make a line chart to show the import trend over time
st.subheader("📈 Import Value Over Time")

#Creation of the chart using Matplotlib
# We use matplotlib to draw the line graph
fig, ax = plt.subplots()

ax.plot(
    filtered_data['YearNum'],
    filtered_data['FoodValue'],
    marker='o',        # Show dots at each point
    linestyle='-',     # Connect them with lines
    color='green'      # Line color
)

# Adding relevant labels to the chart title 
ax.set_title(chart_title)
ax.set_xlabel("YearNum")
ax.set_ylabel("Import Value (Millions USD)")

# Rotate x-axis- easier to read
plt.xticks(rotation=45)

# Show chart on Streamlit
st.pyplot(fig)

