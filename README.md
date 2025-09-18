# PersonalAgent - Meal Planning Assistant

As someone who loves grocery shopping and cooking, I wanted to create an AI agent that could represent my passion for meal planning and food preparation.

## What This Project Does

This project takes your fragmented food inspirations as input and creates a nutritionally balanced daily meal plan, then generates an organized shopping list. Simply provide some food hints or preferences, and the system will first create a complete day's menu with balanced nutrition, then produce a shopping list for all the ingredients needed.

#### Input

Provide fragmented food inspirations or hints, such as:
- "Want one meal fish and one meal noodles"
- "Want healthy meals with chicken and vegetables"
- "Want to try Asian cuisine today"

#### Output

The system works in two steps:
1. **Creates a nutritionally balanced daily meal plan** - `meal_plan.md` with complete breakfast, lunch, dinner, and optional snack
2. **Generates an organized shopping list** - `grocery_list.md` with all ingredients grouped by categories

## Example

For input "Want one meal fish and one meal noodles", the system generates `meal_plan.md` and `grocery_list.md` in the root folder. Feel free to check them out. The input is conducted using CLI. My command is:
```bash
uv run python src/personal_agent/main.py "want one meal fish and one meal nooodles"
```

## Agent Framework

**Recipe Planner**: Takes your fragmented food inspirations and creates a complete, nutritionally balanced daily meal plan with breakfast, lunch, dinner, and optional snack.

**Grocery List Builder**: Analyzes the meal plan and generates an organized shopping list with proper quantities, grouped by food categories for easy shopping.



## Reflection

Through this project, I learned that CrewAI is a complete agent framework that abstracts many steps for using large language models, allowing us to simply use this framework to create very complete workflows. This project has great potential for further development. Future enhancements could include:

- **Nutritional Database Integration**: Connect to a comprehensive healthy food database to ensure each meal is nutritionally balanced and suitable for different age groups.

- **Price Comparison Agent**: Add a third agent that compares product prices across different markets and stores to create an optimized buying plan that saves money while maintaining quality.

These improvements would transform the system from a simple meal planner into a comprehensive nutrition and shopping optimization tool.

---

**P.S.** Instead of using `requirements.txt`, I chose to use `pyproject.toml` and `uv` for package management.
