import streamlit as st
import pandas as pd
import joblib

# ---------------- LOAD MODEL ----------------
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

st.set_page_config(page_title="Marketing Sales Revenue Predictor")

st.title("📊 Marketing Sales Revenue Prediction")
st.caption("Enter realistic marketing values only")

st.warning("⚠️ This model only works for realistic business data")

# ---------------- FORM ----------------
with st.form("form"):

    # -------- CATEGORICAL --------
    region = st.selectbox("Region", ["Select","North","South","East","West"])
    channel = st.selectbox("Marketing Channel", ["Select","Online","Offline"])
    product = st.selectbox("Product Category", ["Select","A","B","C"])
    segment = st.selectbox("Customer Segment", ["Select","Low","Medium","High"])

    st.subheader("📈 Marketing Metrics")

    # -------- STRICT INPUTS --------
    ad_spend = st.number_input("Ad Spend", min_value=5.0, max_value=100.0, value=10.0)
    price = st.number_input("Price", min_value=1.0, max_value=50.0, value=5.0)
    impressions = st.number_input("Impressions", min_value=500.0, max_value=10000.0, value=2000.0)
    market_reach = st.number_input("Market Reach", min_value=100.0, max_value=5000.0, value=1000.0)
    ctr = st.slider("Click Through Rate", 0.01, 1.0, 0.05)
    discount = st.slider("Discount Rate", 0.0, 1.0, 0.1)
    competition = st.slider("Competition Index", 0.0, 1.0, 0.3)
    seasonality = st.slider("Seasonality Index", 0.1, 2.0, 1.0)
    days = st.number_input("Campaign Duration", min_value=1, max_value=90, value=30)
    clv = st.number_input("Customer Lifetime Value", min_value=1000.0, max_value=50000.0, value=5000.0)

    date = st.date_input("Select Date")

    submit = st.form_submit_button("Predict")

# ---------------- VALIDATION ----------------
if submit:

    if "Select" in [region, channel, product, segment]:
        st.error("❌ Select all dropdown values")
        st.stop()

    # 🚫 HARD STOP (THIS FIXES YOUR ISSUE)
    if ad_spend < 5 or impressions < 500 or clv < 1000:
        st.error("❌ Invalid unrealistic inputs — prediction blocked")
        st.stop()

    # ---------------- PROCESS ----------------
    year = date.year
    month = date.month
    day = date.day

    data = {
        "ad_spend": ad_spend,
        "price": price,
        "discount_rate": discount,
        "market_reach": market_reach,
        "impressions": impressions,
        "click_through_rate": ctr,
        "competition_index": competition,
        "seasonality_index": seasonality,
        "campaign_duration_days": days,
        "customer_lifetime_value": clv,
        "year": year,
        "month": month,
        "day": day,
        "region": region,
        "channel": channel,
        "product_category": product,
        "customer_segment": segment
    }

    df = pd.DataFrame([data])
    df = pd.get_dummies(df)
    df = df.reindex(columns=columns, fill_value=0)

    scaled = scaler.transform(df)
    pred = model.predict(scaled)[0]

    # ---------------- OUTPUT ----------------
    st.success(f"💰 Revenue: ₹ {pred:.2f}")

    if pred < 110:
        st.error("Low performance")
    elif pred < 150:
        st.warning("Average performance")
    else:
        st.success("High performance")
