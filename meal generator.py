import random
import pandas as pd

# Sample meal database
meal_database = {
    'Breakfast': [
        {'Meal': 'Oatmeal with Fruits', 'Calories': 300, 'Type': 'Vegetarian'},
        {'Meal': 'Egg and Avocado Toast', 'Calories': 350, 'Type': 'Non-Vegetarian'},
        {'Meal': 'Smoothie Bowl', 'Calories': 400, 'Type': 'Vegan'},
        {'Meal': 'Pancakes with Syrup', 'Calories': 500, 'Type': 'Vegetarian'}
    ],
    'Lunch': [
        {'Meal': 'Grilled Chicken Salad', 'Calories': 400, 'Type': 'Non-Vegetarian'},
        {'Meal': 'Vegetable Stir Fry with Rice', 'Calories': 450, 'Type': 'Vegan'},
        {'Meal': 'Paneer Curry with Roti', 'Calories': 500, 'Type': 'Vegetarian'},
        {'Meal': 'Beef Steak with Vegetables', 'Calories': 600, 'Type': 'Non-Vegetarian'}
    ],
    'Dinner': [
        {'Meal': 'Salmon with Quinoa', 'Calories': 500, 'Type': 'Non-Vegetarian'},
        {'Meal': 'Lentil Soup with Bread', 'Calories': 350, 'Type': 'Vegan'},
        {'Meal': 'Vegetable Pasta', 'Calories': 400, 'Type': 'Vegetarian'},
        {'Meal': 'Chicken Wrap', 'Calories': 450, 'Type': 'Non-Vegetarian'}
    ]
}

# Function to generate a meal plan
def generate_meal_plan(preferences, caloric_goal):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meal_plan = {}

    for day in days:
        daily_meals = []
        total_calories = 0
        
        for meal_time, meals in meal_database.items():
            filtered_meals = [meal for meal in meals if preferences in meal['Type']]
            selected_meal = random.choice(filtered_meals)
            daily_meals.append({meal_time: selected_meal})
            total_calories += selected_meal['Calories']
        
        meal_plan[day] = {'Meals': daily_meals, 'Total Calories': total_calories}
    
    # Adjust the caloric goal feedback
    if total_calories < caloric_goal - 100:
        feedback = "Your plan is slightly below your caloric goal. Consider adding snacks."
    elif total_calories > caloric_goal + 100:
        feedback = "Your plan is slightly more needed snacks adjust daily category"

        feedback = "Your plan is slightly above your caloric goal. Consider reducing portion sizes or skipping snacks."
    else:
        feedback = "Your plan is balanced with your caloric goal."

    return meal_plan, feedback


# Get user input
print("=== Personalized Meal Planner ===")
diet_preference = input("Enter your dietary preference (Vegetarian, Vegan, Non-Vegetarian): ").strip().capitalize()
caloric_goal = int(input("Enter your daily caloric goal: "))

# Generate the meal plan
meal_plan, feedback = generate_meal_plan(diet_preference, caloric_goal)

# Display the meal plan
print("\n=== Weekly Meal Plan ===")
for day, details in meal_plan.items():
    print(f"\n{day}:")
    for meal in details['Meals']:
        for meal_time, info in meal.items():
            print(f"  {meal_time}: {info['Meal']} ({info['Calories']} Calories)")
    print(f"  Total Calories: {details['Total Calories']}")

# Provide feedback
print("\n=== Feedback ===")
print(feedback)

