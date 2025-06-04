import streamlit as st
import os

# Konfiguration der Seite
st.set_page_config(page_title="Samarah Creator Studio", page_icon="🌸", layout="centered")

# Lichtvoller Header
st.markdown("""
    <div style='background-color:#FDF6EC; padding:20px; border-radius:15px; box-shadow: 0px 0px 10px #FAD9C4;'>
        <h1 style='color:#D49494; text-align:center;'>🌸 Samarah Creator Studio</h1>
        <p style='color:#7B5E57; text-align:center; font-size:18px;'>Erstelle, lade hoch & verwalte Deine spirituellen Inhalte</p>
    </div>
    """, unsafe_allow_html=True)

# Navigation
menu = st.sidebar.radio("📂 Module auswählen", ("Home", "Affirmationen", "Workbooks", "Meditationen", "Modulübersicht", "KI-Module"))





# === ALLE Upload-Ordner definieren ===
UPLOAD_FOLDER = "uploads"
AFFIRMATIONS_FOLDER = "uploads/affirmations"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AFFIRMATIONS_FOLDER, exist_ok=True)

# Home-Modul
if menu == "Home":
    st.subheader("✨ Allgemeine Datei-Uploads")

    uploaded_file = st.file_uploader("Wähle eine Datei zum Hochladen:", type=["png", "jpg", "pdf", "zip"])
    if uploaded_file is not None:
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"✅ Datei '{uploaded_file.name}' erfolgreich hochgeladen!")

    st.subheader("📂 Hochgeladene Dateien:")

    # Nur echte Dateien anzeigen, keine versteckten wie .DS_Store
    files = [
        file for file in os.listdir(UPLOAD_FOLDER)
        if os.path.isfile(os.path.join(UPLOAD_FOLDER, file))
        and not file.startswith('.')
    ]

    if files:
        for file in files:
            file_path = os.path.join(UPLOAD_FOLDER, file)
            with open(file_path, "rb") as f:
                st.download_button(label=f"⬇️ {file}", data=f, file_name=file)
    else:
        st.write("🕊️ Noch keine Dateien vorhanden.")

# Affirmationen-Modul
elif menu == "Affirmationen":
    st.subheader("🌸 Affirmationen Upload")

    affirm_file = st.file_uploader("Wähle ein Affirmationsbild hochzuladen:", type=["png", "jpg", "jpeg"])
    if affirm_file is not None:
        file_path = os.path.join(AFFIRMATIONS_FOLDER, affirm_file.name)
        with open(file_path, "wb") as f:
            f.write(affirm_file.getbuffer())
        st.success(f"✅ Affirmationsbild '{affirm_file.name}' erfolgreich hochgeladen!")

    st.subheader("🌼 Deine Affirmationen:")

    allowed_extensions = (".png", ".jpg", ".jpeg")
    files = []

    for entry in os.scandir(AFFIRMATIONS_FOLDER):
        if entry.is_file() and entry.name.lower().endswith(allowed_extensions) and not entry.name.startswith('.'):
            files.append(entry.name)

    if files:
        for file in files:
            file_path = os.path.join(AFFIRMATIONS_FOLDER, file)
            st.image(file_path, caption=file, width=300)
            with open(file_path, "rb") as f:
                st.download_button(label=f"⬇️ {file}", data=f, file_name=file)
    else:
        st.write("🕊️ Noch keine Affirmationen hochgeladen.")
        
# Workbooks-Modul
elif menu == "Workbooks":

    st.subheader("📖 Workbooks & PDF Upload")

    WORKBOOKS_FOLDER = "uploads/workbooks"
    os.makedirs(WORKBOOKS_FOLDER, exist_ok=True)

    workbook_file = st.file_uploader("Lade Dein Workbook als PDF hoch:", type=["pdf"])

    if workbook_file is not None:
        file_path = os.path.join(WORKBOOKS_FOLDER, workbook_file.name)
        with open(file_path, "wb") as f:
            f.write(workbook_file.getbuffer())
        st.success(f"✅ Workbook '{workbook_file.name}' erfolgreich hochgeladen!")

    st.subheader("📂 Deine hochgeladenen Workbooks:")

    files = [
        file for file in os.listdir(WORKBOOKS_FOLDER)
        if os.path.isfile(os.path.join(WORKBOOKS_FOLDER, file))
        and file.lower().endswith(".pdf")
        and not file.startswith('.')
    ]

    if files:
        for file in files:
            file_path = os.path.join(WORKBOOKS_FOLDER, file)
            st.write(f"📄 {file}")
            with open(file_path, "rb") as f:
                st.download_button(label=f"⬇️ {file}", data=f, file_name=file)
    else:
        st.write("🕊️ Noch keine Workbooks hochgeladen.")
