import streamlit as st
import random

value = {0: "Rock", 1: "Paper", 2: "Scissors"}

MAX_ROUNDS = 5

# Başlangıçta skor ve tur sayısını ayarla
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "round" not in st.session_state:
    st.session_state.round = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("🪨 Rock - 📄 Paper - ✂️ Scissors Game")

def reset_game():
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.round = 0
    st.session_state.game_over = False

if st.session_state.game_over:
    st.markdown(f"## Game Over! 🎉")
    if st.session_state.user_score > st.session_state.computer_score:
        st.success(f"You won the game! Final score: {st.session_state.user_score} - {st.session_state.computer_score}")
    elif st.session_state.user_score < st.session_state.computer_score:
        st.error(f"You lost the game! Final score: {st.session_state.user_score} - {st.session_state.computer_score}")
    else:
        st.info(f"It's a tie! Final score: {st.session_state.user_score} - {st.session_state.computer_score}")

    if st.button("Play Again"):
        reset_game()
else:
    st.write(f"Round: {st.session_state.round + 1} / {MAX_ROUNDS}")
    user_choice = st.radio("Choose your move:", ["Rock", "Paper", "Scissors"])

    if st.button("Play"):
        user_index = ["Rock", "Paper", "Scissors"].index(user_choice)
        computer_index = random.randint(0, 2)

        st.write(f"🤖 Computer chose: **{value[computer_index]}**")
        st.write(f"🧑 You chose: **{user_choice}**")

        if user_index == computer_index:
            st.info("🤝 Draw!")
        elif (user_index == 0 and computer_index == 2) or \
             (user_index == 1 and computer_index == 0) or \
             (user_index == 2 and computer_index == 1):
            st.success("🎉 You Win this round!")
            st.session_state.user_score += 1
        else:
            st.error("😢 You Lose this round!")
            st.session_state.computer_score += 1

        st.session_state.round += 1
        st.write("---")
        st.write(f"### Scoreboard")
        st.write(f"🧑 You: {st.session_state.user_score}  |  🤖 Computer: {st.session_state.computer_score}")

        if st.session_state.round >= MAX_ROUNDS:
            st.session_state.game_over = True
