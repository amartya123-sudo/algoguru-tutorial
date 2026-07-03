from pathlib import Path
import streamlit.components.v1 as components

build_dir = Path(__file__).parent.parent / "frontend" / "dist"

_component = components.declare_component(
    "monaco_editor",
    path=str(build_dir),
)

def monaco(
    value="",
    language="python",
    theme="vs-dark",
    height=500,
    request_code=False,
    key=None,
):

    return _component(
        value=value,
        language=language,
        theme=theme,
        height=height,
        request_code=request_code,
        key=key,
        default=None,
    )