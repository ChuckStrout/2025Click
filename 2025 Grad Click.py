import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Load the Excel file
DATA_FILENAME = Path(__file__).parent/'data-click/2025 GSMUD.xlsx'

dfg = pd.read_excel(DATA_FILENAME, sheet_name="Grad Raw Data")
dfg.columns.values[1] = "PROW"
dfg.columns.values[2] = "PSEAT NUMBER"
dfg.columns.values[4] = "ROW"
dfg.columns.values[5] = "SEAT NUMBER"
dfg.columns.values[11] = "PRONOUNCE"
# Display the DataFrame in Streamlit
st.title("2025 RMHS Grad Clicker")


event = "Graduation"
if event == "Graduation":
    venue_options = ("In PAC", "On Turf", "Click","Data")

venue = st.radio("Select Venue", venue_options,horizontal=True )

dfg["Full Name"] = dfg["Last Name"].astype(str) + ", " + dfg["First Name"].astype(str)



# Graduation
if venue == "Data":
    st.dataframe(dfg)
        
if venue == "In PAC":
    selected_name = st.selectbox(
    "Select Your Name",
    options=sorted(dfg["Full Name"].unique()),
    key="full_name_select"
    )   
    selected_row = dfg[dfg["Full Name"] == selected_name].iloc[0]
    st.header("Starting in the PAC ")
    
    sectg=selected_row["SECTION"]
    st.text(f"Sit in the {sectg} Section")
    rowg=selected_row["PROW"]
    st.text(f"Sit in Row: {rowg}")
    snumg=selected_row["PSEAT NUMBER"]
    st.text(f"Sit in Seat Number: {snumg}" )

if venue =="On Turf":
    selected_name = st.selectbox(
    "Select Your Name",
    options=sorted(dfg["Full Name"].unique()),
    key="full_name_select"
    )  
    selected_row = dfg[dfg["Full Name"] == selected_name].iloc[0]
    st.header("On The Turf")
    side=selected_row["SIDE"]
    st.text(f"You will be On the Side: {side}")
    rowg=selected_row["ROW"]
    st.text(f"You will Sit in the Row: {rowg}" )
    sng=selected_row["SEAT NUMBER"]
    st.text(f"Sit in Seat Number: {sng}")

if venue == "Click":
    if "row_index" not in st.session_state:
        st.session_state.row_index = 0


    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if st.button("⬅️ Previous"):
            if st.session_state.row_index > 0:
                st.session_state.row_index -= 1

    with col3:
        if st.button("Next ➡️"):
            if st.session_state.row_index < len(dfg) - 1:
                st.session_state.row_index += 1

    row = dfg.iloc[st.session_state.row_index]
    side = row["SIDE"]
    rown = row["ROW"]
    first = row["First Name"]
    middle = row["Middle"]
    seat = row["SEAT NUMBER"]

    if pd.isna(middle):
        middle = ""
    last = row["Last Name"]
    pronounce = row["PRONOUNCE"]
    if pronounce == 0 or pd.isna(pronounce):
        pronounce=""
    honor = row["Honor"]
    st.title(f"{first} {middle} {last}")
    st.subheader(pronounce)
    st.title(honor)
    st.text(f"Side: {side}  Row: {rown} Seat {seat}")



st.text(f"")
st.text(f"")
st.text(f"")
st.text(f"")
st.text(f"")
st.text(f"")
st.text(f"")
st.text(f"")
st.text("v05292515:18")
