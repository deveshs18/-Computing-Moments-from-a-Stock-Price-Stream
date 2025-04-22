from sampling_RS import sample_stock_prices
from AMS import compute_moments
from alert import check_alerts
import matplotlib.pyplot as plt

def plot_moments(mean, variance, skewness, kurtosis):
    import matplotlib.pyplot as plt

    moments = ['Mean', 'Variance', 'Skewness', 'Kurtosis']
    values = [mean, variance, skewness, kurtosis]

    plt.figure(figsize=(8, 4))
    plt.bar(moments, values)
    plt.yscale('log')  # ✅ Fix: log scale
    plt.title("Statistical Moments of Sampled Stock Prices (Log Scale)")
    plt.ylabel("Log-scaled Value")
    plt.grid(True, axis='y', which='both', linestyle='--')
    plt.tight_layout()
    plt.savefig("moment_plot_log.png")
    plt.show()

# Run the full pipeline
if __name__ == "__main__":
    print("Sampling stock prices...")
    sample = sample_stock_prices(1000)

    print(f"\n Sample size: {len(sample)}")
    print(f" First 10 sampled prices: {sample[:10]}")

    print("\n************** Computing moments from sample...**************")
    mean, variance, skewness, kurtosis = compute_moments(sample)

    print(f"\nMean: {mean:.2f}\nVariance: {variance:.2f}\nSkewness: {skewness:.2f}\nKurtosis: {kurtosis:.2f}")

    print("\n***************** Checking for alerts...****************")
    print("Alerts based on computed moments:")
    check_alerts(mean, variance, skewness, kurtosis)

    print("\n📊 Plotting statistical moments...")
    plot_moments(mean, variance, skewness, kurtosis)
