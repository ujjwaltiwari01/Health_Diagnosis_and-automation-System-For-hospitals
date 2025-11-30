# 🏥 Healthcare Diagnosis Support System

 <div align="center">
 
 <img alt="Hospital" src="https://img.shields.io/badge/Healthcare-AI%20Agents-36C2CE?style=for-the-badge&logo=hospital" />
 <img alt="Streamlit" src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
 <img alt="OpenAI" src="https://img.shields.io/badge/OpenAI-GPT-412991?style=for-the-badge&logo=openai&logoColor=white" />
 <img alt="Gemini" src="https://img.shields.io/badge/Google-Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white" />
 
 <h3>👩‍⚕️ Your AI teammates for faster, safer, clearer clinical decisions</h3>
 <p>Multiple smart agents work together to read symptoms, review history, analyze images, check drugs, recommend treatments, and create patient-friendly instructions — with built‑in safety checks.</p>
 
 <a href="#-quickstart" style="text-decoration:none;"><img alt="Run Locally" src="https://img.shields.io/badge/%F0%9F%9A%80-Run%20Locally-10b981?style=for-the-badge" /></a>
 <a href="#-why-it-matters" style="text-decoration:none;"><img alt="Why" src="https://img.shields.io/badge/%F0%9F%92%A1-Why%20It%20Matters-f59e0b?style=for-the-badge" /></a>
 <a href="#-for-hospitals-clinics--doctors" style="text-decoration:none;"><img alt="Benefits" src="https://img.shields.io/badge/%F0%9F%8F%A5-Benefits-6366f1?style=for-the-badge" /></a>
 </div>

 ---

 ## ✨ What it does 
 - **You tell** the app what hurts and share an image (like an X‑ray) 🗣️🩻
 - **Little helper robots** talk to each other to think and check things 🤖🤝
 - They make a **doctor report** that’s safe, clear, and easy to follow 📄✅

 ### 🧠 Agents inside
 - **Symptom Analyzer** finds patterns
 - **History Reviewer** spots risks
 - **Imaging Analyst** reads X‑rays/MRI/CT with Gemini Vision
 - **Treatment Planner** suggests evidence‑based care
 - **Drug Safety** checks interactions
 - **Referral & Scheduling** routes to the right specialist
 - **Patient Communication** explains in simple words

 ---

 ## 🚀 Quickstart
 Follow these tiny steps and you’re done in minutes.

 1) 🧰 Install tools
 
 ```bash
 python -m venv .venv
 .venv\Scripts\activate   # Windows
 pip install -r requirements.txt
 ```

 2) 🔑 Add your keys
 
 ```bash
 copy .env.example .env   # or create .env
 # In .env set:
 OPENAI_API_KEY=sk-...
 GOOGLE_API_KEY=...
 ```

 3) 🖥️ Run the app
 
 ```bash
 streamlit run streamlit_app.py
 ```

 4) 🧪 Try the CLI (optional)
 
 ```bash
 python -m health_crew.app
 ```

 That’s it! Open the browser link (usually http://localhost:8501), fill the form, optionally upload an image, and click “Run Diagnosis”.

 ---

 ## 🏛 For Hospitals, Clinics, & Doctors
 This agent team reduces time-to-insight, standardizes care, and improves patient communication.

 | Stakeholder | Top Benefits | How It Helps |
 |---|---|---|
 | Hospitals 🏥 | Faster triage, operational efficiency, audit trails | Multi‑agent workflow with safety checkpoints and logs |
 | Clinics 🏩 | Consistent workups, less admin burden | Structured symptom/history intake, referral coordination |
 | Doctors 👨‍⚕️👩‍⚕️ | Decision support, interaction safety, clear plans | Evidence‑based suggestions, drug checks, patient‑ready summaries |

 ### 🔎 Why it matters
 - **Speed:** Parallel domain agents cut cognitive load and time.
 - **Safety:** Built‑in validation and escalation for red flags.
 - **Clarity:** Patient‑friendly output improves adherence.

 ## 🧠 Deep dive: Benefits by stakeholder

 ### 🏥 Hospitals
 - **Operational efficiency**
   - Reduce time-to-triage with structured symptom/history intake and auto-prioritization.
   - Standardize workups across departments with consistent multi-agent checklists.
   - Generate audit-ready logs of decisions, recommendations, and safety checks.
 - **Clinical quality & safety**
   - Evidence-based suggestions via guidelines lookup and drug interaction checks.
   - Emergency red flags trigger escalation via the safety tools.
   - Patient-friendly instructions improve adherence and reduce readmissions.
 - **IT & compliance**
   - Config-driven env vars; add real APIs gradually (FHIR, EHR, DrugBank, RxNorm, etc.).
   - Clear separation of concerns: agents, tasks, tools, workflows, logging.
   - Tracing option for debugging and QA of agent behavior.
 - **Example workflow**
   - Triage nurse enters symptoms ➜ upload chest X‑ray ➜ agents analyze ➜ report + safety flags ➜ referral suggestion with follow-up plan.
 - **Metrics to track**
   - Door‑to‑decision time, rate of guideline adherence, adverse drug event near‑misses, patient comprehension scores, readmission rates.

 ### 🏩 Clinics
 - **Operational**
   - Consistent intake and structured notes reduce documentation time.
   - Automatic referral coordination and follow-up scheduling lessen admin burden.
 - **Clinical**
   - Quick differentials for common complaints with imaging assist when provided.
   - Drug safety screening for polypharmacy patients.
 - **Implementation**
   - Start with Streamlit UI; plug in live APIs later.
   - Works offline with stubbed tools for demos/training.
 - **Example workflow**
   - GP enters symptoms + meds ➜ agent suggests plan ➜ checks interactions ➜ prints patient instructions.
 - **Metrics**
   - Visit duration, time spent on documentation, referral turnaround, follow‑up adherence.

 ### 👩‍⚕️👨‍⚕️ Doctors
 - **Decision support**
   - Structured differential from symptoms/history; optional imaging analysis with Gemini Vision.
   - Treatment options with monitoring and follow‑up reminders.
 - **Safety**
   - Interaction and contraindication flags; emergency escalation cues.
 - **Communication**
   - One‑click patient‑friendly summary to set expectations and red‑flag education.
 - **Example day**
   - Morning clinic: run 5 cases through the app ➜ standardized plans ➜ rapid patient summaries ➜ fewer after‑hours notes.
 - **KPIs**
   - Fewer prescribing errors, higher patient comprehension, improved throughput.

 #### 💰 ROI snapshot
 - **Time saved per case:** 3–8 minutes (intake + plan drafting + summary).
 - **Quality uplift:** More consistent adherence to guidelines and safety checks.
 - **Patient experience:** Clear take‑home plan reduces callbacks and confusion.

 ---

 ## 🧩 Features at a glance
 - ✅ Symptom analysis and differential
 - ✅ History review and risk flags
 - ✅ Imaging analysis with Gemini Vision (X‑ray, MRI, CT, ultrasound)
 - ✅ Treatment recommendations with guidelines lookup
 - ✅ Drug interaction checks
 - ✅ Referral and follow‑up planning
 - ✅ Patient‑friendly instructions
 - ✅ Streamlit web UI and CLI demo

 ---

 ## ⚙️ Configuration (env vars)
 Copy `.env.example` to `.env` and set:
 
 - `OPENAI_API_KEY` (required) – LLM agents
 - `GOOGLE_API_KEY` (required for imaging) – Gemini Vision
 - `OPENAI_MODEL` (optional, default `gpt-4o-mini`)
 - `GEMINI_MODEL` (optional, default `gemini-1.5-pro-latest`)
 - `LOG_LEVEL` (optional, default `INFO`)
 - Optional integrations: `UMLS_API_KEY`, `RXNORM_API_KEY`, `DRUGBANK_API_KEY`, `FHIR_BASE_URL`, `SCHEDULER_BASE_URL`, `GUIDELINES_API_URL`, `GUIDELINES_API_KEY`

 ---

 ## 🧭 How to use (step‑by‑step)
 - Open the app ➜ enter symptoms and demographics
 - Optional: upload an X‑ray/MRI/CT image
 - Click “Run Diagnosis”
 - Read the executive summary, dive into details, and download the report
 - Always have a clinician review before acting

 ---

 ## 🧪 What’s inside the UI
 The Streamlit app shows:
 - Patient form
 - Image upload & preview
 - Progress and tabs for summary, details, and technical output
 - Download button for the full report

 ---

 ## 📣 Lead funnel
 - ⭐ Like it? Star the repo to follow updates
 - 🧑‍💻 Want to integrate with EHR/Guidelines/Pharmacy APIs? Open an issue
 - 🤝 Pilot in your clinic/hospital? Start a discussion with your goals and timeline

 ---

 ## Web UI
  
  The system includes a modern Streamlit web interface (`streamlit_app.py`) with:
  - Patient information form
  - Medical image upload and analysis
  - Real-time multi-agent processing
  - Comprehensive diagnosis reports
  - API key validation and configuration

## Features

- Crew of domain-specialized agents with dedicated tools and tasks
- Sequential workflow ensuring safety checkpoints and validations
- Pluggable tool layer for real API integrations (UMLS, RxNorm, EHR/FHIR, DrugBank, etc.)
- Config-driven setup via environment variables
- Simple CLI entry point (`python -m health_crew.app`) for demonstration
- OpenAI LLM support with multi-agent orchestration (primary)

## Project Structure

Health_Crew/
{{ ... }}
    safety.py
    agents.py
    tools.py
    tasks.py
    workflows.py
    app.py
    utils/
      __init__.py
      logging.py

## Quickstart

1. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

2. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Copy `.env.example` to `.env` and fill in values:

   **Required:**
   - `OPENAI_API_KEY` - Your OpenAI API key (for LLM agents)
   - `GOOGLE_API_KEY` - Your Google AI API key (for medical imaging analysis)

   **Optional:**
   - `OPENAI_MODEL` (defaults to `gpt-4o-mini`)
   - `GEMINI_MODEL` (defaults to `gemini-1.5-pro-latest`)
   - `LOG_LEVEL` (defaults to `INFO`)

   Optional integrations for EHR/Guidelines/Pharmacy can be added later.

4. **Run the Web UI** (Recommended)

   ```bash
   streamlit run streamlit_app.py
   ```

   Open your browser to the displayed URL (typically http://localhost:8501). You can:
   - Enter patient symptoms, demographics, history
   - Upload medical images (X-ray, MRI, CT scans)
   - Run multi-agent diagnosis with or without imaging
   - View comprehensive diagnosis reports

5. **Or run the CLI demo**

   ```bash
   python -m health_crew.app
   ```

   You will be prompted to enter a mock patient case. The crew will run sequentially and print results.

## Medical Imaging Analysis

The system includes advanced medical imaging analysis powered by Google's Gemini Vision model:

### Supported Image Types
- X-rays (chest, bone, dental)
- MRI scans
- CT scans  
- Ultrasound images
- Other medical imaging modalities

### Capabilities
- **Automatic modality detection** - Identifies imaging type and anatomical region
- **Finding extraction** - Detects and describes abnormalities
- **Severity assessment** - Rates findings as Normal/Mild/Moderate/Severe
- **Diagnostic interpretation** - Provides differential diagnoses with confidence levels
- **Patient-friendly explanations** - Translates technical findings into clear language
- **Timeline comparison** - Compares current and previous images to track progression

### Usage
In the Streamlit UI, simply upload a medical image alongside patient information. The imaging analyst agent will automatically:
1. Analyze the image using Gemini Vision
2. Extract key findings and measurements
3. Integrate findings with patient symptoms and history
4. Include imaging results in the comprehensive diagnosis report

## Environment Variables

See `.env.example` for available variables.

### Required
- `OPENAI_API_KEY` - Your OpenAI API key (for LLM agents)
- `GOOGLE_API_KEY` - Your Google AI API key (for medical imaging with Gemini Vision)

### Optional LLM Configuration
- `OPENAI_MODEL` - e.g., `gpt-4o-mini` (default)
- `GEMINI_MODEL` - e.g., `gemini-1.5-pro-latest` (default for imaging)
- `LOG_LEVEL` - Logging verbosity: DEBUG, INFO, WARNING, ERROR

### Optional External Integrations (stubs provided)
- `UMLS_API_KEY`, `RXNORM_API_KEY`, `DRUGBANK_API_KEY` - Medical terminology and drug databases
- `FHIR_BASE_URL` - FHIR-compliant EHR integration
- `SCHEDULER_BASE_URL` - Appointment scheduling system
- `GUIDELINES_API_URL`, `GUIDELINES_API_KEY` - Clinical guidelines repository
  - To enable live clinical guidelines: The endpoint should support `GET /guidelines?q=<condition>` and return `{ "summary": "..." }`

### Tracing
- `CREWAI_TRACING_ENABLED=true` - Enable agent execution traces for debugging

## Notes on Safety and Compliance

- This system is designed strictly for decision support. All outputs require human physician review and approval.
- Emergency flags trigger an `emergency_alert_system` tool call for immediate escalation.
- The `validate_medical_recommendation` tool enforces dosage limits, interactions, and guideline checks (extend with real rulesets).
- Logging with provenance and confidence scoring is enabled in `utils/logging.py`.

## Extending Integrations

Implement the placeholders in `tools.py` to integrate with:

- UMLS, SNOMED CT, ICD-10/11
- RxNorm, DrugBank, FDA datasets
- FHIR-compliant EHRs
- Scheduling systems
- Clinical guideline repositories
Update `config.py` to load necessary API keys and endpoints, and ensure rate-limiting and error handling as needed.
