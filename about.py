import streamlit as st

st.title('Nice to meet you!')

col1, col2 = st.columns(2)

col1.space('medium')
col1.write('Hello, I am Natalie :relaxed:')
col1.write('I\'ve recently graduated from National University of Singapore (NUS), majoring in Data Science and Analytics')
col1.write('I enjoy solving cool problems with data science and love enriching myself by learning new things:woman_technologist:')
col1.write('From time to time, you may spot me going out and exploring the world :earth_asia:')
col1.write('I especially love nature :maple_leaf: and creating memories:sparkles:')

col2.image("mountains.jpg", caption="A beautiful walk around the Siguniang mountain (四姑娘山) in China")

def styled_button(label, link, text_color=None, bg_color=None, hover_text_color=None, hover_bg_color=None):
    bg_color = bg_color or st.get_option("theme.blueColor")
    text_color = text_color or st.get_option("theme.backgroundColor")
    hover_text_color = hover_text_color or st.get_option("theme.textColor")
    hover_bg_color = hover_bg_color or st.get_option("theme.primaryColor")

    st.markdown(
        f"""
        <style>
        .custom-btn {{
            display: inline-flex;             
            justify-content: center;          
            align-items: center;              
            width: 90%;                      
            height: 35px;
            padding: 6px 12px;
            font-size: 16px;
            background-color: {bg_color};
            color: {text_color};
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }}
        .custom-btn:hover {{
            color: {hover_text_color};
            background-color: {hover_bg_color};
        }}
        </style>
        <a href="{link}" target="_blank">
            <button class="custom-btn">{label}</button>
        </a>
        """, 
        unsafe_allow_html=True
    )

col1, col2, col3, col4 = st.columns(4)

with col1:
    styled_button("Email Me 📧", "mailto:nataliejllow@gmail.com?subject=Hello")

with col2:
    styled_button("LinkedIn", "https://www.linkedin.com/in/jia-li-natalie-low/")

with col3:
    styled_button("GitHub", "https://github.com/natalie230")

with col4:
    styled_button("Photos by me 📸", "https://natphotog.my.canva.site/natalie-s-photography-highlights")

st.balloons()