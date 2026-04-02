import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("model/sms_model.pkl")
columns = joblib.load("model/columns.pkl")

st.set_page_config(page_title="SMS Delivery Predictor", layout="centered")

st.title("📩 SMS Delivery Prediction System")
# Load feature importances (add this once, after loading model)
try:
    importances = joblib.load("model/feature_importances.pkl")  # we'll save it
    st.sidebar.subheader("🔍 Top Feature Importance")
    imp_df = pd.DataFrame({
        "Feature": list(importances.keys()),
        "Importance": list(importances.values())
    }).sort_values("Importance", ascending=False).head(8)
    
    st.sidebar.bar_chart(imp_df.set_index("Feature"))
except:
    pass
st.write("Predict whether your SMS will be delivered successfully.")

# -------------------------------
# INPUT SECTION
# -------------------------------

# Message input option
option = st.radio(
    "Choose message input method:",
    ["Type Message", "Select Length"]
)

if option == "Type Message":
    message_text = st.text_area("Enter SMS Message")

    message_length = len(message_text)
    st.write(f"📏 Message Length: {message_length}")

    if message_length == 0:
        st.warning("Please enter a message!")

else:
    message_length = st.slider("Message Length", 50, 300, 120)

# SMS splitting info
# if message_length > 160:
#     parts = message_length // 160 + 1
#     st.info(f"⚠️ Message will be split into {parts} parts")

# Other inputs
country = st.selectbox("Country", ["IN", "US", "UK"])
operator = st.selectbox("Operator", ["airtel", "vodafone", "jio", "verizon"])
sender = st.selectbox("Sender", ["BANKTX", "SHOPPY", "PAYAPP"])
route = st.selectbox("Route", ["domestic", "intl"])
time = st.selectbox("Time of Day", ["morning", "afternoon", "evening", "night"])
campaign = st.selectbox("Campaign Type", ["otp", "promo", "alert"])

historical_rate = st.slider("Historical Delivery Rate", 0.5, 1.0, 0.8)
previous_failures = st.slider("Previous Failures", 0, 5, 1)

# -------------------------------
# ENCODING FUNCTION
# -------------------------------

def encode_input():
    input_data = {
        "message_length": message_length,
        "historical_delivery_rate": historical_rate,
        "previous_failures": previous_failures
    }

    df = pd.DataFrame([input_data])

    # Initialize all columns
    for col in columns:
        if col not in df.columns:
            df[col] = 0

    # Set categorical values
    mapping = {
        f"country_{country}": 1,
        f"operator_{operator}": 1,
        f"sender_id_{sender}": 1,
        f"route_{route}": 1,
        f"time_of_day_{time}": 1,
        f"campaign_type_{campaign}": 1
    }

    for key in mapping:
        if key in df.columns:
            df[key] = 1

    # Ensure correct order
    df = df[columns]

    return df

# -------------------------------
# PREDICTION
# -------------------------------

if st.button("🚀 Predict Delivery"):

    # Handle empty message case
    if option == "Type Message" and message_length == 0:
        st.error("Please enter a message before predicting.")
    else:
        input_df = encode_input()

        prob = model.predict_proba(input_df)[0][1]
        print(f"Predicted Probability: {prob:.2f}")
        st.subheader("📊 Prediction Result")

        if prob > 0.5:
            st.success(f"✅ Delivered (Probability: {prob:.2f})")
        else:
            st.error(f"❌ Failed (Probability: {prob:.2f})")

        # Confidence indicator
        st.progress(int(prob * 100))

        # Insight
        if prob < 0.4:
            st.warning("⚠️ High risk of failure. Consider improving message routing or content.")
        elif prob > 0.7:
            st.info("👍 High likelihood of successful delivery.")