import streamlit as st
import os

# Design V1.0 Update Test

# Farb- und Stildefinition
st.set_page_config(page_title="Samarah Creator Studio", page_icon="🌸", layout="centered")

# Lichtvoller Header
st.markdown(
    """
    <div style='background-color:#FDF6EC; padding:20px; border-radius:15px; box-shadow: 0px 0px 10px #FAD9C4;'>
        <h1 style='color:#D49494; text-align:center;'>🌸 Samarah Creator Studio – Media Center 🌸</h1>
        <p style='color:#7B5E57; text-align:center; font-size:18px;'>Erstelle, lade hoch & verwalte Deine spirituellen Inhalte mit Leichtigkeit und Freude</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Ordner für Uploads
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Upload-Modul
st.markdown("---")
st.subheader("✨ Datei-Upload")

uploaded_file = st.file_uploader("Bitte wähle eine Datei zum Hochladen:", type=["png", "jpg", "pdf", "zip"])

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Datei '{uploaded_file.name}' erfolgreich hochgeladen!")

# Download-Modul
st.markdown("---")
st.subheader("📂 Deine hochgeladenen Dateien")

files = os.listdir(UPLOAD_FOLDER)
if files:
    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file)
        with open(file_path, "rb") as f:
            st.download_button(
                label=f"⬇️ {file}",
                data=f,
                file_name=file,
                mime="application/octet-stream"
            )
else:
    st.write("🕊️ Noch keine Dateien hochgeladen.")

# Lichtvoller Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:#C0A98E;'>© 2025 Samarah Creator Studio ✨</p>",
    unsafe_allow_html=True
)
