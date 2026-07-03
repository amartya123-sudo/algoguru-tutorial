import streamlit as st


def render_sidebar(
    loader,
    navigator,
    project,
    current_lesson,
    goto_lesson,
):

    current, total = navigator.lesson_number(
        project,
        current_lesson,
    )

    with st.sidebar:

        st.title("Image Classification")

        st.caption(
            f"Lesson {current} of {total}"
        )

        st.divider()

        for lesson_name in loader.list_lessons(project):

            if lesson_name == current_lesson:
                st.button(
                    f"📘 {lesson_name}",
                    disabled=True,
                    use_container_width=True,
                )
            else:
                if st.button(
                    lesson_name,
                    use_container_width=True,
                ):
                    goto_lesson(lesson_name)