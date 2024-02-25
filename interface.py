import user
import admin
import streamlit as st 
st.title("REAL ESTATE PORTAL")
nav=st.radio("CHOOSE ACCOUNT",["USER","ADMIN"])

if nav=="USER":
    user.userinterface()
            
else:
    
    admin.ad_login()
    

