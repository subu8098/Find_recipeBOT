🍽️ Telegram Recipe Bot 🤖
🚀 About the Project
The Telegram Recipe Bot is an intelligent cooking assistant that helps users find delicious recipes based on the ingredients they have! Simply send a list of ingredients, and the bot will fetch detailed recipes with images and cooking instructions using the Spoonacular API.

🔹 No more food waste! 🍕🥦
🔹 Get creative with what you have! 🎨
🔹 Instant, easy-to-follow recipes! 📖

📌 Features
✅ Ingredient-Based Recipe Suggestions – Just enter your ingredients, and the bot will fetch matching recipes.
✅ Step-by-Step Cooking Instructions – Get complete preparation steps for each recipe.
✅ Image Support – View recipe images directly in Telegram.
✅ Fast & Efficient – Uses Spoonacular API to fetch reliable and accurate recipes.
✅ Seamless Telegram Integration – Simple, user-friendly interaction via Telegram bot.

🛠️ Tech Stack
Python – Backend logic and API calls
Telegram Bot API – For seamless user interaction
Spoonacular API – For fetching recipes & instructions
Requests – To communicate with APIs
Asyncio (Telegram Ext) – For handling asynchronous message responses
📸 Screenshots
Ingredient Input	Recipe Response	Image Support
🛠️ Setup & Installation
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/telegram-recipe-bot.git
cd telegram-recipe-bot
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up Your API Keys
Get a Spoonacular API key from Spoonacular API
Get a Telegram Bot Token from BotFather
Update these in the RECIPE_API_KEY and TOKEN variables in bot.py.

4️⃣ Run the Bot
bash
Copy
Edit
python bot.py
🔍 How It Works
1️⃣ Send a list of ingredients to the Telegram bot.
2️⃣ The bot fetches recipes from the Spoonacular API.
3️⃣ Valid recipes with cooking instructions are sent back with images.
4️⃣ Enjoy your meal! 🍽️

📜 Example Usage
User:

Copy
Edit
chicken, tomatoes, garlic
Bot:

sql
Copy
Edit
🍽️ *Garlic Chicken Pasta*
📖 Instructions: 1. Cook pasta... 2. Add chicken... (Full instructions sent)
📷 [Image Sent]
🔗 API Details
The bot uses Spoonacular API endpoints:
✅ /recipes/findByIngredients – Fetches recipes based on available ingredients.
✅ /recipes/{id}/information – Fetches cooking instructions for a specific recipe.

🤝 Contributing
Got ideas or improvements? Feel free to open an issue or submit a pull request!

📜 License
This project is licensed under the MIT License.

📩 Contact
💡 Developer: Subu
📧 Email: subuvarathan8098@gmail.com


🌟 If you like this project, don't forget to ⭐ the repo! 🌟
