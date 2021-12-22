from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""Hi there,👋 {message.from_user.first_name}!
\nThis is ABHINAS MUSIC BOT.
I play music on Telegram's Voice Chats.
\nFo More Help Use Buttons Below:
 """,
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Owner 🛠", url="https://t.me/abhinasroy")
                  ],[
                    InlineKeyboardButton(
                        "💬 Updates Channel", url="https://t.me/ABOUT_ABHINAS"
                    ),
                    InlineKeyboardButton(
                        "💻 Support Group", url="https://t.me/DOSTI_GROUP_1234"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add Me To Your Group ➕", url="https://t.me/ABHINAS_KA_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""*ABHINAS MUSIC BOT is alive.*""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Updates Channel", url="https://t.me/ABOUT_ABHINAS")
                ]
            ]
        )
   )


