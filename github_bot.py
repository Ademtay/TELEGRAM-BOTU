import os
import logging
from datetime import datetime, timedelta
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from github import Github

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get environment variables
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f'Merhaba {user.first_name}! 👋\n\n'
        'GitHub Bot\'una hoş geldiniz! Kullanılabilir komutlar:\n'
        '/repos - GitHub repolarınızı listeler\n'
        '/activity - Son aktivitelerinizi gösterir\n'
        '/help - Yardım menüsünü gösterir'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        'GitHub Bot Komutları:\n\n'
        '/start - Botu başlatır\n'
        '/repos - GitHub repolarınızı listeler\n'
        '/activity - Son aktivitelerinizi gösterir\n'
        '/help - Bu yardım mesajını gösterir'
    )

async def list_repos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """List user's GitHub repositories."""
    try:
        g = Github(GITHUB_TOKEN)
        user = g.get_user()
        repos = user.get_repos()
        
        message = "GitHub Repolarınız:\n\n"
        for repo in repos:
            message += f"📁 {repo.name}\n"
            message += f"   ⭐ Stars: {repo.stargazers_count}\n"
            message += f"   🔄 Forks: {repo.forks_count}\n"
            message += f"   📝 Description: {repo.description or 'Açıklama yok'}\n\n"
        
        await update.message.reply_text(message)
    except Exception as e:
        await update.message.reply_text(f"Bir hata oluştu: {str(e)}")

async def show_activity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show user's recent GitHub activity."""
    try:
        g = Github(GITHUB_TOKEN)
        user = g.get_user()
        events = user.get_events()
        
        message = "Son Aktiviteleriniz:\n\n"
        for event in events[:5]:  # Son 5 aktivite
            created_at = event.created_at.strftime("%d/%m/%Y %H:%M")
            message += f"🕒 {created_at}\n"
            message += f"📝 {event.type}\n"
            if hasattr(event, 'repo'):
                message += f"📁 {event.repo.name}\n"
            message += "\n"
        
        await update.message.reply_text(message)
    except Exception as e:
        await update.message.reply_text(f"Bir hata oluştu: {str(e)}")

def main():
    """Start the bot."""
    # Create the Application and pass it your bot's token
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("repos", list_repos))
    application.add_handler(CommandHandler("activity", show_activity))

    # Start the Bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main() 