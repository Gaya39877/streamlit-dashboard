# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from streamlit_option_menu import option_menu
# from numerize.numerize import numerize 
# from query import *
# import time

# st.set_page_config(page_title ="Dashboard",page_icon="🌍", layout= "wide")
# st.subheader("🔔 Insurance Descriptive Analysis")
# st.markdown("##")


# # fetch data
# result = view_all_data()
# df=pd.DataFrame(result,columns=['Policy','Expiry','Location','State','Region','Investment','Construction','BusinessType','Earthquake','Flood','Rating','id'])

# # sidebar
# st.sidebar.image('data/logo1.png', caption='Online Analytics')

# #switcher
# st.sidebar.header('please filter')
# region=st.sidebar.multiselect(
#     "select Region" ,
#     options = df['Region'].unique(),
#     default =df['Region'].unique(),
# )
# location=st.sidebar.multiselect(
#     "select Location" ,
#     options = df['Location'].unique(),
#     default =df['Location'].unique(),
# )
# construction=st.sidebar.multiselect(
#     "select Construction" ,
#     options = df['Construction'].unique(),
#     default =df['Construction'].unique(),
# )

# df_selection = df.query(
#     "Region == @region & Location ==@location & Construction == @construction"
# )

# def Home():
#     with st.expander("Tabular"):
#         showData=st.multiselect('Filter:' , df_selection.columns, default=[])
#         st.write(df_selection[showData])

#         # compute top analytics
#         total_investment = df_selection["Investment"].sum()
#         investment_mode = df_selection["Investment"].mode()[0]
#         investment_mean = df_selection["Investment"].mean()
#         investment_median = df_selection["Investment"].median()
#         rating = df_selection["Rating"].sum()


#         total1, total2, total3, total4, total5 = st.columns(5, gap='large')
#         with total1:
#             st.info('Total Investment', icon="📌")
#             st.metric(label="sum TZS", value=f"{total_investment:,.0f}")
#         with total2:
#             st.info('Most Frequent', icon="📌")
#             st.metric(label="mode TZS", value=f"{investment_mode:,.0f}")
#         with total3:
#             st.info('Average', icon="📌")
#             st.metric(label="average TZS", value=f"{investment_mean:,.0f}")
#         with total4:
#             st.info('Central Earnings', icon="📌")
#             st.metric(label="median TZS", value=f"{investment_median:,.0f}")
#         with total5:
#             st.info('Ratings', icon="📌")
#             # Using numerize without the help argument
#             st.metric(label="Rating",value=numerize(rating),help=f""" Total Rating: {rating} """)
        
#         st.markdown("""---""")

# # graphs
# def graphs():
#     #total_investment = int(df_selection["Investment"]).sum()
#     #average_rating = int(round(df_selection["Rating"]).mean(),2)

#     # simple bar graph
#     investment_by_business_type=(
#         df_selection.groupby(by=["BusinessType"]).count()[["Investment"]].sort_values(by="Investment")
#     )

#     fig_investment=px.bar(
#         investment_by_business_type,
#         x="Investment",
#         y=investment_by_business_type.index,
#         orientation="h",
#         title="<b> Investment by Business Type </b>",
#         color_discrete_sequence=["#00712D"]*len(investment_by_business_type),
#         template="plotly_white",
#     )

#     fig_investment.update_layout(
#         plot_bgcolor="rgba(0,0,0,0)",
#         xaxis=(dict(showgrid=False))
#     )

#     # simple line graph
#     investment_state=df_selection.groupby(by=["State"]).count()[["Investment"]]
    
#     fig_state=px.line(
#         investment_state,
#         x=investment_state.index,
#         y="Investment",
#         orientation="v",
#         title="<b> Investment by State </b>",
#         color_discrete_sequence=["#00712D"]*len(investment_state),
#         template="plotly_white",
#     )

#     fig_state.update_layout(
#         xaxis=dict(tickmode="linear"),
#         plot_bgcolor="rgba(0,0,0,0)",
#         yaxis=(dict(showgrid=False))
#     )

#     left, right= st.columns(2)
#     left.plotly_chart(fig_state, use_container_width=True)
#     right.plotly_chart(fig_investment, use_container_width=True)

# def Progressbar():
#     st.markdown(""" <style>.stProgress  >div > div > div > div { background-image: linear-gradient(to right, #99ff99 , #FFF00)}</style>""", unsafe_allow_html=True,)
#     target=3000000000
#     current=df_selection["Investment"].sum()
#     percent=round((current/target*100))
#     mybar = st.progress(0)


#     if percent>100:
#         st.subheader("Target done !")
#     else:
#         st.write("you have", percent, "% " , "of ", (format(target, 'd')), "TZS")
#         for percent_complete in range(percent):
#             time.sleep(0.1)
#             mybar.progress(percent_complete+1, text="Target Percentage")

# def sidebar():  
    
#     with st.sidebar:
#         selected=option_menu(
#             menu_title="Main Menu",
#             options=["Home", "Progress"],
#             icons=["house","eye"],
#             menu_icon="cast",
#             default_index=0
#         )
#     if selected=="Home":
#         st.subheader(f"Page: {selected}")
#         Home()
#         graphs()

#     if selected=="Progress":
#         st.subheader(f"Page: {selected}")
#         Progressbar()
#         graphs()

# sidebar()

# #theme
# hide_st_style="""

