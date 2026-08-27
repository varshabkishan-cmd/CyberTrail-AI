from agent import CyberTrailAgent
import streamlit as st
import pandas as pd

from agent import CyberTrailAgent


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="CyberTrail AI",
    page_icon="🛡️",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main {
        background-color: #0e1117;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .hero {
        padding: 25px;
        border-radius: 12px;
        background: linear-gradient(90deg, #111827, #1f2937);
        border: 1px solid #334155;
        margin-bottom: 20px;
    }

    .status-box {
        padding: 12px;
        border-radius: 8px;
        background-color: #111827;
        border: 1px solid #334155;
        text-align: center;
    }

    .agent-step {
        padding: 12px;
        margin-bottom: 8px;
        border-radius: 8px;
        background-color: #111827;
        border-left: 4px solid #22c55e;
    }

    .evidence-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #111827;
        border: 1px solid #334155;
        margin-bottom: 10px;
    }

    .attack-path {
        padding: 20px;
        border-radius: 10px;
        background-color: #111827;
        border: 1px solid #334155;
        text-align: center;
        font-size: 18px;
        line-height: 2;
    }

    .summary-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #111827;
        border: 1px solid #334155;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <h1>🛡️ CYBERTRAIL AI</h1>
        <h3>Autonomous Cyber Threat Investigation Platform</h3>
        <p>
        Upload security event logs and allow CyberTrail AI to autonomously
        investigate suspicious activity, correlate evidence, identify the
        affected host, reconstruct the attack timeline and generate a
        risk assessment.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SYSTEM STATUS
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="status-box">
        🟢 <b>SYSTEM STATUS</b><br>
        ONLINE
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="status-box">
        🤖 <b>AGENT STATUS</b><br>
        READY
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="status-box">
        🔍 <b>INVESTIGATION MODE</b><br>
        AUTONOMOUS
        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

st.subheader("📂 Security Log Ingestion")

uploaded_file = st.file_uploader(
    "Upload Security Event CSV",
    type=["csv"]
)


if uploaded_file is None:

    st.info(
        "Upload a security event CSV to begin the autonomous investigation."
    )


