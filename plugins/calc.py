from command import cmd

HELP = {
    "name": "Calculator",
    "description": "Evaluate math expressions",
    "usage": ".calc 5+5"
}

@cmd("calc")
async def calc(event):

    try:
        expr = event.text.split(" ", 1)[1]
        result = eval(expr)
        await event.reply(f"🧮 Result: {result}")
    except:
        await event.reply("Invalid calculation.")
