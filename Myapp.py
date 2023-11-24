import streamlit as st

st.title('ตรวจสอบคุณสมบัติการขอสินเชื่อบ้าน')
st.header('นางสาวชุติมา สุขสมัย')
st.subheader('สาขาวิชาวิทยากรข้อมูล')
st.markdown('---')

col1, col2 =st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('pic/002.jpg')
with col2:
    st.image('pic/Home1.jpg')


html_1="""
<div style="background-color:#73C6B6 ;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลการขอสินเชื่อบ้าน</h5></center>
</div>
"""
st.markdown(html_1,unsafe_allow_html=True)
st.markdown("")

import pandas as pd

dt=pd.read_csv('data/Root1.2.csv')
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

dx = [dt1, dt2, dt3, dt4,dt5,dt6,dt7,dt8,dt9,dt10]
dx2 = pd.DataFrame(dx, index=["dt1", "dt2", "dt3", "dt4", "dt5", "dt6", "dt7", "dt8", "dt9", "dt10"])

if st.button("show bar chart"):
    st.bar_chart(dx2)
    st.button("not show bar chart")
else :
     st.button("not show bar chart")

html_2 = """
<div style="background-color:#FFBF00;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายการขอสินเชื่อบ้าน</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

import numpy as np
import pandas as pd

Gender = st.number_input("กรุณากรอกข้อมูล เพศ/Gender โดยที่ 0 คือเพศชาย 1 คือเพศหญิง")
Married = st.number_input("กรุณากรอกข้อมูล แต่งงาน/Married โดยที่ 0 คือไม่ได้แต่งงาน 1 คือแต่งงาน")
Dependents = st.number_input("กรุณากรอกข้อมูล จำนวนอุปการะ/Dependents")
Education = st.number_input("กรุณากรอกข้อมูล การสำเร็จการศึกษา/Education โดยที่ 0 คือ ไม่ 1 คือ ใช่")
Self_Employed = st.number_input("กรุณากรอกข้อมูล อาชีพอิสระ/Self_Employed โดยที่ 0 คือ ไม่มี 1 คือ มี")
ApplicantIncome = st.number_input("กรุณากรอกข้อมูล รายได้ของผู้สมัคร/ApplicantIncome(หน่วยเป็นพัน)")
CoapplicantIncome = st.number_input("กรุณากรอกข้อมูล รายได้ของผู้สมัคร/CoapplicantIncome(หน่วยเป็นพัน)")
LoanAmount = st.number_input("กรุณากรอกข้อมูล วงเงินกู้/LoanAmount")
Loan_Amount_Term = st.number_input("กรุณากรอกข้อมูล ระยะเวลากู้/Loan_Amount_Term หน่วยเป็นเดือน")

rGender=np.sqrt(Gender)
rMarried=np.sqrt(Married)
rDependents=np.sqrt(Dependents)
rEducation=np.sqrt(Education)
rSelf_Employed=np.sqrt(Self_Employed)
rApplicantIncome=np.sqrt(ApplicantIncome)
rCoapplicantIncome=np.sqrt(CoapplicantIncome)
rLoanAmount=np.sqrt(LoanAmount)
rLoan_Amount_Term=np.sqrt(Loan_Amount_Term)

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

if st.button("ทำนายผล"):
    #ทำนาย

   X = dt.drop('Credit_History', axis=1) #เลือกคอลัมที่เอามาทำงาน
   y = dt.Credit_History   #คอลัมคำตอบ
 
 #  st.write(X.head(3))
 #  st.write(X.shape)
 
   Knn_model = KNeighborsClassifier(n_neighbors=7)
   Knn_model.fit(X,y)
#ข้อมูลสำหรับการจำแนกข้อมูล

   x_input = np.array([[rGender,rMarried,rDependents,rEducation,rSelf_Employed,rApplicantIncome,rCoapplicantIncome,rLoanAmount,rLoan_Amount_Term]])
        #เอา input ไปทดสอบ
   #st.write(x_input)
   #st.write(Knn_model.predict(x_input))
   out=Knn_model.predict(x_input)  #ผลลัพธ์

   if out[0]=="1":
      st.image("pic/Y.jpg")  
      st.header("Yes")
   elif out[0]=="0":
      st.image('pic/N.jpg')
      st.header("No")
   else:
      st.image("./pic/N.jpg") 
      st.header("No") 
   st.button("ไม่ทำนาย")

else:
   st.button("ไม่ทำนาย")