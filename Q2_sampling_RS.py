from stream_generator import generate_stock_price
from datasketches import ebpps_sketch

def sample_stock_prices(num_samples=1000, sketch_size=256):
    sketch = ebpps_sketch(sketch_size)
    stream = generate_stock_price()
    values_for_moment_analysis = []

    print(f"\n📈 Starting stock price stream and sampling with EBPPS...")
    for i in range(num_samples):
        price = next(stream)
        print(f"[Price {i+1}] ➜ ${price:.2f}")
        sketch.update(price, 1.0)
        values_for_moment_analysis.append(price)

    print("\n✅ Reservoir Sampling via ebpps_sketch completed.")
    print(f"************************Total samples collected: {len(values_for_moment_analysis)} ************************")
   
    return values_for_moment_analysis
