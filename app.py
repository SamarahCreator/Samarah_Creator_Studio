import streamlit as st
import os

# Titelbereich
st.title("🌸 Samarah Creator Studio – Media Center V1.0")

# Ordner für Uploads
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Upload-Modul
uploaded_file = st.file_uploader("Wähle eine Datei zum Hochladen", type=["png", "jpg", "pdf", "zip"])

if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ Datei '{uploaded_file.name}' erfolgreich hochgeladen!")

# Download-Modul
st.header("📂 Deine hochgeladenen Dateien:")

files = os.listdir(UPLOAD_FOLDER)
if files:
    for file in files:
        file_path = os.path.join(UPLOAD_FOLDER, file)
        with open(file_path, "rb") as f:
            st.download_button(
                label=f"⬇️ Download {file}",
                data=f,
                file_name=file
            )
else:
    st.write("Noch keine Dateien vorhanden.")
