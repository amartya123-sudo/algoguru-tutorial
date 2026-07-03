import streamlit as st


def render_navigation(
    navigator,
    project,
    current_lesson,
    goto_lesson,
):

    st.divider()

    left, right = st.columns(2)

    previous = navigator.previous_lesson(
        project,
        current_lesson,
    )

    if previous:

        if left.button(
            "← Previous",
            use_container_width=True,
        ):
            goto_lesson(previous)

    next_lesson = navigator.next_lesson(
        project,
        current_lesson,
    )

    if next_lesson:

        if right.button(
            "Next →",
            use_container_width=True,
        ):
            goto_lesson(next_lesson)