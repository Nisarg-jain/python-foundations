"""Reusable string transformation module for emoji parsing."""

def convert_emojis(message: str) -> str:
    """Transforms symbolic text emoticons into Unicode emoji representations.

    Takes a raw string, isolates whitespace-delimited tokens, and maps
    known emoticon keys to their respective Unicode characters.
    """
    emoji_mapping = {
        ":)": "😊",
        ":(": "🙁",
        ";)": "😉",
        "<3": "❤️️"
    }

    tokens = message.split(" ")
    translated_tokens = [emoji_mapping.get(token, token) for token in tokens]
    return " ".join(translated_tokens)


# --- Driver Code (I/O decoupled from transformation logic) ---
user_input = input("> ")
result = convert_emojis(user_input)
print(result)