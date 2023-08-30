import streamlit as st 
from streamlit_timeline import st_timeline
import neurokit2 as nk
from streamlit_extras.metric_cards import style_metric_cards


def show_ecg ():
    ecg_signal = nk.ecg_simulate(duration=30, sampling_rate=250)
    st.line_chart(ecg_signal)



st.set_page_config(page_title="AFIB", layout="wide")
st.title("AFIB features V1")

st.subheader("Vue global de la semaine")

overview_col_1,overview_col_2 = st.columns([1,3])

with overview_col_1:
    st.write("ECG results by Heart Rate")
    st.write('Possible Afib:  3')
    st.write('Undetermined:   1')

with overview_col_2: 

    items = [
    {"id": 1, "content": "AFIB", "start": "2023-08-30", "hour":"12:00:10","detail":"Test pb afib"},
    {"id": 2, "content": "AFIB", "start": "2023-08-30","detail":"Test pb afib"},
    {"id": 3, "content": "Undetermined", "start": "2023-08-28","detail":"Test pb afib"},
   
    ]
    timeline = st_timeline(items, groups=[], options={},  height="300px")
    
    st.subheader("Selected item")
    try :
        st.write("Detail : ",timeline["detail"])
    except :
        st.warning("No session selected")
    show_ecg()




def alerte_card ():
    
    my_card = st.container()
#     my_card.markdown(
#     """
#     <style>
#         .css-1ceev1o.e1f1d6gn0{
#         background-color: red;
#         }

#     </style>

#     """, unsafe_allow_html= True
# )




day_expander = st.expander("10/12/2023")
day_expander.markdown(
"""
<style>
    .st-bg.st-b8.st-bn.st-bo.st-ct.st-bq.st-br.st-bs.st-bt.st-bu.st-bv.st-bw.st-bx.st-by.st-bz.st-c0{
    background-color: white;
    border-radius :10px
    }

</style>

""", unsafe_allow_html= True
)
day_expander_col_1, day_expander_col_2 = day_expander.columns([1,2])
day_expander_col_1.write("Kardia Instant Analysis\n\nPossible Atrial Fibrilation\n\nHR : 120")

with day_expander_col_2:       
    show_ecg()

