import streamlit as st


def render_navigation(
    navigator,
    loader,
    project,
    current_lesson,
    completed_lessons,
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

    lesson = loader.load(
        project,
        current_lesson,
    )

    next_lesson = navigator.next_lesson(
        project,
        current_lesson,
    )

    if next_lesson:

        if lesson.id in completed_lessons:

            if right.button(
                "Next Lesson →",
                use_container_width=True,
            ):
                goto_lesson(next_lesson)

        else:

            right.info(
                "Complete this lesson to unlock the next lesson."
            )