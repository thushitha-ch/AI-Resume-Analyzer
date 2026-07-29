# streamlit
# it is a python third party library / package which is used to build user interface 
# based on with python
# pip install streamlit
# python -m streamlit run fe.py
# email
# pip install requests
# python -m pip install requests
import streamlit as st
import requests as r

be_server_url_loc="http://127.0.0.1:8000"
st.title("AI RESUME ANALYZER")

resume=st.file_uploader("UploadResumePdf", type=["pdf"])

submit_btn=st.button("Analyze Resume")

if submit_btn:
    if resume is None:
        st.warning("please upload a PDF resume.")
    else:
        response=r.post(
            f"{be_server_url_loc}/analyze_resume", 
            files={
                "resume":resume
            }
        )
        st.write(response)
        if response.status_code == 200:
            st.markdown(response.json()["msg"])
        else:
            st.error("Something went wrong.")
    