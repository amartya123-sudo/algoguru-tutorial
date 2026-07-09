# import streamlit as st

# from components.actions import render_actions
# from components.editor import render_editor
# from components.lesson_view import render_lesson
# from components.navigation_bar import render_navigation
# from components.output_panel import render_output
# from components.sidebar import render_sidebar
# from components.validation_panel import render_validation

# from engine.executor import Executor
# from engine.loader import LessonLoader
# from engine.navigation import LessonNavigator
# from engine.validator import Validator


# PROJECT = "image_classification"


# st.set_page_config(
#     page_title="AlgoGuru",
#     layout="wide",
# )


# loader = LessonLoader()
# navigator = LessonNavigator(loader)

# executor = Executor()
# validator = Validator()


# def init_state():

#     if "current_lesson" not in st.session_state:
#         st.session_state.current_lesson = (
#             navigator.first_lesson(PROJECT)
#         )

#     if "editor_state" not in st.session_state:
#         st.session_state.editor_state = {}

#     if "execution" not in st.session_state:
#         st.session_state.execution = None

#     if "validation" not in st.session_state:
#         st.session_state.validation = None


# def goto_lesson(name):

#     st.session_state.current_lesson = name

#     st.session_state.execution = None
#     st.session_state.validation = None

#     st.rerun()


# init_state()


# lesson = loader.load(
#     PROJECT,
#     st.session_state.current_lesson,
# )


# render_sidebar(
#     loader=loader,
#     navigator=navigator,
#     project=PROJECT,
#     current_lesson=st.session_state.current_lesson,
#     goto_lesson=goto_lesson,
# )


# render_lesson(lesson)


# editor_code = render_editor(lesson)


# action = render_actions()


# if action == "reset":

#     st.session_state.editor_state[
#         lesson.id
#     ] = lesson.starter_code

#     st.rerun()


# elif action == "solution":

#     st.code(
#         lesson.solution_code,
#         language="python",
#     )


# elif action == "run":

#     result = executor.run(
#         lesson.scaffold_code,
#         editor_code,
#     )

#     validation = validator.run(
#         lesson.validator_code,
#         result.globals_dict,
#     )

#     st.session_state.execution = result
#     st.session_state.validation = validation


# render_output(
#     st.session_state.execution
# )

# render_validation(
#     st.session_state.validation
# )


# render_navigation(
#     navigator=navigator,
#     project=PROJECT,
#     current_lesson=st.session_state.current_lesson,
#     goto_lesson=goto_lesson,
# )

import streamlit as st

from components.actions import render_actions
from components.editor import render_editor
from components.lesson_view import render_lesson
from components.navigation_bar import render_navigation
from components.output_panel import render_output
from components.sidebar import render_sidebar
from components.validation_panel import render_validation

from engine.executor import Executor
from engine.loader import LessonLoader
from engine.navigation import LessonNavigator
from engine.validator import Validator


PROJECT = "image_classification"


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AlgoGuru",
    layout="wide",
)


# -------------------------------------------------
# Engine
# -------------------------------------------------

loader = LessonLoader()
navigator = LessonNavigator(loader)

executor = Executor()
validator = Validator()


# -------------------------------------------------
# Session State
# -------------------------------------------------

def init_state():

    if "current_lesson" not in st.session_state:
        st.session_state.current_lesson = (
            navigator.first_lesson(PROJECT)
        )

    if "editor_state" not in st.session_state:
        st.session_state.editor_state = {}

    if "execution" not in st.session_state:
        st.session_state.execution = None

    if "validation" not in st.session_state:
        st.session_state.validation = None

    if "completed_lessons" not in st.session_state:
        st.session_state.completed_lessons = set()


init_state()


# -------------------------------------------------
# Navigation
# -------------------------------------------------

def goto_lesson(lesson_name):

    lessons = loader.list_lessons(PROJECT)

    index = lessons.index(lesson_name)

    # Always allow first lesson
    if index > 0:

        previous = loader.load(
            PROJECT,
            lessons[index - 1],
        )

        if (
            previous.id
            not in st.session_state.completed_lessons
        ):

            st.warning(
                "Complete the previous lesson first."
            )
            return

    st.session_state.current_lesson = lesson_name

    st.session_state.execution = None
    st.session_state.validation = None

    st.rerun()


# -------------------------------------------------
# Current Lesson
# -------------------------------------------------

lesson = loader.load(
    PROJECT,
    st.session_state.current_lesson,
)


# -------------------------------------------------
# Sidebar
# -------------------------------------------------

render_sidebar(
    loader=loader,
    navigator=navigator,
    project=PROJECT,
    current_lesson=st.session_state.current_lesson,
    completed_lessons=st.session_state.completed_lessons,
    goto_lesson=goto_lesson,
)


# -------------------------------------------------
# Lesson
# -------------------------------------------------

render_lesson(lesson)


# -------------------------------------------------
# Editor
# -------------------------------------------------

editor_code = render_editor(lesson)


# -------------------------------------------------
# Actions
# -------------------------------------------------

action = render_actions()


# -------------------------------------------------
# Reset
# -------------------------------------------------

if action == "reset":

    st.session_state.editor_state[
        lesson.id
    ] = lesson.starter_code

    st.session_state.execution = None
    st.session_state.validation = None

    st.rerun()


# -------------------------------------------------
# Solution
# -------------------------------------------------

elif action == "solution":

    st.code(
        lesson.solution_code,
        language="python",
    )


# -------------------------------------------------
# Run
# -------------------------------------------------

elif action == "run":

    result = executor.run(
        lesson.scaffold_code,
        editor_code,
    )

    validation = validator.run(
        lesson.validator_code,
        result.globals_dict,
    )

    st.session_state.execution = result
    st.session_state.validation = validation

    if validation.success:

        st.session_state.completed_lessons.add(
            lesson.id
        )

        st.success(
            "🎉 Lesson completed! Next lesson unlocked."
        )


# -------------------------------------------------
# Output
# -------------------------------------------------

render_output(
    st.session_state.execution
)


# -------------------------------------------------
# Validation
# -------------------------------------------------

render_validation(
    st.session_state.validation
)


# -------------------------------------------------
# Navigation
# -------------------------------------------------

render_navigation(
    navigator=navigator,
    loader=loader,
    project=PROJECT,
    current_lesson=st.session_state.current_lesson,
    completed_lessons=st.session_state.completed_lessons,
    goto_lesson=goto_lesson,
)