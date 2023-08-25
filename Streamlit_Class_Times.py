import streamlit as st
import datetime
import pandas as pd

# Helper function
def calculate_breaks(start_time, lunch_time, finish_time, break_length, lunch_duration):

  start_dt = datetime.datetime.combine(datetime.date.today(), start_time)
  lunch_dt = datetime.datetime.combine(datetime.date.today(), lunch_time)
  finish_dt = datetime.datetime.combine(datetime.date.today(), finish_time)

  morning_total_time = lunch_dt - start_dt
  morning_session_time = (morning_total_time / 2) - datetime.timedelta(minutes=break_length / 2)

  afternoon_start = lunch_dt + datetime.timedelta(minutes=lunch_duration)
  afternoon_total_time = finish_dt - afternoon_start
  afternoon_session_time = (afternoon_total_time / 2) - datetime.timedelta(minutes=break_length / 2)

  first_break = start_dt + morning_session_time
  second_break = lunch_dt - morning_session_time
  third_break = afternoon_start + afternoon_session_time
  fourth_break = finish_dt - afternoon_session_time

  return (
    first_break.strftime("%H:%M"),
    second_break.strftime("%H:%M"),
    third_break.strftime("%H:%M"),
    fourth_break.strftime("%H:%M"),
    afternoon_start.strftime("%H:%M"),
    str(morning_session_time),
    str(afternoon_session_time)
  )

# Streamlit app
st.title('Training Day Schedule')

# Inputs
break_length = st.number_input('Break Length (in minutes)', value=20)
lunch_duration = st.number_input('Lunch Duration (in minutes)', value=60)

start_time = st.time_input('Enter start time', datetime.time(9, 30))
lunch_time = st.time_input('Enter lunch time', datetime.time(12, 30))
finish_time = st.time_input('Enter finish time', datetime.time(16, 30))

if st.button('Calculate'):

  breaks = calculate_breaks(start_time, lunch_time, finish_time,
                            break_length, lunch_duration)

  # Create a dataframe for the output
  df = pd.DataFrame({
        'Session': ['Morning Session', 'Second Session', 'Lunch Break', 'Third Session', 'Fourth Session'],
        'Start Time': [start_time.strftime('%H:%M'), breaks[1], lunch_time.strftime('%H:%M'), breaks[2], breaks[3]],
        'End Time': [breaks[0], lunch_time.strftime('%H:%M'), breaks[4], breaks[3], finish_time.strftime('%H:%M')],
        'Length': [breaks[5], breaks[5], str(lunch_duration) + ' mins', breaks[6], breaks[6]]
    })

  # Print output as a table
  st.table(df)
