import pandas as pd

# Load processed India dataset
df = pd.read_csv("data/processed/india_gtd.csv")

selected_columns = [
    "iyear",
    "imonth",
    "iday",
    "provstate",
    "city",
    "attacktype1_txt",
    "targtype1_txt",
    "weaptype1_txt",
    "gname",
    "success",
    "nkill",
    "nwound"
]

model_df = df[selected_columns].copy()

# Fill missing values
model_df["nkill"] = model_df["nkill"].fillna(0)
model_df["nwound"] = model_df["nwound"].fillna(0)

# Create severity score
model_df["severity_score"] = (
    model_df["nkill"] * 2 + model_df["nwound"]
)

# Save engineered dataset
model_df.to_csv(
    "data/features/model_features.csv",
    index=False
)

print(model_df.shape)
print("Feature engineering completed!")
