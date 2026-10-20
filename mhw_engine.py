import numpy as np
import pandas as pd

def process_mhw(csv_path_or_df):
    if isinstance(csv_path_or_df, str):
        df = pd.read_csv(csv_path_or_df)
    else:
        df = csv_path_or_df.copy()

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["doy"] = df["timestamp"].dt.dayofyear

    climatology = []
    for doy in range(1, 367):
        window = df[df["doy"].between(max(1, doy - 15), min(366, doy + 15))]
        if not window.empty and len(window) > 1:
            mean_val = window["temp"].mean()
            p90_val = np.percentile(window["temp"].dropna(), 90)
        else:
            mean_val = df["temp"].mean()
            p90_val = df["temp"].mean() + 1.0
        climatology.append({"doy": doy, "seas": mean_val, "thresh": p90_val})

    clim_df = pd.DataFrame(climatology)
    clim_df["seas"] = clim_df["seas"].rolling(15, min_periods=1, center=True).mean()
    clim_df["thresh"] = clim_df["thresh"].rolling(15, min_periods=1, center=True).mean()

    merged = pd.merge(df, clim_df, on="doy", how="left")
    merged["anomaly"] = merged["temp"] - merged["seas"]
    merged["diff_thresh"] = np.maximum(merged["thresh"] - merged["seas"], 0.1)

    merged["mhw_category"] = "No MHW"
    is_mhw = merged["temp"] > merged["thresh"]

    c1 = is_mhw & (merged["anomaly"] < 2 * merged["diff_thresh"])
    c2 = is_mhw & (merged["anomaly"] >= 2 * merged["diff_thresh"]) & (merged["anomaly"] < 3 * merged["diff_thresh"])
    c3 = is_mhw & (merged["anomaly"] >= 3 * merged["diff_thresh"])

    merged.loc[c1, "mhw_category"] = "Category I (Moderate)"
    merged.loc[c2, "mhw_category"] = "Category II (Strong)"
    merged.loc[c3, "mhw_category"] = "Category III (Severe)"

    return merged
