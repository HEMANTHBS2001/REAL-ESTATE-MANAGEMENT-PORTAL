import streamlit as st 
import pandas as pd
import psycopg2
import main
from streamlit_option_menu import option_menu

def userinterface():
    nav=st.sidebar.radio("USER NAVIGATION",["HOME","PROPERTIES","SEARCH","QUERY"])
    if nav=="HOME":
        st.write("HOME PAGE")
        st.write("WELCOME TO REALESTATE PORTAL")
        
        
    elif nav=="PROPERTIES":
        st.title("PROPERTY DETAILS")
        main.view1()
        
    elif nav=="SEARCH":
        main.search_data()
        unique_values=main.search_data()
        city=st.selectbox("SELECT",unique_values)
        main.search_crit(city)
        main.search_data1()
        unique_values1=main.search_data1()
        types=st.selectbox("SELECT",unique_values1)
        main.search_crit1(city,types)
        
            
    elif nav=="QUERY":
       st.title('PROPERTY QUERY')
       name = st.text_input('NAME')
       mobile_number = st.text_input('Mobile Number')
       property_id =st.text_input('ENTER PROPERTY ID THAT YOU WANT TO ENQUIRE ABOUT')
       
       query = st.text_area('Description About Query')
       

       if st.button('Submit'):
          main.insert_data1(name,mobile_number,property_id,query)
    else:
        pass
      
    
    

    
        
    