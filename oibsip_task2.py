
# name := zeel shah
# task := BMI calculator


import streamlit as st # for using streamlit webapplication

st.header(":blue[BMI Calculator]")
# taking user input of height and weight with it's coresponding measure options
weight_option=st.selectbox(":blue[weight options : ]",options=['kilograms','pounds'])
weight_value=st.number_input(":blue[Enter Weight : ]")
height_option=st.selectbox(":blue[Height options : ]",options=['centimeters','feet','meter'])
height_value=st.number_input(":blue[Enter Height : ]    ")
# button of calculate on click of calculate bmi will be calculate with coresponding user input
calculate = st.button("calculate")
if calculate:
    # try block to handle 0 division exception
    try:
        # as we are calculating bmi while taking kg as consedration it converts pounds to kgs
        if weight_option=="pounds":
            weight_value=weight_value*0.453592
        # we are calculating bmi while  considering cm thus if user selects feet or meter it converts them to cm
        if height_option=="feet":
            height_value=height_value*30.48
        if height_option=="meter":
            height_value=height_value*100
        # calculating bmi values corespond to user input
        bmi_value=weight_value/((height_value/100)**2)
        st.write("You're BMI value is ",bmi_value)
        # if it's less then 18.5 then it's underweight , if it's in range of 18.5 to 25 then it's normal
        # or grater then 25 then it's overweight so print the corspond outcome of it
        if(bmi_value<18.5):
           st.subheader(":blue[You are underweight]")
        elif(bmi_value<25.0):
            st.subheader(":green[You're weight is Normal]")
        elif(bmi_value>25):
            st.subheader(":red[you are overweight]")
       
        st.subheader("* Information *")
       
        st.write(":blue[less then 18.4 :- underweight]   ",":green[  18.5 to 25.0 :- normal]  ",":red[ grater then 25.0 :- overweight]")
    # if valueerror or zivison zero error ocuurs then it will be handled by these code   
    except ValueError:
        st.write('Error','Enter a valid number !')
    except ZeroDivisionError:
        st.write('Error','Height cannot be 0 !')
        
