import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler


def load_data(path):
    return pd.read_csv(path)


# ✅ FIXED DATE HANDLING
def process_date(df):
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors='coerce')

    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day

    df.drop("date", axis=1, inplace=True)
    return df


def perform_eda(df):
    print("\n===== DATA INFO =====")
    print(df.info())

    print("\n===== MISSING VALUES =====")
    print(df.isnull().sum())

    print("\n===== DESCRIPTION =====")
    print(df.describe())

    if "sales_revenue" in df.columns:
        print("\n===== CORRELATION WITH TARGET =====")
        print(df.corr(numeric_only=True)["sales_revenue"].sort_values(ascending=False))


def preprocess_data(df):

    df = df.copy()

    # Drop ID
    df.drop("id", axis=1, inplace=True)

    # Process date
    df = process_date(df)

    # Handle missing values
    df.fillna(df.median(numeric_only=True), inplace=True)

    # One-hot encoding
    df = pd.get_dummies(df, columns=[
        "region", "channel", "product_category", "customer_segment"
    ], drop_first=True)

    return df


def split_features_target(df):
    X = df.drop("sales_revenue", axis=1)
    y = df["sales_revenue"]
    return X, y


def scale_features(X, is_train=True):

    if is_train:
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        joblib.dump(scaler, "model/scaler.pkl")
    else:
        scaler = joblib.load("model/scaler.pkl")
        X_scaled = scaler.transform(X)

    return X_scaled