import streamlit as st

st.set_page_config(page_title="John Eastman", page_icon="🦦", layout="wide")
st.header("My Projects")
# ---- PROJECTS ----
st.write("---")
text_column, image_column = st.columns((4, 3))
with text_column:
    st.subheader("RFP Monster")
    st.write(
        """
        The RFPMonster is a GenAI Workflow (RAG) that automatically generates answers to questions posed by potential clients (RFPs) and
        categorizes the LLM responses with predictive AI models. The project won 2nd place in the company-wide hackathon,
        and was presented in the company's internal summer meeting, and its Fall launch (https://www.youtube.com/watch?v=Wf0iF5akLOA).
        """
    )
with image_column:
    st.markdown("![rfp_monster](./app/static/rfp_monster.gif)")
st.write("---")
text_column_2, image_column_2 = st.columns((4, 3))
with text_column_2:
    st.subheader("GRAGORI")
    st.write(
        """
        GenAI Workflow that generates answers to customer complaints on a specific product by generating and
        querying a knowledge graph from the product's documentation (neo4j)     
        """
    )
with image_column_2:
    st.markdown("![rfp_monster](./app/static/rfp_monster.gif)")