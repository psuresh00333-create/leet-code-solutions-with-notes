# ===============================
# Migrant Help App – Streamlit (Expanded, Fully Online)
# ===============================
import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime
from random import choice, sample

# ===============================
# APP CONFIG
# ===============================
st.set_page_config(page_title="Migrant Help App", page_icon="🏠", layout="wide")
st.title("🏠 Migrant Help App")
st.markdown("**Helping Migrants Access Jobs, Shelters, Chat, AI Job Suggestions, Emergency Services & More!**")

# ===============================
# SIDEBAR: USER INFO
# ===============================
st.sidebar.header("User Info")
user_name = st.sidebar.text_input("Enter your Name")
user_city = st.sidebar.text_input("Your City")
if st.sidebar.button("Save Info"):
    st.sidebar.success(f"Hello {user_name if user_name else 'User'} from {user_city if user_city else 'Unknown'}!")

# ===============================
# HOME SCREEN BUTTONS
# ===============================
st.subheader("Choose an Option:")
col1, col2 = st.columns(2)
with col1:
    find_jobs = st.button("💼 Find Jobs")
    find_shelters = st.button("🏘️ Find Shelters")
    food_help = st.button("🍲 Food Assistance")
    ai_job = st.button("🤖 AI Job Suggestion")
    chat_help = st.button("💬 Chat")
with col2:
    sos_emergency = st.button("🚨 SOS Emergency")
    translation = st.button("🌐 Translate Text")
    volunteer_reg = st.button("🤝 Volunteer Registration")
    feedback_btn = st.button("📝 Feedback / Suggestions")
    faq_btn = st.button("❓ FAQ / Tips")

# ===============================
# FEATURE 1: FIND JOBS (SAMPLE DATA)
# ===============================
if find_jobs:
    st.header("💼 Available Jobs")
    jobs = pd.DataFrame({
        "Job Title": ["Cleaner", "Driver", "Cook", "Delivery Agent", "Electrician", "Data Entry", "Customer Service", "Helper", "Security Guard"],
        "City": ["Hyderabad", "Bangalore", "Delhi", "Mumbai", "Chennai", "Kolkata", "Pune", "Jaipur", "Ahmedabad"],
        "Contact": ["12345","67890","54321","24680","13579","98765","43210","56789","11223"]
    })
    st.dataframe(jobs)

# ===============================
# FEATURE 2: FIND SHELTERS
# ===============================
if find_shelters:
    st.header("🏘️ Nearby Shelters")
    if st.button("Open Map"):
        webbrowser.open("https://www.google.com/maps/search/shelters+near+me/")

# ===============================
# FEATURE 3: FOOD ASSISTANCE
# ===============================
if food_help:
    st.header("🍲 Food Assistance")
    if st.button("Find Free Food Centers"):
        webbrowser.open("https://www.google.com/maps/search/free+food+centers+near+me/")

# ===============================
# FEATURE 4: AI JOB SUGGESTION (SIMULATED)
# ===============================
if ai_job:
    st.header("🤖 AI Job Suggestions (Simulated)")
    skills = st.text_input("Enter your skills (comma separated):")
    if st.button("Suggest Jobs"):
        if skills != "":
            sample_jobs = [
                "Cleaner", "Driver", "Cook", "Delivery Agent", "Electrician",
                "Data Entry Operator", "Customer Service", "Helper", "Security Guard", "Delivery Executive", "Warehouse Staff"
            ]
            suggested_jobs = sample(sample_jobs, 5)
            st.success(f"Based on your skills [{skills}], suggested jobs: {', '.join(suggested_jobs)}")
        else:
            st.warning("Enter skills first")

# ===============================
# FEATURE 5: CHAT (SIMULATED)
# ===============================
chat_history = st.session_state.get("chat_history", [])

if chat_help:
    st.header("💬 Chat with Volunteers (Simulated)")
    chat_message = st.text_input("Type your message here:")
    if st.button("Send Message"):
        if chat_message != "":
            chat_history.append(f"{user_name if user_name else 'User'}: {chat_message}")
            st.session_state["chat_history"] = chat_history
            st.success("Message sent!")
    if chat_history:
        st.subheader("Chat History")
        for msg in chat_history:
            st.write(msg)

# ===============================
# FEATURE 6: SOS EMERGENCY
# ===============================
if sos_emergency:
    st.header("🚨 SOS Emergency")
    if st.button("Send SOS"):
        webbrowser.open("https://www.google.com/maps/search/my+location/")

# ===============================
# FEATURE 7: TRANSLATION (SIMULATED)
# ===============================
if translation:
    st.header("🌐 Translate Text (Simulated)")
    text_to_translate = st.text_area("Enter text:")
    lang_code = st.selectbox("Select Language", ["Hindi", "Telugu", "Bengali", "Marathi", "Tamil", "Malayalam", "Kannada"])
    if st.button("Translate Text"):
        if text_to_translate != "":
            st.success(f"Translated '{text_to_translate}' to {lang_code}: [SIMULATED TRANSLATION]")
        else:
            st.warning("Enter text first")

