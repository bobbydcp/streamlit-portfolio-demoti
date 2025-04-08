#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# ========== CONFIG ==========
st.set_page_config(page_title="Demoti Ravi Chandra | Portfolio", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Me", "Skills", "Courses", "Projects", "Resume", "Contact"])


# ========== ABOUT ==========
if page == "About Me":
    st.title("👋 Hello, I'm Demoti Ravi Chandra")
    st.subheader("🔹 Data & Analytics Professional | Streamlit Developer | ML Enthusiast")

    st.write("""
    I'm a results-driven professional with experience in building analytical solutions and automation tools 
    for solving real-world business problems. My expertise lies in data analytics, machine learning, and 
    low-code platforms like Streamlit — enabling rapid development of impactful dashboards and applications.
    
    I currently work in **Ethics & Compliance Systems & Analytics**, where I focus on integrating machine learning, 
    Power BI, Excel reporting, and incident management systems into a centralized platform.

    I'm passionate about transforming messy data into meaningful insights, and I thrive in cross-functional 
    environments where technology meets strategy.
    """)

    st.markdown("### 🔍 Key Highlights")
    st.markdown("""
    - 📊 Experience with Streamlit, Python, Pandas, Power BI, Excel Automation  
    - 🤖 Built and deployed ML models for object detection and data classification  
    - 🛠️ Created centralized portals for reporting, approvals, and data tracking  
    - 📈 Strong understanding of analytics lifecycle from intake to action  
    """)

    st.markdown("### 📫 Let’s Connect")
    st.markdown("""
    - [LinkedIn](https://linkedin.com/in/your-profile)  
    - [GitHub](https://github.com/yourusername)  
    - 📧 your.email@example.com
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
    - 📧 Email: your.email@example.com  
    - 🔗 [LinkedIn](https://linkedin.com/in/ravi-c-6035bb168)  
    - 💻 [GitHub](https://github.com/bobbydcp)
    """)


# In[ ]:




