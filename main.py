from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import TOKEN

from moduls import*

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("sum", sum))
app.add_handler(CommandHandler("sub", sub))
app.add_handler(CommandHandler("mul", mul))
app.add_handler(CommandHandler("div", div))
app.add_handler(CommandHandler("inv_div", inv_div))
app.add_handler(CommandHandler("rem_of_div", rem_of_div))
app.add_handler(CommandHandler("exp", exp))
app.add_handler(CommandHandler("sqrt", sqrt))
app.add_handler(CommandHandler("sum_comp", sum_comp))
app.add_handler(CommandHandler("sub_comp", sub_comp))
app.add_handler(CommandHandler("mul_comp", mul_comp))
app.add_handler(CommandHandler("div_comp", div_comp))
app.add_handler(CommandHandler("exp_comp", exp_comp))

print("start")
app.run_polling()