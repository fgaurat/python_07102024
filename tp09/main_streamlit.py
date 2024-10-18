import streamlit as st
from CustomerDAO import CustomerDAO

# streamlit run main_streamlit.py

def main():
    st.write("# Le titre")
    title = st.text_input("Movie title", "Life of Brian")
    if st.button('Say Hello'):
        st.write("The current movie title is", title)
    dao = CustomerDAO("customers_db.db")
    customers = dao.findAll()
    st.table(customers)        
if __name__=='__main__':
    main()
