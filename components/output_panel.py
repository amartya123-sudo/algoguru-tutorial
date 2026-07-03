import streamlit as st


def render_output(result):

    if result is None:
        return

    st.divider()

    st.subheader("Output")

    if result.stdout:
        st.code(result.stdout)

    if result.stderr:
        st.error(result.stderr)

    st.caption(
        f"Execution Time: {result.time_taken:.3f} sec"
    )