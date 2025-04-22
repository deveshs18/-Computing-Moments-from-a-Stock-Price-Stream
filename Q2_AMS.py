def compute_moments(data):
    n = len(data)
    if n == 0:
        return None, None, None, None

    mean = sum(data) / n
    variance = sum((x - mean)**2 for x in data) / n
    skewness = sum((x - mean)**3 for x in data) / n
    kurtosis = sum((x - mean)**4 for x in data) / n

    return mean, variance, skewness, kurtosis

# For testing
if __name__ == "__main__":
    sample_data = [100, 105, 95, 110, 90, 120]
    mean, var, skew, kurt = compute_moments(sample_data)
    print(f"Mean: {mean:.2f}, Variance: {var:.2f}, Skewness: {skew:.2f}, Kurtosis: {kurt:.2f}")
