from components.monaco import monaco
import streamlit as st


def render_editor(lesson):

    code = st.session_state.editor_state.get(
        lesson.id,
        lesson.starter_code,
    )

    code = monaco(
        value=code,
        language="python",
        theme="vs-dark",
        height=500,
    )

    st.session_state.editor_state[
        lesson.id
    ] = code

    return code