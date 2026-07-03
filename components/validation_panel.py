import streamlit as st


def render_validation(validation):

    if validation is None:
        return

    st.divider()

    st.subheader("Validation")

    if validation.success:

        st.success(validation.message)

    else:

        st.error(validation.message)

        for error in validation.errors:
            st.write(f"• {error}")