import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np
from llama_utils import generate_llama_explanation
from blockchain.blockchain_utils import add_record, get_records_count

st.subheader("Ανέβασε μια εικόνα για ανίχνευση")

# Φόρτωση μοντέλου ΜΙΑ φορά
@st.cache_resource
def load_model():
    return YOLO("runs/detect/train/weights/best.pt")

model = load_model()

# Συνάρτηση έξω από το if
def detect_weeds(image):
    results = model(image)
    return results

# Upload
uploaded_file = st.file_uploader("📸 Ανέβασε μια εικόνα", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="📷 Εικόνα", use_container_width=True)

    img_array = np.array(image)

    results = detect_weeds(img_array)
    result_img = results[0].plot()

    st.image(result_img, caption="🧠 YOLO Detection", use_container_width=True)

    boxes = results[0].boxes

    classes = boxes.cls.tolist()

    weed_count = classes.count(1)  # 1 = Weed
    crop_count = classes.count(0)  # 0 = Crop

    st.write(f"🌱 Crops: {crop_count}")
    st.write(f"🌿 Weeds: {weed_count}")
    if weed_count > 2:
        decision = "⚠️ High weed presence - Apply herbicide"
    else:
        decision = "✅ Low weed presence - No action needed"

    st.subheader("📊 Decision")
    st.write(decision)

    if st.button("🤖 Generate LLaMA Explanation"):
        with st.spinner("Το LLaMA δημιουργεί επεξήγηση..."):
            explanation = generate_llama_explanation(crop_count, weed_count, decision)

        st.subheader("🧠 LLaMA Explanation")
        st.write(explanation)

    if st.button("🔗 Store decision on Blockchain"):

        tx_hash = add_record(
            uploaded_file.name,
            crop_count,
            weed_count,
            decision,
            explanation
        )

        st.success(f"Stored on blockchain ✅")
        st.code(tx_hash)
else:
    st.info("Περίμενω να ανεβάσεις μια εικόνα...")