# <style>
# #MainMenu {visibility:hidden;}
# footer {visibility:hidden;}
# header {visibility:hidden;}
# </style>
# """

import streamlit as st

# st.set_page_config must be the first Streamlit command
st.set_page_config(page_title="Dashboard", page_icon="🌍", layout="wide")

import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize 
from query import view_all_data
import time

st.subheader("🔔 Insurance Descriptive Analysis")
st.markdown("##")

# fetch data
result = view_all_data()
# Debug: Check if data is fetched
if not result:
    st.error("No data fetched from the database.")
else:
    st.write("Data fetched successfully!")


df = pd.DataFrame(result, columns=['Policy', 'Expiry', 'Location', 'State', 'Region', 'Investment', 'Construction', 'BusinessType', 'Earthquake', 'Flood', 'Rating', 'id'])

# sidebar
st.sidebar.image('data/logo1.png', caption='Online Analytics')

#switcher
st.sidebar.header('please filter')
region = st.sidebar.multiselect(
    "select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique(),
)
location = st.sidebar.multiselect(
    "select Location",
    options=df['Location'].unique(),
    default=df['Location'].unique(),
)
construction = st.sidebar.multiselect(
    "select Construction",
    options=df['Construction'].unique(),
    default=df['Construction'].unique(),
)

df_selection = df.query(
    "Region == @region & Location ==@location & Construction == @construction"
)

def Home():
    with st.expander("Tabular"):
        showData = st.multiselect('Filter:', df_selection.columns, default=[])
        st.write(df_selection[showData]) 

        # compute top analytics
        total_investment = df_selection["Investment"].sum()

        # Handle mode calculation safely
        investment_mode = df_selection["Investment"].mode()
        if not investment_mode.empty:
            investment_mode_value = investment_mode[0]
        else:
            investment_mode_value = 0  # or any default value

        investment_mean = df_selection["Investment"].mean()
        investment_median = df_selection["Investment"].median()
        rating = df_selection["Rating"].sum()

        # compute top analytics
        # total_investment = df_selection["Investment"].sum()
        # investment_mode = df_selection["Investment"].mode()[0]
        # investment_mean = df_selection["Investment"].mean()
        # investment_median = df_selection["Investment"].median()
        # rating = df_selection["Rating"].sum()

        total1, total2, total3, total4, total5 = st.columns(5, gap='large')
        with total1:
            st.info('Total Investment', icon="📌")
            st.metric(label="sum TZS", value=f"{total_investment:,.0f}")
        with total2:
            st.info('Most Frequent', icon="📌")
            st.metric(label="mode TZS", value=f"{investment_mode_value:,.0f}")
        # with total2:
        #     st.info('Most Frequent', icon="📌")
        #     st.metric(label="mode TZS", value=f"{investment_mode:,.0f}")
        with total3:
            st.info('Average', icon="📌")
            st.metric(label="average TZS", value=f"{investment_mean:,.0f}")
        with total4:
            st.info('Central Earnings', icon="📌")
            st.metric(label="median TZS", value=f"{investment_median:,.0f}")
        with total5:
            st.info('Ratings', icon="📌")
            st.metric(label="Rating", value=numerize(rating), help=f""" Total Rating: {rating} """)
        
        st.markdown("""---""")

# graphs
def graphs():
    investment_by_business_type = (
        df_selection.groupby(by=["BusinessType"]).count()[["Investment"]].sort_values(by="Investment")
    )

    fig_investment = px.bar(
        investment_by_business_type,
        x="Investment",
        y=investment_by_business_type.index,
        orientation="h",
        title="<b> Investment by Business Type </b>",
        color_discrete_sequence=["#00712D"] * len(investment_by_business_type),
        template="plotly_white",
    )

    fig_investment.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=(dict(showgrid=False))
    )

    investment_state = df_selection.groupby(by=["State"]).count()[["Investment"]]

    fig_state = px.line(
        investment_state,
        x=investment_state.index,
        y="Investment",
        orientation="v",
        title="<b> Investment by State </b>",
        color_discrete_sequence=["#00712D"] * len(investment_state),
        template="plotly_white",
    )

    fig_state.update_layout(
        xaxis=dict(tickmode="linear"),
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=(dict(showgrid=False))
    )

    left, right = st.columns(2)
    left.plotly_chart(fig_state, use_container_width=True)
    right.plotly_chart(fig_investment, use_container_width=True)

def Progressbar():
    st.markdown("""<style>.stProgress >div > div > div > div { background-image: linear-gradient(to right, #99ff99 , #FFF00)}</style>""", unsafe_allow_html=True)
    target = 3000000000
    current = df_selection["Investment"].sum()
    percent = round((current / target * 100))
    mybar = st.progress(0)

    if percent > 100:
        st.subheader("Target done!")
    else:
        st.write(f"you have {percent}% of {format(target, 'd')} TZS")
        for percent_complete in range(percent):
            time.sleep(0.1)
            mybar.progress(percent_complete + 1, text="Target Percentage")

def sidebar():
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",
            options=["Home", "Progress"],
            icons=["house", "eye"],
            menu_icon="cast",
            default_index=0
        )
    if selected == "Home":
        st.subheader(f"Page: {selected}")
        Home()
        graphs()

    if selected == "Progress":
        st.subheader(f"Page: {selected}")
        Progressbar()
        graphs()

sidebar()

#theme
hide_st_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
