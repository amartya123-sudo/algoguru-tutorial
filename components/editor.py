from components.monaco import monaco
import streamlit as st


def render_editor(lesson):

    initial_code = st.session_state.editor_state.get(
        lesson.id,
        lesson.starter_code,
    )

    code = monaco(
        value=initial_code,
        language="python",
        theme="vs-dark",
        height=500,
        key=f"editor_{lesson.id}",
    )

    if code is None:
        code = initial_code

    st.session_state.editor_state[lesson.id] = code

    return code