#!/usr/bin/env python
import argparse
import warnings

from personal_agent.crew import PersonalAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew with CLI input for meal inspiration.
    """
    parser = argparse.ArgumentParser(
        description="Personal Agent - Meal Planning and Grocery List Generator"
    )
    parser.add_argument(
        "inspiration",
        nargs="?",
        default="Want to eat noodles. Want one meal to eat fish. Want a tomato and eggs. Less sugar, less sauce.",
        help="Meal inspiration input, e.g.: 'Want to eat noodles.'",
    )

    args = parser.parse_args()

    inputs = {"inspiration": args.inspiration}

    print(f"🍽️  Meal Inspiration: {args.inspiration}")
    print("🚀 Starting to generate 3-day meal plan and grocery list...")
    print("-" * 50)

    try:
        PersonalAgent().crew().kickoff(inputs=inputs)
        print("-" * 50)
        print("✅ Complete! Please check the following files:")
        print("📄 meal_plan.md - 3-day meal plan")
        print("🛒 grocery_list.md - grocery list")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()
