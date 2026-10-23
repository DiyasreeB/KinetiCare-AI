

\# KinetiCare AI



\## Project Overview

KinetiCare AI is a prototype designed to demonstrate basic movement analysis for rehabilitation and physical therapy support. It uses simulated movement signals to estimate repetitions, range of motion, tempo, and consistency.



\## Features

\- Select an exercise type.

\- Choose a simulated signal scenario: Normal, Noisy, or Low Range.

\- Start, pause, resume, stop, and complete a demo session.

\- View movement metrics and a signal plot.

\- Download session results as a CSV file.

\- Run basic automated tests using synthetic data.



\## Technologies Used

\- Python

\- Streamlit

\- NumPy

\- Pandas

\- Plotly



\## Setup Instructions

1\. Install Python 3.13 or another compatible Python version.

2\. Open Command Prompt in the project folder.

3\. Install the required packages:



&#x20;  `python -m pip install -r requirements.txt`



\## Run the Application

Run this command from the project folder:



`python -m streamlit run app.py`



Streamlit will provide a local address to open the application in your browser.



\## Run Tests

Run:



`python test\_kineticare.py`



The current basic test suite contains five tests for normal, noisy, paused, incomplete, and low-range synthetic signals. All five passed in the recorded test run. These tests do not establish clinical accuracy or validate the complete application.



\## Limitations and Safety

\- Movement data is simulated; no real wearable sensor or Bluetooth connection is implemented.

\- The prototype has not been clinically validated.

\- It is not a medical device and must not be used for diagnosis or treatment decisions.

\- Results are demonstrations of basic signal-processing logic, not medical advice.

\- Real-world testing, accessibility review, privacy assessment, and expert evaluation are future work.



