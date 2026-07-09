import streamlit as st


def render_sidebar(
    loader,
    navigator,
    project,
    current_lesson,
    completed_lessons,
    goto_lesson,
):

    lessons = loader.list_lessons(project)

    current, total = navigator.lesson_number(
        project,
        current_lesson,
    )

    completed = len(completed_lessons)

    with st.sidebar:

        st.title("Image Classification")

        st.progress(completed / total)

        st.caption(
            f"{completed} / {total} Lessons Completed"
        )

        st.divider()

        for index, lesson_name in enumerate(lessons):

            lesson = loader.load(
                project,
                lesson_name,
            )

            # Completed lesson
            if lesson.id in completed_lessons:

                label = f"{lesson.title}"
                disabled = False

            # Current lesson
            elif lesson_name == current_lesson:

                label = f"▶ {lesson.title}"
                disabled = True

            # First lesson is always unlocked
            elif index == 0:

                label = lesson.title
                disabled = False

            else:

                previous = loader.load(
                    project,
                    lessons[index - 1],
                )

                unlocked = (
                    previous.id
                    in completed_lessons
                )

                if unlocked:
                    label = lesson.title
                    disabled = False
                else:
                    label = f"🔒 {lesson.title}"
                    disabled = True

            if st.button(
                label,
                disabled=disabled,
                use_container_width=True,
                key=f"lesson_{lesson_name}",
            ):
                goto_lesson(lesson_name)