import streamlit as st
import random

value = {0: "Rock", 1: "Paper", 2: "Scissors"}

st.title("🪨 Rock - 📄 Paper - ✂️ Scissors Game")

user_choice = st.radio("Choose your move:", ["Rock", "Paper", "Scissors"])
if st.button("Play"):
    user_index = ["Rock", "Paper", "Scissors"].index(user_choice)
    computer_index = random.randint(0, 2)

    st.write(f"🤖 Computer chose: {value[computer_index]}")
    st.write(f"🧑 You chose: {user_choice}")

    if user_index == computer_index:
        st.info("🤝 Draw!")
    elif (user_index == 0 and computer_index == 2) or \
         (user_index == 1 and computer_index == 0) or \
         (user_index == 2 and computer_index == 1):
        st.success("🎉 You Win!")
    else:
        st.error("😢 You Lose!")
