import streamlit as st

from knowledge_gpt.components.faq import faq
from dotenv import load_dotenv
import os

load_dotenv()


def sidebar():
    with st.sidebar:
        st.markdown(
            "## OpenAI API key를 입력하고 사용하세요🔑\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=os.environ.get("OPENAI_API_KEY", None)
            or st.session_state.get("OPENAI_API_KEY", ""),
        )

        st.session_state["OPENAI_API_KEY"] = api_key_input

#        st.markdown("---")
#        st.markdown("# About")
#        st.markdown(
#            "📖KnowledgeGPT allows you to ask questions about your "
#            "documents and get accurate answers with instant citations. "
#        )
#        st.markdown(
#            "This tool is a work in progress. "
#            "You can contribute to the project on [GitHub](https://github.com/mmz-001/knowledge_gpt) "  # noqa: E501
#            "with your feedback and suggestions💡"
#        )
#        st.markdown("Made by [mmz_001](https://twitter.com/mm_sasmitha)")
#        st.markdown("---")

#        faq()
