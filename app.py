import streamlit as st
import pandas as pd
import sqlite3
import random

# Database setup
def init_db():
    conn = sqlite3.connect('deutlit.db')
    c = conn.cursor()
    # Create tables for questions, vocabulary, etc.
    c.execute('''CREATE TABLE IF NOT EXISTS questions (
                    id INTEGER PRIMARY KEY,
                    type TEXT,
                    level TEXT,
                    content TEXT,
                    answer TEXT
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS vocabulary (
                    id INTEGER PRIMARY KEY,
                    word TEXT,
                    translation TEXT,
                    level TEXT
                )''')
    # Insert sample data if empty
    c.execute("SELECT COUNT(*) FROM questions")
    if c.fetchone()[0] == 0:
        sample_data = [
            ('quiz', 'A1', 'What is the article for "Haus"?', 'das'),
            ('grammar', 'A1', 'Conjugate "sein" for "ich": ___', 'bin'),
            ('exam', 'A1', 'Drag the words to form a sentence.', 'sample')
        ]
        c.executemany("INSERT INTO questions (type, level, content, answer) VALUES (?, ?, ?, ?)", sample_data)
    c.execute("SELECT COUNT(*) FROM vocabulary")
    if c.fetchone()[0] == 0:
        vocab_data = [
            ('Haus', 'house', 'A1'),
            ('Auto', 'car', 'A1')
        ]
        c.executemany("INSERT INTO vocabulary (word, translation, level) VALUES (?, ?, ?)", vocab_data)
    conn.commit()
    conn.close()

init_db()

# Main app
st.title("Deutlit - German Learning App")

# Level selection
level = st.selectbox("Select your level", ["A1", "A2", "B1", "B2", "C1", "C2"])

# Feature selection
feature = st.selectbox("Choose a feature", ["Rapid Fire Quiz", "Grammar Exercises", "Vocabulary Flashcards", "Exam Preparation"])

if feature == "Rapid Fire Quiz":
    st.header("Rapid Fire Quiz - Article Learning")
    # Fetch questions
    conn = sqlite3.connect('deutlit.db')
    questions = pd.read_sql(f"SELECT * FROM questions WHERE type='quiz' AND level='{level}'", conn)
    conn.close()
    if not questions.empty:
        q = random.choice(questions.to_dict('records'))
        user_answer = st.text_input(q['content'])
        if st.button("Submit"):
            if user_answer.lower() == q['answer'].lower():
                st.success("Correct!")
            else:
                st.error(f"Wrong! Correct answer: {q['answer']}")
    else:
        st.write("No questions available for this level.")

elif feature == "Grammar Exercises":
    st.header("Fill in the Blanks - Grammar")
    conn = sqlite3.connect('deutlit.db')
    exercises = pd.read_sql(f"SELECT * FROM questions WHERE type='grammar' AND level='{level}'", conn)
    conn.close()
    if not exercises.empty:
        ex = random.choice(exercises.to_dict('records'))
        user_answer = st.text_input(ex['content'])
        if st.button("Submit"):
            if user_answer.lower() == ex['answer'].lower():
                st.success("Correct!")
            else:
                st.error(f"Wrong! Correct answer: {ex['answer']}")
    else:
        st.write("No exercises available for this level.")

elif feature == "Vocabulary Flashcards":
    st.header("Animated Vocabulary Flashcards")
    conn = sqlite3.connect('deutlit.db')
    vocab = pd.read_sql(f"SELECT * FROM vocabulary WHERE level='{level}'", conn)
    conn.close()
    if not vocab.empty:
        card = random.choice(vocab.to_dict('records'))
        if st.button("Show Translation"):
            st.write(f"{card['word']} - {card['translation']}")
        # Placeholder for animation
        st.write("Animation placeholder")
    else:
        st.write("No vocabulary available for this level.")

elif feature == "Exam Preparation":
    st.header("Exam Preparation - Drag and Drop")
    # Placeholder for drag and drop
    st.write("Drag and drop feature coming soon. Sample: Arrange words.")
    # For now, simple text
    st.text("Sample sentence: Ich ___ ein Auto. (habe)")
    user_input = st.text_input("Fill: ")
    if st.button("Check"):
        if user_input.lower() == "habe":
            st.success("Correct!")
        else:
            st.error("Try again.")

# Footer
st.write("Prototype version. Database sorted by Goethe levels.")