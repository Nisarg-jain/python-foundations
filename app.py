# ==============================================================================
# 1. SEQUENCE UNPACKING (Destructuring Pattern)
# ==============================================================================
point_3d = (100, 250, 45)

# Pythonic unpacking - avoids repetitive manual indexing
pos_x, pos_y, pos_z = point_3d
print(f"Coordinates: X={pos_x}, Y={pos_y}, Z={pos_z}")


# ==============================================================================
# 2. DICTIONARY LOOKUPS & DEFENSIVE ACCESS (O(1) Hash Map)
# ==============================================================================
user_profile = {
    "username": "dev_engineer",
    "role": "admin",
    "login_count": 42
}

# Defensive retrieval: prevents unhandled KeyError exceptions
contact_email = user_profile.get("email", "support@system.local")
access_level = user_profile.get("role", "guest")

print(f"User: {user_profile['username']} | Role: {access_level} | Contact: {contact_email}")


# ==============================================================================
# 3. TEXT TOKENIZATION & MAPPING (Emoji Converter Engine)
# ==============================================================================
def parse_emojis(sentence: str) -> str:
    """Tokenizes an input string and maps symbolic text tokens to emojis."""
    emoji_mapping = {
        ":)": "😊",
        ":(": "🙁",
        ";)": "😉",
        "<3": "❤️️"
    }
    
    tokens = sentence.strip().split(" ")
    transformed_tokens = [emoji_mapping.get(token, token) for token in tokens]
    return " ".join(transformed_tokens)


sample_message = "Good morning :) I hope you have a great day <3"
parsed_message = parse_emojis(sample_message)
print(f"\nOriginal: {sample_message}")
print(f"Parsed:   {parsed_message}")


# ==============================================================================
# 4. MODULAR FUNCTIONS & STACK ISOLATION
# ==============================================================================
def display_system_status(service_name: str, is_active: bool) -> None:
    """Prints a formatted health status message for a given service."""
    status_indicator = "ONLINE" if is_active else "OFFLINE"
    print(f"[STATUS] Service '{service_name}' is currently {status_indicator}.")


print("\n--- System Diagnostics ---")
display_system_status("Database", True)
display_system_status("PaymentGateway", False)