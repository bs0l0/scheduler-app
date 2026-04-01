import streamlit as st
import pandas as pd

st.set_page_config(page_title="Weekly Task Scheduler", layout="wide")
st.title("🗓️ Weekly Task Scheduler")


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times = [f"{h:02d}:00" for h in range(6, 24)] 

if 'tasks' not in st.session_state:

    st.session_state.tasks = pd.DataFrame("", index=times, columns=days)

st.sidebar.header("Add New Task")
with st.sidebar.form("task_form"):
    task_name = st.text_input("Task Description")
    selected_day = st.selectbox("Day", days)
    selected_time = st.selectbox("Time Slot", times)
    submit = st.form_submit_button("Add to Schedule")

    if submit and task_name:
        st.session_state.tasks.at[selected_time, selected_day] = task_name
        st.success(f"Added: {task_name}")

col1, col2 = st.columns([4, 1])

with col1:
    st.subheader("Your Weekly View")

    edited_df = st.data_editor(
        st.session_state.tasks,
        use_container_width=True,
        height=600
    )

    st.session_state.tasks = edited_df

with col2:
    st.subheader("Controls")
    if st.button("Clear All Tasks"):
        st.session_state.tasks = pd.DataFrame("", index=times, columns=days)
        st.rerun()
    
    st.download_button(
        label="Export to CSV",
        data=st.session_state.tasks.to_csv(),
        file_name="weekly_schedule.csv",
        mime="text/csv",
    )


st.info("💡 Pro-tip: You can double-click any cell in the table to edit or delete tasks manually.")