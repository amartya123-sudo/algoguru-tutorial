# AlgoGuru Tutorial Platform

An interactive AI learning platform built with **Streamlit** and a custom **Monaco Editor**, allowing learners to complete hands-on coding tutorials directly in the browser. The current implementation includes a complete **Image Classification** tutorial consisting of 12 guided lessons, each with its own starter code, execution scaffold, validator, and reference solution.

---

# Features

* Interactive Monaco code editor
* Python code execution
* Lesson-by-lesson learning
* Hidden execution scaffold
* Automatic validation
* Solution viewer
* Previous/Next lesson navigation
* Modular architecture
* Easy to add new tutorials
* Completely local execution
* Beginner-friendly workflow

---

# Project Structure

```text
algoguru-tutorial/
│
├── app.py
│
├── components/
│   ├── monaco.py
│   ├── sidebar.py
│   ├── lesson.py
│   ├── editor.py
│   ├── actions.py
│   ├── output.py
│   ├── validation.py
│   └── navigation.py
│
├── engine/
│   ├── executor.py
│   ├── loader.py
│   ├── navigation.py
│   ├── validator.py
│   ├── models.py
│   └── progress.py
│
├── tutorials/
│   └── image_classification/
│       ├── lesson01/
│       ├── lesson02/
│       ├── ...
│       └── lesson12/
│
├── frontend/
│   └── dist/
│
├── assets/
│
└── requirements.txt
```

---

# Architecture

```text
User
 │
 ▼
Monaco Editor
 │
 ▼
app.py
 │
 ├───────────────┐
 ▼               ▼
LessonLoader   Executor
 │               │
 ▼               ▼
Lesson       Python Execution
 │               │
 └───────► Validator
                 │
                 ▼
          Output + Feedback
```

---

# Execution Flow

1. User selects a lesson.
2. Lesson metadata is loaded.
3. Starter code is displayed in Monaco.
4. User writes or modifies the code.
5. Clicking **Run Code** sends the editor content to the execution engine.
6. The scaffold injects the user's code into a controlled execution template.
7. Python executes the generated script.
8. Global variables are collected.
9. The validator checks the execution results.
10. Output and validation feedback are displayed.

---

# Lesson Structure

Each lesson contains the following files:

```text
lesson01/
│
├── lesson.yaml
├── starter.py
├── scaffold.py
├── validator.py
└── solution.py
```

---

# lesson.yaml

Stores all lesson metadata.

Example:

```yaml
id: lesson01

title: Import Libraries

difficulty: Beginner

estimated_time: 5

objective: Learn the required libraries.

concept: |
  PyTorch provides...

instructions:
  - Import torch
  - Import torchvision.transforms

hint: Use import statements.

success_message: Great!

next_lesson: lesson02
```

---

# starter.py

Contains the initial code shown inside the Monaco editor.

Example:

```python
import torch
```

---

# scaffold.py

Acts as a hidden execution wrapper.

Example:

```python
{{USER_CODE}}

print("Execution Finished")

context = globals()
```

The placeholder `{{USER_CODE}}` is replaced by the editor content before execution.

---

# validator.py

Checks whether the learner completed the lesson correctly.

Example:

```python
def validate(namespace):

    errors = []

    if "torch" not in namespace:
        errors.append("Import torch.")

    return {
        "success": len(errors) == 0,
        "message": "Great Job!",
        "errors": errors
    }
```

---

# solution.py

Contains the reference implementation.

The learner can view this after completing or whenever the UI allows.

---

# Loader

`LessonLoader` loads every lesson into memory.

Responsibilities:

* Discover projects
* Discover lessons
* Read lesson files
* Parse YAML metadata
* Return a complete `Lesson` object

---

# Lesson Model

Every lesson is represented as a dataclass.

```python
Lesson

id
title
difficulty
estimated_time
objective
concept
instructions
hint
success_message
next_lesson

starter_code
scaffold_code
validator_code
solution_code
```

---

# Monaco Editor

The editor is implemented as a custom Streamlit component.

Responsibilities:

* Display starter code
* Syntax highlighting
* Theme support
* Return edited code
* Preserve editor state

The editor is intentionally isolated from the execution engine.

---

# Executor

The execution engine is responsible for running learner code safely.

Process:

1. Receive scaffold
2. Inject user code
3. Generate temporary Python file
4. Execute using subprocess
5. Capture stdout
6. Capture stderr
7. Collect globals
8. Return execution result

Returned information includes:

* stdout
* stderr
* execution time
* success flag
* execution namespace

---

# Validator

The validator executes lesson-specific validation logic.

It receives the execution namespace.

Example:

```python
validate(globals())
```

Returns:

```python
{
    success,
    message,
    errors
}
```

Each lesson can define completely different validation logic.

---

# Navigation

The navigation engine provides:

* First lesson
* Previous lesson
* Next lesson
* Lesson numbering

Navigation logic is separated from the UI.

---

# Session State

The application stores:

```text
current_lesson

editor_state

execution

validation
```

`editor_state` remembers code independently for every lesson.

---

# Components

## Sidebar

Displays:

* project
* lessons
* current lesson

---

## Lesson

Displays:

* title
* objective
* concept
* instructions

---

## Editor

Displays Monaco and stores code.

---

## Actions

Buttons:

* Run
* Reset
* Show Solution

---

## Output

Displays:

* stdout
* stderr
* execution time

---

## Validation

Displays:

* success message
* validation errors

---

## Navigation

Displays:

* Previous
* Next

---

# Adding a New Lesson

Create:

```text
lesson13/

lesson.yaml

starter.py

scaffold.py

validator.py

solution.py
```

No application changes are required.

---

# Adding a New Tutorial

Create:

```text
tutorials/

object_detection/

lesson01/

lesson02/
```

The loader discovers projects automatically.

---

# Execution Safety

The scaffold separates user code from hidden execution logic.

Advantages:

* Controlled execution
* Hidden tests
* Reusable lesson templates
* Cleaner validation

---

# Why Use a Scaffold?

Instead of executing only:

```python
USER_CODE
```

the platform executes:

```python
{{USER_CODE}}

hidden execution

validation context

print(...)
```

This allows lessons to include datasets, helper functions, hidden assertions, or evaluation code without exposing them to the learner.

---

# Current Tutorial

## Image Classification

Lessons include:

1. Import Libraries
2. Image Transformations
3. Loading Images
4. Custom Dataset
5. DataLoader
6. CNN Architecture
7. Forward Pass
8. Loss Function
9. Optimizer
10. Training Loop
11. Model Evaluation
12. Prediction

---

# Technology Stack

* Python
* Streamlit
* Custom Monaco Editor
* PyTorch
* Torchvision
* Pillow
* YAML
* Dataclasses

---

# Future Improvements

* Progress tracking
* Hint system
* Locked solutions
* Split-pane IDE layout
* Dataset explorer
* Image preview
* File explorer
* Multiple AI projects
* Object Detection tutorial
* Image Segmentation tutorial
* NLP tutorial
* LLM tutorial
* RAG tutorial
* Persistent progress
* Certificates

---

# Development Philosophy

The project follows a modular architecture:

* UI components are independent.
* Business logic is contained within the engine.
* Lessons are data-driven.
* Projects are plug-and-play.
* Monaco is independent of execution.
* Validators are lesson-specific.
* New tutorials require no engine modifications.

This separation keeps the codebase maintainable, scalable, and easy to extend as additional AI tutorials and learning features are added.
