from command import cmd

@cmd("calc")
async def calc(event):

    try:
        expr = event.text.split(" ", 1)[1]
        result = eval(expr)
        await event.reply(f"🧮 Result: {result}")
    except:
        await event.reply("Invalid calculation.")
