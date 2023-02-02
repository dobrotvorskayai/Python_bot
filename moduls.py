from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}\n'
                                    'Введи код действия и через пробел введи числа для выполнения вычислений:\n'
                                    '/sum - сложение\n'
                                    '/sub - вычитание\n'
                                    '/mul - умножение\n'
                                    '/div - деление\n'
                                    '/inv_div - целочисленное деление\n'
                                    '/rem_of_div - остаток от деления\n'
                                    '/exp - возведение в степень\n'
                                    '/sqrt - корень квадратьный\n'
                                    '/sum_comp - сложение комплексных чисел\n'
                                    '/sub_comp - вычитание комплексных чисел\n'
                                    '/mul_comp - умножение комплексных чисел\n'
                                    '/div_comp - деление комплексных чисел\n'
                                    '/exp_comp - возведение в степень комплексных чисел\n'
                                    )

async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    a = int(item[1])
    b = int(item[2])
    await update.message.reply_text(f'{a} + {b} = {a + b}')

async def sub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    a = int(item[1])
    b = int(item[2])
    await update.message.reply_text(f'{a} - {b} = {a - b}')

async def mul(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    a = int(item[1])
    b = int(item[2])
    await update.message.reply_text(f'{a} * {b} = {a * b}')

async def div(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    a = int(item[1])
    b = int(item[2])
    await update.message.reply_text(f'{a} / {b} = {a / b}')

async def inv_div(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    a = int(item[1])
    b = int(item[2])
    await update.message.reply_text(f'{a} // {b} = {a // b}')

async def rem_of_div(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    a = int(item[1])
    b = int(item[2])
    await update.message.reply_text(f'{a} % {b} = {a % b}')

async def exp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    a = int(item[1])
    b = int(item[2])
    await update.message.reply_text(f'{a} ** {b} = {a ** b}')

async def sqrt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    a = int(item[1])
    await update.message.reply_text(f'{a} ** 0,5 = {a ** 0.5}')

async def sum_comp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    lst = []
    x = int(item[1])
    y = int(item[2])
    z = int(item[3])
    w = int(item[4])
    a = lst.append(complex(x, y))
    b = lst.append(complex(z, w))
    await update.message.reply_text(f'{lst[0]} + {lst[1]} = {lst[0] + lst[1]}')

async def sub_comp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    lst = []
    x = int(item[1])
    y = int(item[2])
    z = int(item[3])
    w = int(item[4])
    a = lst.append(complex(x, y))
    b = lst.append(complex(z, w))
    await update.message.reply_text(f'{lst[0]} - {lst[1]} = {lst[0] - lst[1]}')

async def mul_comp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    lst = []
    x = int(item[1])
    y = int(item[2])
    z = int(item[3])
    w = int(item[4])
    a = lst.append(complex(x, y))
    b = lst.append(complex(z, w))
    await update.message.reply_text(f'{lst[0]} * {lst[1]} = {lst[0] * lst[1]}')

async def div_comp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    lst = []
    x = int(item[1])
    y = int(item[2])
    z = int(item[3])
    w = int(item[4])
    a = lst.append(complex(x, y))
    b = lst.append(complex(z, w))
    await update.message.reply_text(f'{lst[0]} / {lst[1]} = {lst[0] / lst[1]}')

async def exp_comp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    item = msg.split()
    lst = []
    x = int(item[1])
    y = int(item[2])
    z = int(item[3])
    w = int(item[4])
    a = lst.append(complex(x, y))
    b = lst.append(complex(z, w))
    await update.message.reply_text(f'{lst[0]} ** {lst[1]} = {lst[0] ** lst[1]}')

