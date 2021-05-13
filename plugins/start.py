from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/TG_Free_bots")],
        [InlineKeyboardButton("All our FREE BOTS", url="https://t.me/TG_Free_Bots/3")]


    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation

    
    @app.on_message(filters.text & filters.private )
def echo(client, message):
 update_channel = "TG_Free_Bots"
 user_id = message.from_user.id
 if update_channel :
  try:
   client.get_chat_member(update_channel, user_id)
  except UserNotParticipant:
   message.reply_text("**__Join our Bot's Channel to use ME__** ",parse_mode="markdown", reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([ [ InlineKeyboardButton("Join our Bot's channel" ,url="https://t.me/TG_Free_Bots") ]
   ]))
   return
