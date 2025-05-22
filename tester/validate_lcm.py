import sys
import re

ALLOWED_TYPES = {
    'int8_t' , 'int16_t', 'int32_t', 'int64_t', 'float',
    'double', 'string', 'boolean', 'byte'
}

def validate_lcm_file(filename):
    with open(filename) as f:

        for line_num, line in enumerate(f,1):
            line = line.strip()

            if not line or line.startswith("//"):
                continue
            match = re.match(r'(\w+)\s+\w+(\[.*\])?;', line)

            if match:
                lcm_type = match.group(1)
                if lcm_type not in ALLOWED_TYPES:
                    print(f"ERROR: Unsupported type '{lcm_type} at line {line_num} in {filename}")
                    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_lcm.py <file.lcm>")
        sys.exit(1)
    validate_lcm_file(sys.argv[1])
    print("LCM type validation passed.")