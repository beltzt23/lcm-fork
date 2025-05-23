import sys
import re

# Supported types for each target language
SUPPORTED_LANGUAGES = {
    'c': {'int8_t', 'int16_t', 'int32_t', 'int64_t', 'float', 'double', 'string', 'boolean', 'byte'},
    'java': {'int8_t', 'int16_t', 'int32_t', 'int64_t', 'float', 'double', 'string', 'boolean'},
    'python': {'int8_t', 'int16_t', 'int32_t', 'int64_t', 'float', 'double', 'string', 'boolean', 'byte'}
}

def validate_lcm_file(filename, language):
    with open(filename) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()

            # Skip comments and structural lines
            if not line or line.startswith("//"):
                continue
            if line.startswith("package") or line.startswith("struct") or line == "}":
                continue

            # Match a line like: type name; or type name[...];
            match = re.match(r'^(\w+)\s+\w+(\[.*\])?;$', line)
            if match:
                lcm_type = match.group(1)

                # Validate against selected or all languages
                if language == 'all':
                    for lang, allowed in SUPPORTED_LANGUAGES.items():
                        if lcm_type not in allowed:
                            print(f"❌ ERROR: Type '{lcm_type}' not supported in {lang.upper()} (line {line_num})")
                            sys.exit(1)
                else:
                    allowed_types = SUPPORTED_LANGUAGES.get(language.lower())
                    if not allowed_types:
                        print(f"❌ ERROR: Unknown language '{language}'. Supported: {', '.join(SUPPORTED_LANGUAGES.keys())}")
                        sys.exit(1)
                    if lcm_type not in allowed_types:
                        print(f"❌ ERROR: Type '{lcm_type}' not supported in {language.upper()} (line {line_num})")
                        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_lcm.py <file.lcm> [language]")
        print("Example: python validate_lcm.py example.lcm java")
        print("         python validate_lcm.py example.lcm all")
        sys.exit(1)

    file_to_check = sys.argv[1]
    lang = sys.argv[2] if len(sys.argv) > 2 else 'all'

    validate_lcm_file(file_to_check, lang)
    print(f"✅ LCM type validation passed for {file_to_check} using language '{lang}'.")
