from components.monaco import monaco
import streamlit as st


def render_editor(lesson):

    code = st.session_state.editor_state.get(
        lesson.id,
        lesson.starter_code,
    )

    new_code = monaco(
        value=code,
        language="python",
        theme="vs-dark",
        height=500,
    )

    # Handle case where monaco returns None
    if new_code is not None:
        code = new_code
        st.session_state.editor_state[
            lesson.id
        ] = code

    return code