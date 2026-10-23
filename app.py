"""Streamlit demo: Flora-Captioner captions on SO-101 beer-pour episode 21."""

import base64
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

HERE = Path(__file__).parent


def b64(name: str) -> str:
    return base64.b64encode((HERE / name).read_bytes()).decode()


st.set_page_config(page_title="Flora trên SO-101", layout="wide")
st.title("Flora tự viết task instruction cho dataset SO-101")
st.caption("nvidia/Flora-Captioner · SO-101 rót bia · episode 21")

# Both cameras live in one component so a single button can drive them in sync.
html = (
    (HERE / "player.html").read_text(encoding="utf-8")
    .replace("__GLOBAL__", b64("global_ep21.mp4"))
    .replace("__WRIST__", b64("wrist_ep21.mp4"))
    .replace("__CAPTIONS__", json.dumps(json.loads((HERE / "captions.json").read_text(encoding="utf-8")), ensure_ascii=False))
)
components.html(html, height=620, scrolling=True)
