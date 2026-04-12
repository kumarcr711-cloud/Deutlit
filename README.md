# Deutlit

Deutlit is a Streamlit-based German learning app focused on helping learners improve faster through structured practice aligned to Goethe and CEFR levels (A1 to C2).

Current status: Prototype

## Vision

Build a practical and engaging learning experience for German learners through short, focused exercises that improve:

- Article accuracy
- Grammar confidence
- Vocabulary retention
- Exam readiness

## Core Features

### 1. Rapid Fire Quiz

Fast article drills (der, die, das) with instant feedback.

### 2. Grammar Exercises

Fill-in-the-blank tasks for conjugations and sentence structure by difficulty level.

### 3. Vocabulary Flashcards

Level-based vocabulary cards designed for repetition and recall.

### 4. Exam Preparation

Practice modules inspired by Goethe-style exam formats.

## What Is Implemented Today

- Level selector (A1 to C2)
- Quiz and grammar prompts with answer checking
- Vocabulary display from a local SQLite database
- Initial exam placeholder module
- Bootstrap sample data on first run

## Planned Improvements

- Timed quiz mode with streaks and scoring
- Better grammar feedback with short rule explanations
- Spaced repetition for vocabulary
- Progress tracking and weak-topic recommendations
- Real drag-and-drop interactions for exam tasks
- Expanded and validated question banks per CEFR level

## Suggested Architecture

The app is currently a single-file prototype.

See the full architecture diagram and component responsibilities in [ARCHITECTURE.md](ARCHITECTURE.md).
For runtime interaction flow, see [DATAFLOW.md](DATAFLOW.md).

### Proposed Module Structure

```text
deutlit/
	app.py
	src/
		ui/
			pages/
		services/
			quiz_service.py
			grammar_service.py
			vocab_service.py
			exam_service.py
			progress_service.py
		data/
			repositories.py
			schema.sql
			seed_data.py
		models/
			question.py
			vocab_item.py
			user_progress.py
	tests/
		test_quiz_service.py
		test_grammar_service.py
```

## Tech Stack

- Python
- Streamlit
- SQLite
- Pandas

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ArsalYoosuf/Deutlit.git
cd Deutlit
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

## Roadmap

- v0.1: Prototype with core modes and local data
- v0.2: Scoring, timer, and progress tracking
- v0.3: Expanded content and personalized practice
- v1.0: Full exam preparation flows with analytics

## Contributing

Contributions are welcome. If you want to help, open an issue with:

- Feature proposal
- Bug report
- UX suggestion
- Content quality improvement

## License

This project is licensed under the terms in the LICENSE file.
