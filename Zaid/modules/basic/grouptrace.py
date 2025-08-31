from pyrogram import Client, filters
from Zaid.modules.help import add_command_help

@Client.on_message(filters.command(["grouptrace"], prefixes=[".", "/", "#"]))
async def grouptrace(client, message):
    chat = message.chat

    if not (chat.type in ["group", "supergroup", "channel"]):
        return await message.reply_text("❌ Ye command sirf groups/channels me kaam karti hai.")

    # Members count
    try:
        members = await client.get_chat_members_count(chat.id)
    except:
        members = "N/A"

    # Linked chat
    linked_chat = chat.linked_chat.id if chat.linked_chat else "N/A"

    # Slow mode
    slowmode = f"{chat.slow_mode_delay} sec" if chat.slow_mode_delay else "Off"

    # Build reply
    text = f"📌 **Group Trace Report**\n\n"
    text += f"👥 **Group Name:** {chat.title}\n"
    text += f"🆔 **ID:** `{chat.id}`\n"
    text += f"🔗 **Username:** @{chat.username if chat.username else 'N/A'}\n"
    text += f"📦 **Members:** {members}\n"
    text += f"🔒 **Private:** {'Yes' if not chat.username else 'No'}\n"
    text += f"⏱ **Slow Mode:** {slowmode}\n"
    text += f"🔗 **Linked Chat:** {linked_chat}\n"
    text += f"🚫 **Restrictions:** {'Yes' if chat.permissions else 'No'}\n"

    if chat.date:
        text += f"📅 **Created On:** {chat.date.strftime('%d-%m-%Y')}\n"

    await message.reply_text(text)


# Help menu
add_command_help(
    "grouptrace",
    [
        [".grouptrace", "Get complete info about the current group/channel."],
    ],
)
