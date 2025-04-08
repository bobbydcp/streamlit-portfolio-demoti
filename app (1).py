#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# ========== CONFIG ==========
st.set_page_config(page_title="Your Name | Portfolio", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Skills", "Courses", "Projects", "Resume", "Contact"])

# ========== ABOUT ==========
if page == "About Me":
    st.title("👋 Hi, I'm Demoti Ravi Chandra")
    st.subheader("Data Analyst | ML Enthusiast | Streamlit Developer")
    st.write("""
    I’m passionate about building intuitive data tools and solving real-world problems with analytics and machine learning.
    I have hands-on experience with Python, Streamlit, Power BI, and more.
    """)

# ========== SKILLS ==========
elif page == "Skills":
    st.title("🛠️ Skills")
    st.markdown("""
    - **Languages:** Python, SQL
    - **Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn, OpenCV
    - **Tools:** Streamlit, Power BI, Excel, Git, VS Code
    - **Other:** Machine Learning, Data Visualization, Web Apps
    """)

# ========== COURSES ==========
elif page == "Courses":
    st.title("📚 Courses")
    st.write("Here are some of the relevant courses I’ve completed:")
    st.markdown("""
    - Machine Learning - Coursera (Andrew Ng)
    - Applied Data Science with Python - University of Michigan
    - Deep Learning Specialization - Coursera
    - Streamlit Crash Course – YouTube
    """)

# ========== PROJECTS ==========
elif page == "Projects":
    st.title("🚀 Projects")
    projects = [
        {
            "title": "Object Detection App",
            "description": "Real-time object detection using YOLOv5 and Streamlit UI.",
            "tech": "Python, OpenCV, YOLOv5, Streamlit",
            "link": "https://github.com/yourusername/object-detection-app"
        },
        {
            "title": "Excel Data Cleaner",
            "description": "Automated Excel file cleaning using pandas and UI via Streamlit.",
            "tech": "Python, Pandas, Streamlit",
            "link": "https://github.com/yourusername/excel-data-cleaner"
        }
    ]
    for project in projects:
        st.subheader(project["title"])
        st.write(project["description"])
        st.write(f"**Tech Used:** {project['tech']}")
        st.markdown(f"[🔗 GitHub Link]({project['link']})")
        st.markdown("---")

# ========== RESUME ==========
elif page == "Resume":
    st.title("📄 Resume")
    st.write("Click below to download my resume.")
    with open("Your_Resume.pdf", "rb") as f:
        st.download_button("Download Resume", f, file_name="Your_Resume.pdf")

# ========== CONTACT ==========
elif page == "Contact":
    st.title("📬 Contact")
    st.markdown("""
    - 📧 Email: ravichandra.dcp@gmail.com  
    - 🔗 [LinkedIn](https://linkedin.com/in/yourprofile)  
    - 💻 [GitHub](https://github.com/bobbydcp)
    """)


# In[ ]:




