from exlcm.example_t import example_t  # Correct import

def main():
    msg = example_t()

    # Intentionally try valid or invalid values here
    msg.timestamp = 1234567890
    msg.position = [1.0, 2.0]         # Try changing this to [1.0, 2.0] to test failure
    msg.orientation = [0.0, 0.0, 0.0, 1.0]
    msg.num_ranges = 3
    msg.ranges = [100, 200]          # Try [100, 200] to trigger struct error
    msg.name = "SensorA"
    msg.enabled = "True"                    # Try "True" (string) to test type error

    # ✅ Wrap encoding in try/except block
    try:
        encoded = msg.encode()
    except Exception as e:
        print(f" Message failed to encode: {e}")
        return

    print(" Message encoded successfully")
    print("Encoded message (hex):", encoded.hex())

    # Decode to test round-trip integrity
    decoded = example_t.decode(encoded)
    print("\nDecoded:")
    print(f"  Timestamp: {decoded.timestamp}")
    print(f"  Position: {decoded.position}")
    print(f"  Orientation: {decoded.orientation}")
    print(f"  Num Ranges: {decoded.num_ranges}")
    print(f"  Ranges: {decoded.ranges}")
    print(f"  Name: {decoded.name}")
    print(f"  Enabled: {decoded.enabled}")

if __name__ == "__main__":
    main()