# Meditationen-Modul
elif menu == "Meditationen":

    st.subheader("🎧 Meditationen & Audio Upload")

    MEDITATION_FOLDER = "uploads/meditations"
    os.makedirs(MEDITATION_FOLDER, exist_ok=True)

    meditation_file = st.file_uploader("Lade Deine Meditation hoch:", type=["mp3", "wav"])

    if meditation_file is not None:
        file_path = os.path.join(MEDITATION_FOLDER, meditation_file.name)
        with open(file_path, "wb") as f:
            f.write(meditation_file.getbuffer())
        st.success(f"✅ Meditation '{meditation_file.name}' erfolgreich hochgeladen!")

    st.subheader("🎼 Deine hochgeladenen Meditationen:")

    files = [
        file for file in os.listdir(MEDITATION_FOLDER)
        if os.path.isfile(os.path.join(MEDITATION_FOLDER, file))
        and file.lower().endswith((".mp3", ".wav"))
        and not file.startswith('.')
    ]

    if files:
        for file in files:
            file_path = os.path.join(MEDITATION_FOLDER, file)
            st.audio(file_path)
            with open(file_path, "rb") as f:
                st.download_button(label=f"⬇️ {file}", data=f, file_name=file)
    else:
        st.write("🕊️ Noch keine Meditationen hochgeladen.")

elif menu == "Modulübersicht":

    st.subheader("🗂️ Samarah Creator Studio – Modulübersicht")

    st.markdown("""
    <style>
    .status-active {color: green; font-weight: bold;}
    .status-inprogress {color: orange; font-weight: bold;}
    </style>
    """, unsafe_allow_html=True)

    modules = {
        "Home Uploads": "aktiv",
        "Affirmationen": "aktiv",
        "Workbooks": "aktiv",
        "Meditationen": "aktiv",
        "KI-Module (geplant)": "in Arbeit"
    }

    st.write(f"**Studio-Version:** 1.0 (2025-06-04)")

    for mod_name, status in modules.items():
        if status == "aktiv":
            st.markdown(f"- {mod_name} <span class='status-active'>● Aktiv</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"- {mod_name} <span class='status-inprogress'>● In Arbeit</span>", unsafe_allow_html=True)

    st.markdown("---")
    st.write("Klicke im Menü links, um zu den Modulen zu wechseln.")

elif menu == "KI-Module":

    st.subheader("🤖 KI Affirmations-Generator")

    prompt = st.text_area("Gib ein Thema oder Stichwort ein, zu dem Du Affirmationen möchtest:")

    if st.button("Affirmationen generieren"):
        if prompt.strip() == "":
            st.warning("Bitte gib ein Thema oder Stichwort ein.")
        else:
            # Simulierter KI-Output (hier später echte KI-Integration)
            affirmations = [
                f"Ich bin voller Kraft und {prompt}.",
                f"Mein Herz öffnet sich für {prompt} und Liebe.",
                f"Jeden Tag werde ich stärker in {prompt}.",
                f"Ich erlaube mir, {prompt} zu empfangen und zu geben."
            ]

            st.markdown("### Deine generierten Affirmationen:")
            for aff in affirmations:
                st.write(f"- {aff}")

            # Download der Affirmationen als Textdatei
            affirm_text = "\n".join(affirmations)
            st.download_button(
                label="Affirmationen als Text herunterladen",
                data=affirm_text,
                file_name=f"affirmationen_{prompt.replace(' ', '_')}.txt",
                mime="text/plain"
            )

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:#C0A98E;'>© 2025 Samarah Creator Studio ✨</p>", unsafe_allow_html=True)
