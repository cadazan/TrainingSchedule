# TrainingSchedule
Training Schedule Calculator
This Python code uses the Streamlit library to create a web app that calculates a training day schedule based on user inputs.

The app prompts the user to enter the following inputs:

- Break length (in minutes)
- Lunch duration (in minutes)
- Start time
- Lunch time
- Finish time

The `calculate_breaks` function uses these inputs to determine the start time and duration of each session and break throughout the day. It returns six variables that correspond to the start times of the first break, second break, third break, and fourth break, the start time of the afternoon session, and the duration of the morning and afternoon sessions.

The `if st.button('Calculate'):` block calls the `calculate_breaks` function with the user inputs and generates a Pandas dataframe to display the schedule in a table. The dataframe includes the session name, start time, end time, and length.

The app displays the table when the user clicks the "Calculate" button.

Note that this app assumes that the training day occurs on the current date, which may not be accurate for all use cases.