# ===============================
# FEATURE 8: VOLUNTEER REGISTRATION
# ===============================
if volunteer_reg:
    st.header("🤝 Volunteer Registration")
    vol_name = st.text_input("Volunteer Name")
    vol_city = st.text_input("City")
    vol_skill = st.text_input("Skill")
    if st.button("Register Volunteer"):
        if vol_name != "" and vol_city != "" and vol_skill != "":
            st.success(f"Volunteer {vol_name} registered from {vol_city} with skill {vol_skill}")
        else:
            st.warning("Fill all fields")

# ===============================
# FEATURE 9: FEEDBACK
# ===============================
if feedback_btn:
    st.header("📝 Feedback / Suggestions")
    feedback = st.text_area("Write your feedback here:")
    if st.button("Submit Feedback"):
        if feedback != "":
            st.success("Thank you for your feedback!")
        else:
            st.warning("Enter feedback first")

# ===============================
# FEATURE 10: FAQ / MIGRANT TIPS
# ===============================
if faq_btn:
    st.header("❓ FAQ / Migrant Tips")
    st.markdown("""
- How to find jobs quickly? → Check job listings and AI suggestions daily  
- How to find shelters? → Use the shelter locator map  
- How to get free food? → Check the food assistance map and NGOs  
- Emergency number? → Use SOS or call local helplines  
- Language barrier? → Use the translation feature  
- Travel safely? → Follow safety tips and travel in groups
""")

# ===============================
# FEATURE 11: SAFETY TIPS
# ===============================
st.subheader("🛡️ Safety Tips")
st.markdown("""
1. Keep ID & documents safe  
2. Travel in groups  
3. Avoid unsafe areas at night  
4. Use official shelters & NGOs  
5. Report harassment
""")

# ===============================
# FEATURE 12: DAILY MOTIVATION
# ===============================
st.subheader("💡 Daily Motivation Quote")
quotes = [
    "Keep going, you are stronger than you think.",
    "Every step you take brings you closer to your goal.",
    "Help others and the world will help you back.",
    "Stay positive, even during challenges.",
    "Your effort today will make your tomorrow better."
]
st.info(choice(quotes))

# ===============================
# FEATURE 13: EMERGENCY CONTACTS
# ===============================
st.subheader("📞 Emergency Contacts")
st.markdown("""
- Police: 100  
- Ambulance: 108  
- Fire: 101  
- Child Helpline: 1098
""")

# ===============================
# FEATURE 14: RESOURCE LINKS
# ===============================
st.subheader("📌 Quick Resource Links")
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Government Schemes"):
        webbrowser.open("https://www.ncs.gov.in/")
with col2:
    if st.button("Legal Aid"):
        webbrowser.open("https://legalaid.gov.in/")
with col3:
    if st.button("NGO Directory"):
        webbrowser.open("https://www.indiango.in/")

# ===============================
# FEATURE 15: WEATHER (SIMULATED)
# ===============================
st.subheader("☀️ Weather Info (Simulated)")
city_name = st.text_input("Enter city for weather info")
if st.button("Check Weather"):
    if city_name != "":
        temp = choice(range(25, 40))
        weather_desc = choice(["Sunny", "Cloudy", "Rainy", "Windy"])
        st.success(f"Weather in {city_name}: {temp}°C, {weather_desc}")
    else:
        st.warning("Enter city name first")

# ===============================
# FEATURE 16: DATE & TIME
# ===============================
st.sidebar.subheader("📅 Current Date & Time")
st.sidebar.write(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# ===============================
# FEATURE 17: DAILY HOROSCOPE (FUN)
# ===============================
st.subheader("🔮 Daily Horoscope (Fun)")
signs = ["Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn","Aquarius","Pisces"]
if st.button("Get Your Daily Horoscope"):
    st.info(f"{choice(signs)}: Today is a good day to stay positive and work hard. Opportunities may come unexpectedly!")

# ===============================
# FEATURE 18: SKILL TRAINING LINKS
# ===============================
st.subheader("🎓 Skill Training Resources")
st.markdown("""
- [NPTEL Courses](https://onlinecourses.nptel.ac.in/)  
- [Coursera Free Courses](https://www.coursera.org/)  
- [Skill India](https://www.skillindia.gov.in/)
""")

# ===============================
# FEATURE 19: DONATION LINKS
# ===============================
st.subheader("💖 Donate to NGOs")
st.markdown("""
- [Goonj](https://goonj.org/)  
- [CRY](https://www.cry.org/)  
- [Smile Foundation](https://www.smilefoundationindia.org/)
""")

# ===============================
# FEATURE 20: RESOURCE MAP IMAGE (SIMULATED)
# ===============================
st.subheader("🗺️ Resource Map (Simulated)")
st.image("https://i.imgur.com/ZQZ1Z5b.png", caption="Sample resource map for migrants")

st.success("✅ Migrant Help App Loaded Successfully! All features are fully interactive.")