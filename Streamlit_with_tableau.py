import streamlit as st
import streamlit.components.v1 as components 
import graphviz
import datetime
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu


#navbar

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=[
            "About Project",
            "Research Question 1",            
            "Research Question 2",
            "Research Question 3",
            "Conclusion",
        ],
        default_index=0,
    )

df = pd.read_csv(r"All_Parameters.csv")
#Tableau Links
html_water_quality = """<div class='tableauPlaceholder' id='viz1680507672618' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Om&#47;OmdenaBhopal-LendiyaLake&#47;DrinkingWaterQuality&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='OmdenaBhopal-LendiyaLake&#47;DrinkingWaterQuality' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Om&#47;OmdenaBhopal-LendiyaLake&#47;DrinkingWaterQuality&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1680507672618');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='1150px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
html_temperature = """<div class='tableauPlaceholder' id='viz1679222151461' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Om&#47;OmdenaBhopal-LendiyaLake&#47;Temperature-Dash&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /><param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='OmdenaBhopal-LendiyaLake&#47;Temperature-Dash' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Om&#47;OmdenaBhopal-LendiyaLake&#47;Temperature-Dash&#47;1.png' /><param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>         <script type='text/javascript'>                    var divElement = document.getElementById('viz1679222151461');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='1150px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
html_DO_on_ch_tur = """<div class='tableauPlaceholder' id='viz1680507920475' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Om&#47;OmdenaBhopal-LendiyaLake&#47;DOvsCvsTurb&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='OmdenaBhopal-LendiyaLake&#47;DOvsCvsTurb' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Om&#47;OmdenaBhopal-LendiyaLake&#47;DOvsCvsTurb&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1680507920475');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.minWidth='1000px';vizElement.style.maxWidth='100%';vizElement.style.minHeight='850px';vizElement.style.maxHeight=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='1150px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""


st.title("Omdena - VIT Bhopal Chapter")
st.header("Monitoring of Water Quality in Bhopal through Satellite Imagery & GIS System")

#dataframe
st.subheader("Click to observe Dataset")
with st.expander("Dataframe"):
            st.text("Here is the dataset that has been used in this Analysis : ")
            st.dataframe(df, height=600, width=1200) 

#Creating Container
header = st.container()
temperature = st.container()
water_Quality = st.container()
DO_effect = st.container()
Conclusion_Project= st.container()      

#Heading
if selected == "About Project":
    with header :
        st.markdown("Bhopal is also known as The City of Lakes which indicates that Bhopal has a significant quantity of Lakes.\nPeople who live in the area are constantly in contact with chemicals assimilated in the water bodies during Gas Tragedy.\nSurveys done by the Bhopal campaign groups have shown that their environment contains six of the persistent organic pollutants banned by the United Nations for their highly poisonous impacts on the environment and human health, which has now reached 42 areas in Bhopal and continues to spread.\nAccording to the Surveyors, the situation is getting worse, and second and third-generation children are being born with disabilities.\n\nApart from this, during the “Gas Tragedy”, MIC(methyl isocyanide) was released, which reacts with water exothermically and produces carbon dioxide, methylamine, dimethylurea, and/or trimethyl biuret, these chemicals cause adverse effects on human bodies while incorporating itself to water. Swiss lab results show chloroform concentrations as many as 3.5 times higher than drinking-water guidelines from the World Health Organization and U.S. EPA , and carbon tetrachloride at up to 2,400 times higher than the guidelines, which impels us to study various lakes of Bhopal.")
        #workflow
        st.subheader("WorkFlow")
        src_workflow="https://whimsical.com/embed/9h4F2fEq2x3yiPp6Hb9o9V"
        components.iframe(src_workflow, width=350, height=500, scrolling=False)

if selected == "Research Question 1":
    with temperature:
            #Integration of the Graph
            st.subheader("Research Question: What is the variation for Temperature in Monsoon & Before/After Pandemic ?")
            components.html(html_temperature, width=1500, height=900)
            st.subheader("Conclusion of the variation for Temperature in Monsoon & Before/After Pandemic")
            src_temp="https://whimsical.com/embed/Bi2oHYzkFky6Ahy4X5QbYz"
            components.iframe(src_temp, width=680, height=500, scrolling=False)

if selected == "Research Question 2":
    with water_Quality:
            #Integration of the Graph
            st.subheader("Research Question: What is water-quality of the Lake ? ")
            components.html(html_water_quality, width=1500, height=900)
            st.subheader("Conclusion of the Water-Quality of the Lake")
            src_temp="https://whimsical.com/embed/QS43wevQ96nxzxytRSHjjA"
            components.iframe(src_temp, width=800, height=300, scrolling=False)

if selected == "Research Question 3":
    with water_Quality:
            #Integration of the Graph
            st.subheader("Research Question: Is Algae (Chlorophyll) affecting the Lake?")
            components.html(html_DO_on_ch_tur, width=1500, height=900)
            st.subheader("Conclusion of the Algae (Chlorophyll), affecting the Lake")
            src_temp="https://whimsical.com/embed/PZVbgfKAoW95sqFHG7x9x4"
            components.iframe(src_temp, width=700, height=500, scrolling=False)

if selected == "Conclusion":
    with Conclusion_Project:
            #Integration of the Graph
            st.subheader("What is the conclusion of this Project?")
            st.markdown("Zoom in/out to read about the conclusion of all the Research Question. You can observe all the Parameters & How they are affecting the Lake.")
            st.markdown("You will be able to observe:")
            st.markdown("1. Post-Monsoon & Pre-Monsoon Analysis")
            st.markdown("2. Post-Covid & Pre-Covid Analysis")
            st.markdown("3. Change over the Span of 4-5 Years")
            src_temp="https://whimsical.com/embed/LRzb5Pc3Xx4aZi9TatvDiQ"
            components.iframe(src_temp, width=800, height=500, scrolling=False)
            st.balloons()
