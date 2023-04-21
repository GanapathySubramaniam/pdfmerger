import streamlit as st
from PyPDF2 import PdfMerger
import io

def callback(button_name):
    st.session_state[button_name]=True

def add_to_session_state(key,value):
    if key not in st.session_state.keys():
        st.session_state[key]=value
    
add_to_session_state('Merge PDF',False)




def merge_pdfs(pdfs_list):
    merger=PdfMerger()
    for pdf in pdfs_list:
        merger.append(pdf) 
    output = io.BytesIO()
    merger.write(output)
    output.seek(0)
    return output
    


def app():
    st.header("PDF MERGER")
    new_name=st.text_input('Enter the Name of the combined file')
    pdf_files_list=st.file_uploader('Select the PDFS to be merged ', type=None, accept_multiple_files=True,label_visibility="visible")
    if st.button('Merge PDF',on_click=callback,args=['Merge PDF']) or st.session_state['Merge PDF']:
            pdf_data=merge_pdfs(pdf_files_list)
            st.success('PDFS Merged!!')
            st.download_button('Download the Combined PDF',data=pdf_data.getvalue(),file_name=new_name)
                 





app()
