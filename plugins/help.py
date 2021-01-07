from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently only supports Youtube Single  videos(No playlist),Just Send Youtube Url.\n\nLike:http://www.youtube.com/watch?v=6Ojs-T8936g\n\nYou can also use @vid or @youtube in inline mode to search youtube videos.\n\nExample: Type \"@vid silenceandroidgamer\"\nOr\nType \"@youtube silenceandroidgamer\"."
    await message.reply_text(helptxt)
