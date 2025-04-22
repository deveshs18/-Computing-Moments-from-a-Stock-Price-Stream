def check_alerts(mean, variance, skewness, kurtosis):
    if mean is None:
        print("[CRITICAL] No data available to analyze.")
        return

    if variance > 150:
        print("[CRITICAL] High variance: Prices are changing rapidly.")
    elif variance < 10:
        print("[INFO] Low variance: Very little price movement.")
    else:
        print("[INFO] Variance is moderate: Normal market fluctuation.")

    if abs(skewness) > 2:
        print("[WARNING] Unusual skewness: The price trend is uneven, indicating abnormal behavior.")
    elif abs(skewness) < 0.5:
        print("[INFO] Skewness is low: Prices are symmetrically distributed.")
    else:
        print("[INFO] Skewness is moderate: Slight trend in price direction.")

    if kurtosis > 1000:
        print("[CRITICAL] High kurtosis: There are extreme prices in the data, be cautious.")
    elif 100 < kurtosis <= 1000:
        print("[WARNING] Moderate kurtosis: Occasional large movements exist.")
    else:
        print("[INFO] Low kurtosis: Prices are distributed normally without extreme values.")

# For testing
if __name__ == "__main__":
    check_alerts(mean=100, variance=160, skewness=2.5, kurtosis=1200)
