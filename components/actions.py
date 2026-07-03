import streamlit as st


def render_actions():

    col1, col2, col3 = st.columns(3)

    if col1.button(
        "▶ Run Code",
        use_container_width=True,
    ):
        return "run"

    if col2.button(
        "Show Solution",
        use_container_width=True,
    ):
        return "solution"

    if col3.button(
        "Reset",
        use_container_width=True,
    ):
        return "reset"

    return None