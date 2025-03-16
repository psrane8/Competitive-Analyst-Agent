__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st
import main
import sys,re
import os 
class StreamToContainer:
    def __init__(self,container):
        self.container=container
        self.buffer=[]
        self.colors=['red','green','blue','orange']
        self.colorIndex=0
   
    def write(self,data):
        # Filter out ANSI escape codes using a regular expression
        cleaned_data = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)
       
        self.buffer.append(cleaned_data)
        if "\n" in data:
            self.container.markdown(''.join(self.buffer) , unsafe_allow_html=True)
            self.buffer = []


#retrieve the user defined OpenAI api key 
gemini_api_key = st.sidebar.text_input('Gemini API Key', type='password')
os.environ['GEMINI_API_KEY']=gemini_api_key
st.sidebar.write("Create a new Gemini API Key for LLM access \nhttps://aistudio.google.com/app/apikey")
seper_api_key = st.sidebar.text_input('Serper API Key', type='password')
os.environ['SERPER_API_KEY']=seper_api_key
st.sidebar.write("Create a new Serper API Key for Internet Search access  \nhttps://serper.dev/api-key")


st.header("WATM's Competitive Analyst Agentic System")
st.subheader("Generate a Competitive Analysis Report",divider="rainbow",anchor=False)
 
with st.form("form"):
    company_name=st.text_input("Enter the name of the Company",key="company_name")
    submitted=st.form_submit_button("Submit")


if company_name and submitted and seper_api_key and gemini_api_key:
    with st.status("🤖 **Agents at work...**",expanded=True,state="running") as status:
        with st.container(height=300):
            sys.stdout = StreamToContainer(st)
            inputs = {"company_name":company_name}
            result=main.run(inputs)
           
        status.update(label="✅ Your Report is ready",state="complete", expanded=False)
    st.subheader("Competitive Analysis Report is ready!", anchor=False, divider="rainbow")
    st.markdown(result)

else:
    st.error("Please make sure to add the company name, Gemini & Serper API key to continue",icon="🚨")
