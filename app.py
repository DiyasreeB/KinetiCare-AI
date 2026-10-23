
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="KinetiCare AI",
    page_icon="💪",
    layout="wide"
)

if "status" not in st.session_state:
    st.session_state.status = "Ready"
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0
if "last_result" not in st.session_state:
    st.session_state.last_result = None

st.title("KinetiCare AI")
st.subheader("Rehabilitation & Physical Therapy Assistant")

st.warning(
    "SIMULATION ONLY — This prototype uses synthetic movement signals. "
    "It is not a medical device and is not clinically validated."
)

st.sidebar.header("Session Settings")
exercise = st.sidebar.selectbox(
    "Select exercise",
    ["Arm Raise", "Knee Extension", "Shoulder Movement"]
)
duration = st.sidebar.slider("Session duration (seconds)", 10, 60, 30)
quality = st.sidebar.selectbox(
    "Signal scenario", ["Normal", "Noisy", "Low Range"]
)

st.subheader("Session Controls")
st.write(f"**Session status:** {st.session_state.status}")

c1, c2, c3, c4 = st.columns(4)

if c1.button("Start Session", use_container_width=True):
    st.session_state.status = "Running"
    st.session_state.elapsed = duration
    st.session_state.last_result = None
    st.rerun()

if c2.button("Pause Session", use_container_width=True):
    if st.session_state.status == "Running":
        st.session_state.status = "Paused"
    st.rerun()

if c3.button("Resume Session", use_container_width=True):
    if st.session_state.status == "Paused":
        st.session_state.status = "Running"
    st.rerun()

if c4.button("Stop Session", use_container_width=True):
    st.session_state.status = "Stopped"
    st.session_state.last_result = None
    st.rerun()

if st.session_state.status == "Running":
    st.info(
        "The simulated session is marked Running. "
        "This prototype does not collect live sensor data."
    )
    if st.button("Complete Demo Session"):
        st.session_state.status = "Completed"
        st.rerun()

if st.session_state.status == "Paused":
    st.warning("Session paused. Resume or stop the demo session.")

if st.session_state.status == "Stopped":
    st.info("Session stopped. Press Start Session to begin another demo.")

if st.session_state.status == "Completed":
    np.random.seed(42)

    time = np.arange(0, duration, 0.1)
    amplitude = 25 if quality != "Low Range" else 8
    noise = 0.8 if quality == "Normal" else 4.0

    movement = (
        45 + amplitude * np.sin(2 * np.pi * time / 3)
        + np.random.normal(0, noise, len(time))
    )

    data = pd.DataFrame({
        "Time (seconds)": time,
        "Simulated Angle (degrees)": movement
    })

    threshold = 45 + amplitude * 0.5
    peaks = []
    min_gap = 20

    for i in range(1, len(movement) - 1):
        is_peak = (
            movement[i] > movement[i - 1]
            and movement[i] >= movement[i + 1]
            and movement[i] > threshold
        )
        if is_peak and (not peaks or i - peaks[-1] >= min_gap):
            peaks.append(i)

    reps = len(peaks)
    rom = float(np.max(movement) - np.min(movement))
    tempo = duration / reps if reps else 0

    if len(peaks) >= 3:
        intervals = np.diff(np.array(peaks)) * 0.1
        mean_interval = float(np.mean(intervals))
        std_interval = float(np.std(intervals))
        consistency = max(
            0.0, 100 * (1 - std_interval / mean_interval)
        ) if mean_interval else 0.0
    else:
        consistency = 0.0

    st.success("Demo session completed.")
    a, b, c, d = st.columns(4)
    a.metric("Estimated Repetitions", reps)
    b.metric("Simulated Range", f"{rom:.1f}°")
    c.metric("Seconds per Rep", f"{tempo:.2f}" if reps else "N/A")
    d.metric("Consistency Estimate", f"{consistency:.1f}%")

    fig = px.line(
        data,
        x="Time (seconds)",
        y="Simulated Angle (degrees)",
        title="Simulated Movement Signal"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.write(f"**Exercise:** {exercise}")
    st.write(f"**Scenario:** {quality}")
    st.info(
        "These metrics are calculated from synthetic data using a simple "
        "prototype algorithm. They are not clinical measurements."
    )

    st.download_button(
        "Download Session Data (CSV)",
        data.to_csv(index=False),
        file_name="kineticare_session.csv",
        mime="text/csv"
    )

st.caption(
    "KinetiCare AI | Synthetic data only | Not for diagnosis or treatment decisions"
)
