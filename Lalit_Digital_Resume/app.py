from pathlib import Path
import pandas as pd
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV100.pdf"
profile_pic = current_dir / "assets" / "Lalit.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "My Digital CV | Lalit Kumar"
PAGE_ICON = ":wave:"
NAME = "Lalit Kumar"
DESCRIPTION = """
Assistant Professor (Physics), G. B. Pant Memorial Govt. College Rampur Bushahr,
Shimla 172001 INDIA
Currently Pursuing Ph.D from Central University of Himachla Pradesh,
Dharamshala (Accredited with 'A+' grade by NAAC)
"""
EMAIL = "lalitbijj409@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCHgSX5FQgmn63ggJjH4pdcg",
    "GitHub": "https://github.com/Anynomous123",
    "Google Scholar": "https://scholar.google.com/citations?user=ql1NfzwAAAAJ&hl=en",
    "ORCID": "https://orcid.org/0000-0002-9369-1124",
    "ResearchGate":"https://www.researchgate.net/profile/Lalit-Kumar-81",
}
PROJECTS = {
    "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
    "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
    "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
   }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Educational Qualifications")
data = {
#        "Sr. No.":	[1,	2	,3,	4,	5	,6],
    "Year":[2020	,2019,	2019,	2017,	2014,	2012],
    "Name of Institute": ["IIT Delhi",	"Himachal Pradesh Public Service Commission",	"Central University of Himachal Pradesh",	"Govt. College Banjar (HPU Shimla)","	Govt. Sr. Sec. School Banjar (HPBOSE Dharamshala)","	Govt. Sr. Sec. School Jibhi (HPBOSE Dharamshala)"],
    "Examination Passed":	["GATE",	"SET",	"PG",	"UG"	,"12th"	,"10th"],
    "Percentage":["","" ,	"78.00%",	"81.00%",	"82.00%",	"86.00%"],
}

df = pd.DataFrame(data)
df = df.set_index([pd.Index(['1', '2', '3', '4','5','6'])])
st.write(df)
#st.table(df)

