from telegram import Update, InputMediaPhoto
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import requests

# API Configuration
RECIPE_API_KEY = r"YOUR_KEY"
FIND_BY_INGREDIENTS_URL = "https://api.spoonacular.com/recipes/findByIngredients"
RECIPE_DETAILS_URL = "https://api.spoonacular.com/recipes/{id}/information"

# Function to fetch recipes based on ingredients
def get_recipes(ingredients):
    print(f"Fetching recipes for ingredients: {ingredients}")

    params = {
        "ingredients": ",".join(ingredients),
        "number": 5,  # Number of recipes to return
        "apiKey": RECIPE_API_KEY
    }
    
    response = requests.get(FIND_BY_INGREDIENTS_URL, params=params)
    print(f"API Request Sent. Status Code: {response.status_code}")

    if response.status_code == 200:
        recipes = response.json()
        print("API Response Received:", recipes)  # Debugging

        valid_recipes = []
        for recipe in recipes:
            recipe_id = recipe.get("id")
            title = recipe.get("title", "Unknown Recipe")
            image_url = recipe.get("image", None)  # Get image URL if available
            
            if recipe_id:
                details = get_recipe_details(recipe_id)
                if details:
                    valid_recipes.append({
                        "title": title,
                        "image_url": image_url,
                        "instructions": details.get("instructions", "No instructions available.")
                    })

        if not valid_recipes:
            print("No valid recipes found with instructions.")
            return []

        print("Recipes with instructions fetched successfully!")
        return valid_recipes

    print("Error fetching recipes from API.")
    return []

# Function to fetch full recipe details
def get_recipe_details(recipe_id):
    url = RECIPE_DETAILS_URL.format(id=recipe_id)
    params = {"apiKey": RECIPE_API_KEY}
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()  # Returns full recipe details
    return None

# Start command
async def start(update: Update, context: CallbackContext):
    print("Received /start command")
    await update.message.reply_text("Hello! Send me a list of vegetables, and I'll suggest recipes with full instructions!")

# Handle user input
async def suggest_recipe(update: Update, context: CallbackContext):
    user_input = update.message.text
    print(f"User input received: {user_input}")

    ingredients = user_input.split(", ")
    print(f"Extracted ingredients: {ingredients}")

    recipes = get_recipes(ingredients)
    
    if not recipes:
        await update.message.reply_text("No recipes found. Try adding more ingredients!")
        return

    print(f"Sending {len(recipes)} recipes to user.")

    for recipe in recipes:
        message_text = f"🍽️ *{recipe['title']}*\n📖 Instructions:\n{recipe['instructions']}"

        if recipe["image_url"]:
            print(f"Sending image: {recipe['image_url']}")
            await update.message.reply_photo(photo=recipe["image_url"], caption=message_text, parse_mode="Markdown")
        else:
            await update.message.reply_text(message_text, parse_mode="Markdown")

# Main function to start the bot
def main():
    TOKEN = r"YOUR_TOKEN"

    print("Starting Telegram bot...")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, suggest_recipe))

    print("Bot is now running and listening for messages...")
    app.run_polling()

if __name__ == "__main__":
    main()
