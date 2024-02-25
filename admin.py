import streamlit as st 
import main

main.get_db_connection()

def ad_login():
   login_admin1()
   
    
        
        
    
    
    
def login_succ():
    st.title("LOGIN SUCCESSFULL")
    
def admin_navigation():
    
    nav=st.sidebar.radio("ADMIN NAVIGATION",["ADD","VIEW","SEARCH","DELETE","IMPORT DATA","EXPORT DATA","VIEW QUERY"])
    if nav=="ADD":
        admin_adding()
                
    elif nav=="VIEW":
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
        
    elif nav=="DELETE":
        property_id=st.text_input("ENTER PROPERTY ID TO DELETE")
        if st.button("CONFIRM DELETE"):
            main.delete_data(property_id)
    elif nav=="IMPORT DATA":
        nav=st.radio("TYPE OF FILE",["CSV","EXCEL"])
        if nav=="CSV":
            file=st.text_input("ENTER PATH OF THE FILE")
            if st.button("CONFIRM IMPORT"):
                main.csv_add(file)
        else:
            file=st.text_input("ENTER PATH OF THE FILE")
            if st.button("CONFIRM IMPORT"):
                main.excel_add(file)
    elif nav=="EXPORT DATA":
            file=st.text_input("ENTER FILE NAME TO EXPORT")
            if st.button("CONFIRM EXPORT"):
                main.export_file(file)
    
    elif nav=="VIEW QUERY":
            main.view_query()
    else:
        pass
def admin_adding():
       st.title('Real Estate Portal - Property Details Collection')
       owner = st.text_input('Owner')
       mobile = st.text_input('Mobile')
       district = st.text_input('District')
       taluk = st.text_input('Taluk')
       types=st.selectbox("TYPE",["RENT ","SELL ","LEASE "])
       age = float(st.number_input('Age Of The House'))
       description = str(st.text_area('Description'))
       price = int(st.number_input('Price', min_value=0))
       bedrooms = int(st.number_input('Bedrooms', min_value=0))
       sqft = float(st.number_input('Square Feet', min_value=0, step=1))
       #return owner,mobile,district,taluk,types,age,description,price,bedrooms,sqft
   
       if st.button('Submit'):
           
           main.insert_data(owner,district,taluk,types,age,mobile,bedrooms,sqft,description,price)
       
def login_admin():
    username=st.text_input("ENTER NAME")
    password=st.text_input("ENTER PASSWORD")
    but=st.button("SUBMIT")
    connection = main.get_db_connection()
    cursor = connection.cursor()
    if but:
        query=f"SELECT * FROM admin_panel WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        data=cursor.fetchone()
        
        
        if data:
            login_succ()
            admin_navigation()
        else:
            st.warning("INVALID USERNAME OR PASSWORD")  
            
    else:
        pass

def login_admin1():
    username=st.text_input("ENTER NAME")
    password=st.text_input("ENTER PASSWORD",type="password")
    
    if username=="HEMANTH" and password=="1234":
        admin_navigation()