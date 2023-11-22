import streamlit as st 

st.title('ตรวจสอบคุณสมบัติการขอสินเชื่อบ้าน')
st.header('นางสาวชุติมา สุขสมัย')
st.subheader('สาขาวิทยาการข้อมูล')
st.markdown("----")

#col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
#with col1:
    #st.image('./pic/k1.jpg')
#with col2:
    #st.image('./pic/iris.jpg')
    

html_1="""
<div style="background-color:#63D767;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลการขอสินเชื่อบ้าน</h5></center>
</div>
"""    
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd
import numpy as np

dt=pd.read_csv('./data/Root1.csv')
st.write(dt.head(10))

dt1 = dt['Gender'].sum()
dt2 = dt['Married'].sum()
dt3 = dt['Dependents'].sum()
dt4 = dt['Education'].sum()
dt5 = dt['Self_Employed'].sum()
dt6 = dt['ApplicantIncome'].sum()
dt7 = dt['CoapplicantIncome'].sum()
dt8 = dt['LoanAmount'].sum()
dt9 = dt['Loan_Amount_Term'].sum()
dt10 = dt['Credit_History'].sum()

dx = [dt1, dt2, dt3, dt4, dt5, dt6, dt7, dt8, dt9, dt10]
dx2 = pd.DataFrame(dx, index=["dt1", "dt2", "dt3", "dt4", "dt5", "dt6", "dt7", "dt8", "dt9", "dt10"])

if st.button("show bar chart"):
   st.bar_chart(dx2)
   st.button("Not show bar chart")
else :
   st.button("Not show bar chart")
   
   
html_2 = """
<div style="background-color:#6CE9E8;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายการขอสินเชื่อบ้าน</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

Gender = st.number_input("กรุณากรอกข้อมูล เพศ/Gender โดยที่ 0 คือเพศชาย 1 คือเพศหญิง")
Married = st.number_input("กรุณากรอกข้อมูล แต่งงาน/Married โดยที่ 0 คือไม่ได้แต่งงาน 1 คือแต่งงาน")
Dependents = st.number_input("กรุณากรอกข้อมูล จำนวนอุปการะ/Dependents")
Education = st.number_input("กรุณากรอกข้อมูล การสำเร็จการศึกษา/Education โดยที่ 0 คือ ไม่ 1 คือ ใช่")
Self_Employed = st.number_input("กรุณากรอกข้อมูล อาชีพอิสระ/Self_Employed โดยที่ 0 คือ ไม่มี 1 คือ มี")
ApplicantIncome = st.number_input("กรุณากรอกข้อมูล รายได้ของผู้สมัคร/ApplicantIncome(หน่วยเป็นพัน)")
CoapplicantIncome = st.number_input("กรุณากรอกข้อมูล รายได้ของผู้สมัคร/CoapplicantIncome(หน่วยเป็นพัน)")
LoanAmount = st.number_input("กรุณากรอกข้อมูล วงเงินกู้/LoanAmount")
Loan_Amount_Term = st.number_input("กรุณากรอกข้อมูล ระยะเวลากู้/Loan_Amount_Term หน่วยเป็นเดือน")

import numpy as np

Gender=np.sqrt(Gender)
Married=np.sqrt(Married)
Dependents=np.sqrt(Dependents)
Education=np.sqrt(Education)
Self_Employed=np.sqrt(Self_Employed)
ApplicantIncome=np.sqrt(ApplicantIncome)
CoapplicantIncome=np.sqrt(CoapplicantIncome)
LoanAmount=np.sqrt(LoanAmount)
Loan_Amount_Term=np.sqrt(Loan_Amount_Term)

from sklearn.neighbors import KNeighborsClassifier

if st.button("ทำนายผล"):
    #ทำนาย
    dt = pd.read_csv("./data/Root1.csv") 
    X = dt.drop('Credit_History', axis=1)
    y = dt.Credit_History 
    st.button("ไม่ทำนายผล")

    Knn_model = KNeighborsClassifier(n_neighbors=3)
    Knn_model.fit(X, y)

#ข้อมูลสำหรับทดลองจำแนกข้อมูล
    x_input = np.array([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term]])

#เอา input ไปทดสอบ
    st.write(Knn_model.predict(x_input))
    out=Knn_model.predict(x_input)

    if out[0]=="0":    
        #st.image("./pic/iris1.jpg")
        st.header("No")
    elif out[0]=="1":
        #st.image("./pic/iris2.jpg")
        st.header("Yes")
    else:
        #st.image("./pic/iris3.jpg") 
        st.header("Yes") 
    st.button("ไม่ทำนาย")
else:
    st.button("ไม่ทำนาย")
    