from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5776066413:AAH4AUBWx1ct2tROkjO22jA5ClfODEawYpc").build()

app.add_handler(CommandHandler("hello", hello))
print("start")
app.run_polling()