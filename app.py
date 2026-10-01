"""Robust user input validation and ratio calculation engine."""

def calculate_risk_ratio() -> None:
    """Calculates risk factor by dividing fixed income by validated age.

    Safely handles invalid literal conversions and division by zero.
    """
    base_income = 50_000

    try:
        raw_age = input("Enter age: ")
        age = int(raw_age)

        risk_ratio = base_income / age
        print(f"Calculated Risk Ratio: {risk_ratio:.2f}")

    except ValueError:
        # Triggered when int() fails to parse non-numeric strings
        print("Error: Input must be a valid integer literal.")

    except ZeroDivisionError:
        # Defensive check against division by zero in financial formulas
        print("Error: Age cannot be zero.")


if __name__ == "__main__":
    calculate_risk_ratio()