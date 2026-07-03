import streamlit as st


def render_lesson(lesson):

    st.title(lesson.title)

    st.markdown(
        f"**Objective:** {lesson.objective}"
    )

    with st.expander(
        "Concept",
        expanded=True,
    ):
        st.markdown(lesson.concept)

    st.subheader("Instructions")

    if isinstance(lesson.instructions, list):

        for item in lesson.instructions:
            st.markdown(f"- {item}")

    else:

        st.markdown(lesson.instructions)