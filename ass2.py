# water_reminder.py

def calculate_water_intake(weight, age):
    intake = round(weight * 0.033, 2)

    if age < 18:
        interval = 1.5
    elif age <= 55:
        interval = 2
    else:
        interval = 2.5

    return intake, interval

def main():
    try:
        weight = float(input("Enter your weight in kg: "))
        age = int(input("Enter your age: "))

        if weight <= 0 or age <= 0:
            raise ValueError("Weight and age must be positive numbers.")

        intake, interval = calculate_water_intake(weight, age)

        print(f"\n✅ Recommended daily water intake: {intake} liters.")
        print(f"🔔 Reminder every {interval} hours.")

    except ValueError as e:
        print(f"⚠️ Input error: {e}")

if __name__ == "__main__":
    main()
