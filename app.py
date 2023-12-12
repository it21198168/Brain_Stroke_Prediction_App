import pickle
import pandas as pd
import numpy as np
import streamlit as st
import joblib
from streamlit_option_menu import option_menu



# Load your scikit-learn model using joblib
model = joblib.load('D:\FDM_Project\Trained_model (4).pkl')

rad = option_menu(
    
    menu_title = None, 
    options=["Home","Prediction","About US"],
     icons = ["house-door-fill", "calculator-fill","bar-chart-fill","people-fill"],
    default_index =0,
    orientation = "horizontal",
    
        
)
# rad =  st.sidebar.radio("Navigation",["Home","Prediction","About US",])


if rad == "Prediction":

    st.markdown(
        """
        <style>
        body {
            background-color: #17202A; /* Dark background color */
            color: white;
        }
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #42f54a; /* Green title color */
        }
        .sidebar .css-17v3wfv.e1ro7h5l0 ul li a {
            color: white !important; /* Navigation link color */
        }
        .sidebar .css-17v3wfv.e1ro7h5l0 ul li a:hover {
            color: #42f54a !important; /* Navigation link hover color */
        }
        .css-4dmqd5 {
            background-color: #17202A !important; /* Button background color */
            color: white !important; /* Button text color */
        }
        .css-4dmqd5:hover {
            background-color: #42f54a !important; /* Button hover background color */
            color: white !important; /* Button hover text color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Set a professional dark blue background color
    st.markdown(
        """
        <style>
        body {
            background-color: #17202A;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create a Streamlit app
    st.title("Stroke Prediction App")

    # Add styles for the title
    st.markdown(
        """
        <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #42f54a; /* Green title color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Style the header
    st.header("Please provide the following information:")

    # Create input widgets for user input with placeholders
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=0, max_value=150, step=1, format="%d", key="age_input", help="Enter age")
        if age < 0:
            st.error("Age cannot be negative. Please enter a valid value.")

    with col2:
        avg_glucose_level = st.number_input("Avg. Glucose Level", min_value=0.0, max_value=500.0, step=0.1, format="%.1f", key="glucose_input", help="Enter average glucose level")
        if avg_glucose_level < 0:
            st.error("Avg. Glucose Level cannot be negative. Please enter a valid value.")

    with col3:
        bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, step=0.1, format="%.1f", key="bmi_input", help="Enter BMI")
        if bmi < 0:
            st.error("BMI cannot be negative. Please enter a valid value.")

    # Add space between widgets
    st.markdown("<hr>", unsafe_allow_html=True)

    gender = st.selectbox("Gender", ["Male", "Female"], key="gender_input", help="Select gender")
    hypertension = st.selectbox("Hypertension", ["No", "Yes"], key="hypertension_input", help="Select hypertension status")
    heart_disease = st.selectbox("Heart Disease", ["No", "Yes"], key="heart_disease_input", help="Select heart disease status")
    ever_married = st.selectbox("Ever Married", ["No", "Yes"], key="ever_married_input", help="Select marital status")
    work_type = st.selectbox("Work Type", ["Children","Govt Job","Private", "Self-employed" ], key="work_type_input", help="Select work type")
    smoking_status = st.selectbox("Smoking Status", ["Formerly Smoked", "Never Smoked", "Smokes" ], key="smoking_status_input", help="Select smoking status")
    residence_type = st.selectbox("Residence Type", ["Rural", "Urban"], key="residence_type_input", help="Select residence type")

    # Convert categorical inputs to numerical values
    gender_n = 1 if gender == "Male" else 0
    hypertension_n = 1 if hypertension == "Yes" else 0
    heart_disease_n = 1 if heart_disease == "Yes" else 0
    ever_married_n = 1 if ever_married == "Yes" else 0
    work_type_n = ["Children","Private" ,"Govt Job","Self-employed" ].index(work_type)
    smoking_status_n = ["Formerly Smoked", "Never Smoked", "Smokes" ].index(smoking_status)
    residence_n = ["Rural","Urban" ].index(residence_type)

    # Create a DataFrame with user inputs
    data = {
        'age': [age],
        'avg_glucose_level': [avg_glucose_level],
        'bmi': [bmi],
        'gender_n': [gender_n],
        'hypertension_n': [hypertension_n],
        'heartDisesas_n': [heart_disease_n],
        'everMarried_n': [ever_married_n],
        'Wtype_n': [work_type_n],
        'Smoikng_status': [smoking_status_n],
        'residence_n': [residence_n]
    }
    prediction_data = pd.DataFrame(data)

    # Style the Predict button
    st.markdown(
        """
        <style>
        .stButton button {
            background-color: #42f54a;
            color: white;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 4px;
            padding: 10px 20px;
        }
        </style>
        
        """,
        unsafe_allow_html=True
    )






    # Create a button to make predictions
    if st.button("Predict", key="predict_button"):
        prediction = model.predict(prediction_data)
        import streamlit as st

        # Assuming you have your prediction_text
        prediction_text = "Positive" if prediction[0] else "Negative"

        # Define CSS styles for "Positive" and "Negative"
        positive_style = 'color: red;'
        negative_style = 'color: blue;'

        # Use HTML and CSS to change text color
        if prediction_text == "Positive":
            st.markdown(f'<p style="{positive_style}">Stroke Prediction: {prediction_text}</p>', unsafe_allow_html=True)
        else:
            st.markdown(f'<p style="{negative_style}">Stroke Prediction: {prediction_text}</p>', unsafe_allow_html=True)

        if prediction[0]:  # If the prediction is positive
            st.write('<p><b style="color: red;">You have been diagnosed with Stroke Risk.</b></p><br><p style="color: red;">The algorithm has diagnosed you with Stroke Risk based on your inputs. Please consult a Doctor.</p>', unsafe_allow_html=True)
        else:
            st.write('<p><b style="color: blue;">You have been diagnosed with no Stroke Risk.</b> Congratulations.</p><br><p style="color: red;">The algorithm has diagnosed you with no Stroke Risk based on your inputs. However, it might be better to talk to a doctor regardless.</p>', unsafe_allow_html=True)

    # Data for visualization (you can use user input data)
    numerical_data = {
        "Age": age,
        "Average Glucose Level": avg_glucose_level,
        "BMI": bmi,
    }


    # Determine the sugar level message based on the glucose level
    sugar_level_message = ""
    if avg_glucose_level < 70.0:
        sugar_level_message = "Sugar level is low, meet a doctor"
    elif 70.0 <= avg_glucose_level <= 120.0:
        sugar_level_message = "Good blood sugar level"
    else:
        sugar_level_message = "Sugar level is high, meet a doctor immediately"

    # Create a bar chart using Plotly
    data_keys = list(numerical_data.keys())
    data_values = list(numerical_data.values())
    
    import plotly.graph_objects as go



    fig = go.Figure()
    fig.add_trace(go.Bar(x=data_keys, y=data_values, text=[sugar_level_message], textposition='inside'))

    # Custom CSS for the bar chart
    fig.update_layout(
        plot_bgcolor='#17202A',  # Change the background color to dark blue (#17202A)
        paper_bgcolor='#17202A',  # Change the plot paper color to dark blue (#17202A)
        font=dict(color='white'),  # Change text color to white
        title="User Input Data Visualization",  # Add a title
        xaxis_title="Numerical Data",  # Add x-axis title
        yaxis_title="Values",  # Add y-axis title
        title_font=dict(size=28),  # Change title font size
        xaxis=dict(
            tickfont=dict(size=14),  # Customize x-axis tick font size
        ),
        yaxis=dict(
            tickfont=dict(size=14),  # Customize y-axis tick font size
        ),
    )

    # Display the bar chart in the Streamlit app
    st.plotly_chart(fig)


if rad == "Home":

    

    st.markdown(
        f"""
        <style>
        body {{
            background-color: #ADD8E6;  /* Set your desired background color */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    
    import streamlit as st

# Create a page 'state' to switch between pages
    page = st.session_state.page if hasattr(st.session_state, "page") else 'home'

    # Create a creative banner
    st.markdown(
    """
    <div style="background-color: #ADD8E6; padding: 1rem; text-align: center; width: 100%;">
   
    <h1 style="color: black; font-size: 3rem;">🧠 Stroke Prediction </h1>
     <p style="color: black; font-size: 1.5rem;">Predict the likelihood of a stroke</p>
    </div>
    """,
    unsafe_allow_html=True,
)


    # Check the current page
    if page == 'home':
        # Introduction and description
        



        

        # Create an engaging illustration or image
        st.image(
    "https://media.istockphoto.com/id/1249957366/photo/brain-stroke.jpg?s=612x612&w=0&k=20&c=jxe-N4MUYBFsxQnq1D63gMNKNCe0hxAtEkrypi0PX1k=",
    width=705,  # Set the desired width in pixels
    
)



        # Information about strokes
        st.write(
    '<div "><span style="font-size: 30px; font-family: Arial, sans-serif;">Understanding Strokes</span></div>',
    unsafe_allow_html=True
)

        st.write(
            '<p style="font-size: 20px;">A stroke is your brain’s equivalent of a heart attack, happening when there’s an issue with blood flow to part of your brain. This can happen when blood vessels are blocked or because of bleeding in your brain. Strokes are a life-threatening emergency, and immediate medical attention is critical to prevent permanent damage or death.</p>',unsafe_allow_html=True
        )

        # Get Started button to navigate to another page
        

        # Add your prediction form or content here.

    # Create a footer with social media links
    st.markdown(
        """
        <div style="background-color: #3366cc; padding: 2rem; text-align: center;">
            <p style="color: white; font-size: 1.5rem;">Connect with us:</p>
            <a href="https://twitter.com/YourTwitterProfile" target="_blank" style="color: white; margin: 0 10px;">
                <img src="https://img.icons8.com/material-rounded/24/000000/twitter.png"/>
            </a>
            <a href="https://www.linkedin.com/in/yourlinkedinprofile" target="_blank" style="color: white; margin: 0 10px;">
                <img src="https://img.icons8.com/material-outlined/24/000000/linkedin.png"/>
            </a>
            <a href="https://github.com/yourgithubprofile" target="_blank" style="color: white; margin: 0 10px;">
                <img src="https://img.icons8.com/material-rounded/24/000000/github.png"/>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

   




if rad == "About US":

# Page title
    st.title("About Us")

    st.write("Welcome to our project group! We are a team of dedicated individuals working together to achieve our project goals. We are passionate about what we do and committed to delivering high-quality results. Get to know each of our team members below.")

    # Define your team members and their details
    team_members = [
        {
            "name": "Team Member 1",
            "photo_url": "https://cdn-icons-png.flaticon.com/512/2919/2919906.png",
            "details": "Team Member 1: Siriwardana L.H.E.R - IT21211300(Team Leader)",
        },
        {
            "name": "Team Member 2",
            "photo_url": "https://cdn-icons-png.flaticon.com/512/2919/2919906.png",
            "details": "Team Member 2: Muthukumari T.R.V. - IT21480522",
        },
        {
            "name": "Team Member 3",
            "photo_url": "https://cdn-icons-png.flaticon.com/512/2919/2919906.png",
            "details": "Team Member 3: Weerasekara N.P - IT21198168"
        },
        {
            "name": "Team Member 4",
            "photo_url": "https://cdn-icons-png.flaticon.com/512/2919/2919906.png",
            "details": "Team Member 4: Deheragoda D.M.L.M - IT21480218",
        },
    ]

    # Create columns for displaying photos horizontally
    columns = st.columns(4)

    # Display team members
    for i, member in enumerate(team_members):
        col = columns[i]
        col.subheader(member["name"])
        col.image(member["photo_url"], caption="Photo of " + member["name"], use_column_width=True)
        col.write(member["details"])