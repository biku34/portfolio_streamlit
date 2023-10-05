import streamlit as st
nav=st.sidebar.radio("Portfolio",['Home','About','Education','Work','Contact'])
if nav == 'Home':
    st.markdown("# Bikram Sadhukhan")
    st.subheader("BTech-MTech Cybersecurity")
    st.write("Java|SQL|C++|C|Digital Forensic Tools|CTF Player")
    st.divider()
if nav == 'About':
    st.header("About Me : ")
    st.divider()
    st.text("I am currently pursuing a BTech-MTech Dual Degree in Cybersecurity at the National \nForensic Sciences University. As a student of cybersecurity, I possess a fundamental \nknowledge of digital forensic terminologies and have a deep interest in pursuing\na career in this field\nI want to pursue my career so that I could give back to the society and to the mass.\nMy aim is to utilize my skills and knowledge to serve society and contribute towards \ncreating a safer digital space for all. I am passionate about exploring the latest \ndevelopments in the cybersecurity world and enjoy analyzing real-world problems to \narrive at effective solutions. I am keen on exploring diverse career opportunities \nand enhancing my skill set further.")
if nav == 'Contact':
    st.header("Get in touch : ")
    st.divider()
    icl,lin = st.columns([2,40])
    with icl:
        st.image("linkedin.png")
    with lin:
        st.write("https://www.linkedin.com/in/bikram-sadhukhan-8a78ab22a/")
    icm,mai = st.columns([2,40])
    with icm:
        st.image("gmail.png")
    with mai:
        st.write("bikramsadhukhan505@gmail.com")
if nav == 'Education' :
    st.markdown("# Education")
    st.divider()
    st.subheader("National Forensic Sciences University , Gandhinagar")
    st.write("BTech-MTech CSE with specialization in \nCybersecurity and Digital Forensics")
    st.write("2022-2027")
    st.subheader("Convent of Jesus and Mary , Ranaghat")
    st.write("Higher Secondary (PCM)")
    st.write("2020-2022")
    st.subheader("Convent of Jesus and Mary , Ranaghat")
    st.write("Senior Secondary")
    st.write("2012-2020")
if nav == 'Work':
    st.header("Work Experience : ")
    st.divider()
    st.header("No Work Experience Yet : )")
