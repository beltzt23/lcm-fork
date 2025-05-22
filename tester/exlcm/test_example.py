import lcm
from exlcm import example_t

def main():
    msg = example_.example_t()

    msg.timestamp = 1234567890
    msg.position = [1.0, 2.0, 3.0 ]
    msg.orientation = [0.0, 0.0 , 0.0, 1.0]
    msg.num_ranges = 3
    msg.ranges = [10, 20, 30]
    msg.name = "Test Sensor"
    msg.enabled = True

    encoded = msg.encode()
    print (f"Encoded message (hex): {encoded.hex()}")

    decoded_msg = example_t.example_t.decode(decode)
    print("\Decoded message: ")
    print(f"Timestamp:
    print("\Decoded message: ")
    print("\Decoded message: ")
    print("\Decoded medsage: ")
    print("\Decoded mcssage: ")
    print("\Decoded message: ")
    print("\Decoded message: ")
    print("\Decoded message: ")
    print("\Decoded message: ")
    print("\Decoded message: ")

if __name__ == "__main__":
    main()