else:

    try:

        df = pd.read_csv(uploaded_file)

        required_columns = [
            "timestamp",
            "source_ip",
            "destination_ip",
            "hostname",
            "user",
            "event_type",
            "process",
            "domain",
            "action"
        ]


        missing_columns = [

            column

            for column in required_columns

            if column not in df.columns

        ]


        if missing_columns:

            st.error(
                "Missing required columns: "
                + ", ".join(missing_columns)
            )


        else:

            st.success(
                f"Security log loaded successfully — "
                f"{len(df)} events detected."
            )


            # ------------------------------------------
            # DATASET OVERVIEW
            # ------------------------------------------

            st.subheader("📊 Dataset Overview")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Total Events",
                    len(df)
                )

            with col2:
                st.metric(
                    "Hosts",
                    df["hostname"].nunique()
                )

            with col3:
                st.metric(
                    "Users",
                    df["user"].nunique()
                )

            with col4:
                st.metric(
                    "Event Types",
                    df["event_type"].nunique()
                )


            # ------------------------------------------
            # DATA PREVIEW
            # ------------------------------------------

            with st.expander(
                "👁️ View Uploaded Security Events"
            ):

                st.dataframe(
                    df,
                    use_container_width=True
                )


            st.divider()


            # ------------------------------------------
            # INVESTIGATION BUTTON
            # ------------------------------------------

            if st.button(
                "🔍 START AUTONOMOUS INVESTIGATION",
                type="primary",
                use_container_width=True
            ):


                # --------------------------------------
                # AGENT WORKFLOW
                # --------------------------------------

                st.subheader(
                    "🤖 Autonomous Agent Workflow"
                )


                agent_status = st.empty()


                agent_status.markdown(
                    """
                    <div class="agent-step">
                    ⏳ STEP 1 — Ingesting and validating security logs
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                progress_bar = st.progress(10)


                progress_bar.progress(25)

                agent_status.markdown(
                    """
                    <div class="agent-step">
                    🔎 STEP 1 — Security logs ingested
                    </div>

                    <div class="agent-step">
                    🔍 STEP 2 — Investigating suspicious DNS activity
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                progress_bar.progress(45)


                agent_status.markdown(
                    """
                    <div class="agent-step">
                    🔎 STEP 1 — Security logs ingested
                    </div>

                    <div class="agent-step">
                    🔎 STEP 2 — DNS investigation completed
                    </div>

                    <div class="agent-step">
                    💻 STEP 3 — Investigating endpoint processes
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                progress_bar.progress(60)


                agent_status.markdown(
                    """
                    <div class="agent-step">
                    🔎 STEP 1 — Security logs ingested
                    </div>

                    <div class="agent-step">
                    🔎 STEP 2 — DNS investigation completed
                    </div>

                    <div class="agent-step">
                    🔎 STEP 3 — Endpoint investigation completed
                    </div>

                    <div class="agent-step">
                    🌐 STEP 4 — Investigating network communication
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                progress_bar.progress(75)


                agent_status.markdown(
                    """
                    <div class="agent-step">
                    🔎 STEP 1 — Security logs ingested
                    </div>

                    <div class="agent-step">
                    🔎 STEP 2 — DNS investigation completed
                    </div>

                    <div class="agent-step">
                    🔎 STEP 3 — Endpoint investigation completed
                    </div>

                    <div class="agent-step">
                    🔎 STEP 4 — Network investigation completed
                    </div>

                    <div class="agent-step">
                    🕒 STEP 5 — Reconstructing attack timeline
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                progress_bar.progress(90)


                # --------------------------------------
                # RUN AGENT
                # --------------------------------------

                with st.spinner(
                    "CyberTrail Agent is correlating evidence..."
                ):

                    agent = CyberTrailAgent(df)

                    result = agent.investigate()


                progress_bar.progress(100)


                agent_status.markdown(
                    """
                    <div class="agent-step">
                    ✅ INVESTIGATION COMPLETE
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                st.success(
                    "CyberTrail AI completed the autonomous investigation."
                )


                st.divider()


                # --------------------------------------
                # INVESTIGATION RESULT
                # --------------------------------------

                st.header(
                    "🚨 Investigation Result"
                )


                col1, col2, col3, col4 = st.columns(4)


                with col1:

                    st.metric(
                        "Affected Host",
                        result["affected_host"]
                    )


                with col2:

                    st.metric(
                        "Risk Level",
                        result["risk_level"]
                    )


                with col3:

                    st.metric(
                        "Risk Score",
                        f'{result["risk_score"]}/100'
                    )


                with col4:

                    st.metric(
                        "Evidence Indicators",
                        len(result["findings"])
                    )


                st.divider()


                # --------------------------------------
                # EVIDENCE
                # --------------------------------------

                st.subheader(
                    "🔎 Evidence Correlation"
                )


                if result["findings"]:

                    for finding in result["findings"]:

                        st.markdown(
                            f"""
                            <div class="evidence-box">
                            ⚠️ {finding}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


                else:

                    st.success(
                        "No suspicious indicators were detected."
                    )


                st.divider()


                # --------------------------------------
                # ATTACK PATH
                # --------------------------------------

                st.subheader(
                    "🧭 Reconstructed Attack Path"
                )


                st.markdown(
                    f"""
                    <div class="attack-path">

                    🌐 External Activity

                    ↓

                    🔍 Suspicious DNS Activity

                    ↓

                    🖥️ {result["affected_host"]}

                    ↓

                    💻 Suspicious Process Execution

                    ↓

                    🌐 Outbound Communication

                    ↓

                    🔗 Internal Communication

                    ↓

                    📁 File Activity

                    </div>
                    """,
                    unsafe_allow_html=True
                )


                st.divider()


                # --------------------------------------
                # AGENT EXPLANATION
                # --------------------------------------

                st.subheader(
                    "🧠 Autonomous Investigation Summary"
                )


                summary = (
                    f"CyberTrail AI identified "
                    f"{result['affected_host']} as the primary host "
                    f"of interest by correlating evidence across "
                    f"DNS activity, endpoint processes and network "
                    f"communications. The autonomous agent analyzed "
                    f"{len(df)} security events and detected "
                    f"{len(result['findings'])} key suspicious "
                    f"indicators. The final risk assessment is "
                    f"{result['risk_level']} with a risk score of "
                    f"{result['risk_score']}/100."
                )


                st.markdown(
                    f"""
                    <div class="summary-box">
                    {summary}
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                st.divider()


                # --------------------------------------
                # ATTACK TIMELINE
                # --------------------------------------

                st.subheader(
                    "🕒 Reconstructed Investigation Timeline"
                )


                st.dataframe(
                    result["timeline"],
                    use_container_width=True
                )


                # --------------------------------------
                # DOWNLOAD REPORT
                # --------------------------------------

                st.divider()

                st.subheader(
                    "📥 Export Investigation Report"
                )


                report = f"""
CYBERTRAIL AI
AUTONOMOUS CYBER THREAT INVESTIGATION REPORT

Affected Host:
{result["affected_host"]}

Risk Level:
{result["risk_level"]}

Risk Score:
{result["risk_score"]}/100

Evidence Indicators:
"""


                for finding in result["findings"]:

                    report += f"\n- {finding}"


                report += f"""

Investigation Summary:

{summary}
"""


                st.download_button(
                    label="📄 Download Investigation Report",
                    data=report,
                    file_name="CyberTrail_Investigation_Report.txt",
                    mime="text/plain",
                    use_container_width=True
                )


    except Exception as e:

        st.error(
            f"Unable to process the uploaded file: {e}"
        )