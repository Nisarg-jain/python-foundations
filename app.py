# ==============================================================================
# 1. UPGRADED GUESSING GAME (Crash-proof, Boundary-checked, while-else)
# ==============================================================================
SECRET_NUMBER = 9
GUESS_LIMIT = 3
guess_count = 0

print("--- Guessing Game Started (Range: 1-10) ---")

while guess_count < GUESS_LIMIT:
    raw_input = input("Enter your guess: ").strip()

    # Defensive check: ensure input is an integer before casting
    if not raw_input.isdigit():
        print("Invalid input! Please enter a positive integer.")
        continue  # Do not penalize guess count on malformed input

    guess = int(raw_input)
    guess_count += 1

    if guess == SECRET_NUMBER:
        print(f"Brilliant! You guessed it in {guess_count} attempt(s)!\n")
        break
else:
    # Executes only if the while loop terminates via condition (guess_count == GUESS_LIMIT)
    print(f"Game Over! You exhausted all {GUESS_LIMIT} attempts. Secret was {SECRET_NUMBER}.\n")


# ==============================================================================
# 2. UPGRADED CAR ENGINE (Finite State Machine pattern, Sanitized Input)
# ==============================================================================
print("--- Car CLI Engine Initialized. Type 'help' for commands. ---")

is_car_running = False

while True:
    # Single-point sanitization: strip surrounding whitespace and lowercase
    command = input("> ").strip().lower()

    if command == "start":
        if is_car_running:
            print("Warning: Engine is already idling! Cannot start again.")
        else:
            is_car_running = True
            print("Engine ignited... Ready to drive.")

    elif command == "stop":
        if not is_car_running:
            print("Warning: Car is already at a dead stop.")
        else:
            is_car_running = False
            print("Engine shut off. Handbrake engaged.")

    elif command == "help":
        print("""
Supported Commands:
  start - Fire up the car engine
  stop  - Turn off the engine
  quit  - Exit the CLI simulator
        """)

    elif command == "quit":
        print("Exiting simulator. Safe travels!")
        break

    else:
        print(f"Unknown command: '{command}'. Type 'help' for valid actions.")