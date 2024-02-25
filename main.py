import streamlit as st
import psycopg2
import pandas as pd
from streamlit_option_menu import option_menu

# Function to create a database connection
def get_db_connection():
    connection = psycopg2.connect(
        dbname="project",
        user="postgres",
        password="102001",
        host="localhost",
        port="5432"
    )
    return connection


def main():
    st.title("User Login App")
    menu = st.selectbox("Menu", ["Login", "Register"])

    if menu == "Login":
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if check_credentials(username, password):
                st.success(f"Logged in as {username}")
            else:
                st.error("Invalid credentials")

    elif menu == "Register":
        st.subheader("Register")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")

        if st.button("Register"):
            register_user(new_username, new_password)
            st.success("Registration successful! You can now login.")

def insert_data(owner,district,taluk,types,age,mobile,bedrooms,sqft,description,price):
    connection = get_db_connection()
    cursor = connection.cursor()
    query=f"INSERT INTO propertydata (owner,district,taluk,type,age,mobile,bedrooms,sqft,description,price)  VALUES ('{owner}','{district}','{taluk}','{types}','{age}','{mobile}','{bedrooms}','{sqft}','{description}','{price}')"
    cursor.execute(query)
    connection.commit()
    connection.close()
    execu_add()
    
def execu_add():
    if insert_data:
        st.success("SUCCESSFULLY ADDED")
    else:
        st.warning("UNABLE TO ADD")
        
def view_connect():
    connection = get_db_connection()
    cursor = connection.cursor()
    query="SELECT * FROM propertydata"
    cursor.execute(query)
    column_names = [i[0] for i in cursor.description] 
    data=cursor.fetchall()
    connection.commit()
    connection.close()
    
    return column_names,data
    
def view1():
    column_names,data = view_connect()
    if data:
        df=pd.DataFrame(data,columns=column_names)
       
        st.table(df)
    else:
        st.warning("NO DATA TO DISPLAY")
    
    

def delete_data(property_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    property_id=int(property_id)
    query=f"DELETE FROM propertydata WHERE property_id='{property_id}'"
    cursor.execute(query)
    connection.commit()
    connection.close()
    execu_del()
    
def execu_del():
    if delete_data:
        st.success("SUCCESSFULLY DELETED")
    else:
        st.warning("UNABLE TO DELETE")
    
def csv_add(file):
    connection = get_db_connection()
    cursor = connection.cursor()
    with open(file, "r") as f:
        for line in f:
            line = line.strip()
            dataset = line.split(",")
            if dataset[0]!="owner":
                cursor.execute('INSERT INTO propertydata (owner,district,taluk,type,age,mobile,bedrooms,sqft,description,price) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)',(dataset[0],dataset[1],dataset[2],dataset[3],dataset[4],dataset[5],int(dataset[6]),float(dataset[7]),dataset[8],float(dataset[9])))
    st.write("IMPORTED SUCCESSFULLY")
    connection.commit()
    connection.close()   

def search_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT taluk FROM propertydata ORDER BY taluk")
    city = [row[0] for row in cursor.fetchall()]
    
    connection.commit()
    connection.close()
    return city

def search_data1():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT DISTINCT type FROM propertydata")
    types = [row[0] for row in cursor.fetchall()]
    
    connection.commit()
    connection.close()
    return types

def search_crit(city):
    connection = get_db_connection()
    cursor = connection.cursor()
    query=f"SELECT * FROM propertydata WHERE taluk = '{city}'"
    cursor.execute(query)
    column_names = [i[0] for i in cursor.description] 
    data=cursor.fetchall()
    connection.commit()
    connection.close()
    df=pd.DataFrame(data,columns=column_names)
   
    st.table(df)
    
def search_crit1(city,types):
    connection = get_db_connection()
    cursor = connection.cursor()
    query=f"SELECT * FROM propertydata WHERE taluk = '{city}' AND type = '{types}'"
    cursor.execute(query)
    column_names = [i[0] for i in cursor.description] 
    data=cursor.fetchall()
    connection.commit()
    connection.close()
    df=pd.DataFrame(data,columns=column_names)
   
    st.table(df)
    
def excel_add(file):
    connection = get_db_connection()
    cursor = connection.cursor()
    with open(file, "r",encoding='cp437') as f:
        for line in f:
            line = line.strip()
            dataset = line.split(",")
            st.write(dataset)
            #if dataset[0]!="owner":
                #cursor.execute('INSERT INTO propertydata (owner,mobile,district,taluk,type,age,bedrooms,sqft,description,price) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)',(dataset[0],dataset[1],dataset[2],dataset[3],dataset[4],dataset[5],dataset[6],dataset[7],dataset[8],dataset[9]))
    st.write("IMPORTED SUCCESSFULLY")
    connection.commit()
    connection.close()   
    
            
def export_file(file):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM propertydata")
    a=cursor.fetchall()
    tocsv=pd.DataFrame(a)
    tocsv.to_csv(file,index=False) 
            
    connection.commit()
    connection.close() 
 
def insert_data1(name,mobile_number,property_id,query):
    connection = get_db_connection()
    cursor = connection.cursor()
    query=f"INSERT INTO querybox (name,mobile_number,property_id,query)  VALUES ('{name}','{mobile_number}','{property_id}','{query}')"
    cursor.execute(query)
    connection.commit()
    connection.close()
    execu_add1()

def execu_add1():
    if insert_data:
        st.success("SUCCESSFULLY QUERY ADDED")
    else:
        st.warning("UNABLE TO ADD QUERY")
        
        
def data_query():
    connection = get_db_connection()
    cursor = connection.cursor()
    query="SELECT * FROM querybox"
    cursor.execute(query)
    column_names = [i[0] for i in cursor.description] 
    data=cursor.fetchall()
    connection.commit()
    connection.close()
    
    return column_names,data
    
def view_query():
    column_names,data = data_query()
    if data:
        df=pd.DataFrame(data,columns=column_names)
       
        st.table(df)
    else:
        st.warning("NO DATA TO DISPLAY")
        
def register_admin():
    username=st.text_input("ENTER NAME")
    password=st.text_input("ENTER PASSWORD")
    
    but=st.button("SUBMIT")
    connection = get_db_connection()
    cursor = connection.cursor()
    if but:
        
        query=f"INSERT INTO admin_panel (username,password) VALUES ('{username}','{password}')"
        a=cursor.execute(query)
        login_admin()
    else:
        pass
    
    connection.commit()
    connection.close()
    

    

     
connection = get_db_connection()
cursor = connection.cursor()
cursor.execute("SELECT DISTINCT type FROM propertydata")
types = [row[0] for row in cursor.fetchall()]
print(types)
connection.commit()
connection.close()

   

    