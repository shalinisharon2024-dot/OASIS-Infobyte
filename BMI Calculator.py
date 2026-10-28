"""
Oasis Infobyte Python Programming Internship
Task: BMI Calculator
Description: Computes Body Mass Index (BMI) given weight and height, 
providing exact metric categorizations and health advisories.
"""

def get_valid_float(prompt: str) -> float:
    """Helper function to continuously prompt user until a valid positive float is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Error: Value must be greater than zero. Please try again.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a valid numerical value.")

def calculate_bmi():
    print("=" * 45)
    print("      HEALTH METRIC: BMI CALCULATOR     ")
    print("=" * 45)
    
    # User input collection with validation
    weight = get_valid_float("Enter your weight in kilograms (kg): ")
    height = get_valid_float("Enter your height in meters (e.g., 1.75): ")
    
    # BMI formula: weight (kg) / [height (m)]^2
    bmi = weight / (height ** 2)
    
    # Determine category based on standard WHO thresholds
    if bmi < 18.5:
        category = "Underweight"
        advice = "Focus on nutrient-dense foods and caloric surplus."
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
        advice = "Great job! Maintain your balanced lifestyle."
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        advice = "Consider incorporating regular physical activity and a balanced diet."
    else:
        category = "Obese"
        advice = "Consult a healthcare professional for personalized guidance."

    print("\n" + "-" * 45)
    print(f"📊 RESULTS SUMMARY:")
    print(f"   • Calculated BMI : {bmi:.2f}")
    print(f"   • Health Status  : {category}")
    print(f"   • Recommendation : {advice}")
    print("-" * 45)

if __name__ == "__main__":
    calculate_bmi()