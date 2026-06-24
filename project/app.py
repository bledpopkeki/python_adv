import streamlit as st
import requests

API = "http://127.0.0.1:8000"

st.set_page_config(page_title="Workout Tracker", layout="centered")

st.title("🏋️ Workout Tracker")

# ---------------------------
# ADD WORKOUT
# ---------------------------
st.header("Add Workout")

with st.form("add_form"):
    exercise = st.text_input("Exercise")
    duration = st.number_input("Duration (minutes)", min_value=1)
    calories = st.number_input("Calories burned", min_value=0)
    notes = st.text_input("Notes")

    submit = st.form_submit_button("Add Workout")

    if submit:
        data = {
            "exercise": exercise,
            "duration": int(duration),
            "calories": int(calories),
            "notes": notes
        }

        requests.post(f"{API}/workouts", json=data)
        st.success("Workout added!")

# ---------------------------
# LOAD DATA
# ---------------------------
st.header("Your Workouts")

response = requests.get(f"{API}/workouts")
workouts = response.json()

# ---------------------------
# DELETE WORKOUT
# ---------------------------
for w in workouts:
    with st.container():
        st.markdown(f"### {w['exercise']}")
        st.write(f"⏱ Duration: {w['duration']} min")
        st.write(f"🔥 Calories: {w['calories']}")
        st.write(f"📝 Notes: {w['notes']}")

        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"Delete {w['id']}"):
                requests.delete(f"{API}/workouts/{w['id']}")
                st.rerun()

        with col2:
            if st.button(f"Edit {w['id']}"):
                st.session_state["edit_id"] = w["id"]

# ---------------------------
# EDIT WORKOUT
# ---------------------------
if "edit_id" in st.session_state:

    workout_id = st.session_state["edit_id"]

    st.header("Edit Workout")

    edit_exercise = st.text_input("New Exercise")
    edit_duration = st.number_input("New Duration", min_value=1)
    edit_calories = st.number_input("New Calories", min_value=0)
    edit_notes = st.text_input("New Notes")

    if st.button("Update Workout"):

        updated = {
            "exercise": edit_exercise,
            "duration": int(edit_duration),
            "calories": int(edit_calories),
            "notes": edit_notes
        }

        requests.put(
            f"{API}/workouts/{workout_id}",
            json=updated
        )

        st.success("Workout updated!")
        del st.session_state["edit_id"]
        st.rerun()

# ---------------------------
# STATS
# ---------------------------
st.header("Statistics")

col1, col2 = st.columns(2)

calories = requests.get(f"{API}/stats/total-calories").json()
duration = requests.get(f"{API}/stats/total-duration").json()

with col1:
    st.metric("Total Calories", calories["total_calories"])

with col2:
    st.metric("Total Minutes", duration["total_minutes"])