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


st.set_page_config(
    page_title="AlgoGuru",
    layout="wide",
)


loader = LessonLoader()
navigator = LessonNavigator(loader)

executor = Executor()
validator = Validator()


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


def goto_lesson(name):

    st.session_state.current_lesson = name

    st.session_state.execution = None
    st.session_state.validation = None

    st.rerun()


init_state()


lesson = loader.load(
    PROJECT,
    st.session_state.current_lesson,
)


render_sidebar(
    loader=loader,
    navigator=navigator,
    project=PROJECT,
    current_lesson=st.session_state.current_lesson,
    goto_lesson=goto_lesson,
)


render_lesson(lesson)


editor_code = render_editor(lesson)


action = render_actions()


if action == "reset":

    st.session_state.editor_state[
        lesson.id
    ] = lesson.starter_code

    st.rerun()


elif action == "solution":

    st.code(
        lesson.solution_code,
        language="python",
    )


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


render_output(
    st.session_state.execution
)

render_validation(
    st.session_state.validation
)


render_navigation(
    navigator=navigator,
    project=PROJECT,
    current_lesson=st.session_state.current_lesson,
    goto_lesson=goto_lesson,
)