st.write('\n')
st.subheader("Research Experience")
st.write("")
st.write(
"""
📑 Authored 10 publications in reputable international journals.

📑 Two papers were authored and published at the 66th National DAE Symposium on Nuclear Physics.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Interests")
st.write("")
st.write(
    """
📖 Engaging in Book Reading

💻 Basic physics problems are tackled using programming in Scilab, Python, and Fortran

"""
)

# --- JOB 2
st.write('\n')
st.subheader("Skills")
st.write("")
st.write(
    """
- 👩‍💻 Programming: Python, Scilab, Fortran.
- 📊 Data Visulization: Gnumeric, Libre Office Calc, Gnuplot, Xmgrace.
- 📚 Modeling: Numerical Methods in Computational Physics.
"""
)

# --- JOB 3
st.write('\n')
st.subheader("Research Publications in International Journals")
data = {
"Title":	["Deuteron structure and form factors: Using an inverse potential approach", 
"Alpha–Alpha Scattering Potentials for Various-Channels Using Phase Function Method",
"An Innovative Approach to Construct Inverse Potentials Using Variational Monte-Carlo and Phase Function Method: Application to np and pp Scattering	",
"Neutron-Proton Scattering Phase Shifts in S-Channel using Phase Function Method for Various Two Term Potentials",
"Deuteron Structure and Form Factors: Using Inverse Potentials for S-waves",
"Phase Shift Analysis for Alpha-alpha Elastic Scattering using Phase Function Method for Gaussian Local Potential",
"Phase Shift Analysis of Light Nucleon-Nucleus Elastic Scattering using Reference Potential",
"Approach	Phase Shift Analysis for Neutron-Alpha Elastic Scattering Using Phase Function Method with Local Gaussian Potential",
"Recalculated Viola-Seaborg Coefficients for Partial Alpha Half-lives Based on AME2016",
"3He-α Elastic Scattering Phase Shifts in Various Channels Using Phase Function Method with Morse Potential",
"Triton scattering phase-shifts for S-wave using Morse potential",
"Neutron-Proton Interaction Modeled using Morse Function: Constructing Inverse Potentials Using Variational Monte-Carlo and Phase Function Method",
"Simulation of vibrational spectrum of diatomic molecules using Morse potential by matrix methods in gnumeric worksheet"],
"Authors":	["Khachi, Anil, Lalit Kumar, MR Ganesh Kumar, and O. S. K. S. Sastri.",
"	Khachi, Anil; Kumar, Lalit; Sastri, OSKS;",
"	Sastri, OSKS; Khachi, Anil; Kumar, Lalit;",
"	Khachi, Anil; Kumar, Lalit; Sastri, OSKS;",
"	Khachi, Anil; Kumar, Lalit; Kumar, MR; Sastri, OSK;",
"	Khachi, Anil; Sastri, OSKS; Kumar, Lalit; Sharma, Aditi;	",
"Kumar, Lalit; Awasthi, Shikha; Khachi, Anil; Sastri, OSK;",
"	Kumar, Lalit; Khachi, Anil; Sastri, OSKS;",
"	Kumar, Lalit; Gora, Swapna; Rana, Vikram; Khachi, Anil; Sastri, OSKS;",
"	Khachi, Anil; Sastri, OSKS; Kumar, Lalit;",
"	Khachi, Anil; Awasthi, Shikha; Sastri, OSKS; Kumar, Lalit;",
"	Khachi, Anil; Kumar, Lalit; Sastri, OSKS;",
"	Sastri, OSKS; Sharma, Aditi; Awasthi, Shikha; Kachi, Anil; Kumar, Lalit;"],
"Publication	":["Physical Review C",	
"Phys. At. Nucl.",
"	Braz. J. Phys.",
"	J. Nucl. Phy. Mat.",
"	arXiv preprint arXiv:2209.03575",
"	J. Nucl. Phy. Mat.",
"	arXiv preprint arXiv:2209.00951",
"	J. Nucl. Phy. Mat.",
"	J. Nucl. Phy. Mat.	",
"J. Nucl. Phy. Mat.",
"	J. Nucl. Phy. Mat.",
"	arXiv preprint arXiv:2104.14788",
"	Phys. Educ."],
"Volume	":[107,	85,	52,	9,"",	9,	2022,	9,	9,	9,	9,	"",	36],
"Number":[	6,	4,	2,	1,	"",	1,"",		2,	1,	2,	1,"",""],		
"Pages":	[64002,	"382-391",	58,	"87-93",	"",	"1-5","",		"215-221",	"37-42",	"161-167",	"81-85",	"",	"1-14"],
"Year":	[2023,	2022,	2022,	2021,	2022,	2021,		2022,	2022,2021,	2022,	2021,	2021,	2019],
"Publisher":	["APS",	"Pleiades Publishing Moscow",	"Springer US New York","","","","","","","","","",""],										
}
df = pd.DataFrame(data)
df = df.set_index([pd.Index(['1', '2','3','4','5','6','7','8','9','10','11','12','13'])])
st.write(df)
#st.table(df)

st.write('\n')
st.subheader("Paper Presented in Conferences/Symposium (National/International)")
st.write("")
data = {
"Title":	["Phase Shift Analysis of α− 12C Elastic Scattering Using Phase Function Method","	P & D Inverse Potentials for Proton-Proton Scattering"],
"Authors":	["Kumar, Lalit; Khachi, Anil; Sharma, Aman; Sastri, OSKS;",	"Kumar, Lalit; Khachi, Anil; Sharma, Arushi; Sastri, OSKS;"],
"Publication":	["Proceedings of the DAE Symp. on Nucl. Phys	","Proceedings of the DAE Symp. on Nucl. Phys"],
"Volume":	[66	,66],
"Pages":	[575,	579],
"Year":	[2022, 2022],
}

df = pd.DataFrame(data)
df = df.set_index([pd.Index(['1', '2'])])
st.write(df)

st.write('\n')
st.subheader("Conferences/colloquia/seminars/schools and workshops attended:")
st.write("")
st.write(
    """
1 Online International Conference on Theoretical Aspects of Nuclear Physics 15 - 20 February, 2021, Organized by Department of Physics and Astronomical Science, Central University ofHimachal Pradesh.

2 Online Faculty Development Programme on Model Based Simulations in Classical Physics Using XCOS 15 - 21 November, 2021 Organized by Department of Physics and Astronomical Sciences Central University of Himachal Pradesh (CUHP) and Indian Association of Physics Teachers(IAPT)

3 Online International Conference on Recent Trends in Nuclear Physics 16 -18 February, 2022, Organized by Department of Physics and Astronomical Science, Central University of Himachal Pradesh.

4 Participated in the “66 th DAE Symposium on Nuclear Physics”, and has made the Poster presentation for the contribution (B116) titled “Phase Shift Analysis of α- 12 C Elastic Scattering Using Phase Function Method” December 1 - 5, 2022 Cotton University, Guwahati, Assam, India.

5 Participated in the “66 th DAE Symposium on Nuclear Physics”, and has made the Poster presentation for the contribution (B118) titled “P&D Inverse Potentials for Proton-Proton Scattering”. December 1 - 5, 2022 Cotton University, Guwahati, Assam, India.

6 Online International Conference on Recent Trends in Nuclear Physics 2 - 4 March, 2023, Organized by Department of Physics and Astronomical Science, Central University of Himachal Pradesh and Indian Association of Physics Teachers (IAPT).

"""
)

st.write('\n')
st.subheader("Awards")
st.write("")
st.write(
"""
🏆 Recipient of the 'Best Oral Presentation Award' at the Online International Conference on Recent Trends in Nuclear Physics, held from 16th to 18th February 2022.
"""
)
# --- Projects & Accomplishments ---
#st.write('\n')
#st.subheader("Projects & Accomplishments")
#st.write("---")
#for project, link in PROJECTS.items():
#    st.write(f"[{project}]({link})")
