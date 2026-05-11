import streamlit as st
import os

# Make sure secrets are read 
#θα τα βάλω μετά (supabase για login)
#supabase_url = st.secrets["supabase_connection"]["url"]
#supabase_key = st.secrets["supabase_connection"]["key"]
# Register them as environment variables so st_login_form can see them
#os.environ["SUPABASE_URL"] = supabase_url
#os.environ["SUPABASE_KEY"] = supabase_key

#from st_supabase_connection import SupabaseConnection

#st_supabase_client = st.connection(
   # name="supabase_connection",
   # type=SupabaseConnection,
    #ttl=None
   # )


st.set_page_config(page_title="SAF_WEED Dashboard", layout="centered")

st.title("🌿 SAF_WEED Dashboard")
#επίσης supabase
#if not st.session_state.get("authenticated", False):
    #st.markdown(
        #"""
        #<style>
            #[data-testid="stSidebar"] {display: none;}
        #</style>
        #""",
        #unsafe_allow_html=True
    #)
    #st.warning("Please log in to access the dashboard.")
#else:
    #st.sidebar.success("Select Any Page from here")
#----- login form
#from st_login_form import login_form
#supabase_connection = login_form()

#if st.session_state["authenticated"]:
    
    #if st.session_state["username"]:
        #st.success(f"Welcome {st.session_state['username']}")
        #...

    #else:
        #st.success("Welcome guest")
        #...
#else:
    #st.error("Not authenticated")
    
    