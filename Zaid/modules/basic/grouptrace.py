from telethon import events
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.channels import GetFullChannelRequest

from Zaid import bot  # <-- agar aapke bot ka naam "bot" hi hai

@bot.on(events.NewMessage(pattern=r"\.grouptrace"))
async def grouptrace(event):
    if not event.is_group:
        return await event.reply("❌ Ye command sirf groups/channels me kaam karti hai.")

    chat = await event.get_chat()

    try:
        if event.is_channel:
            full = await bot(GetFullChannelRequest(chat.id))
            members = full.full_chat.participants_count
            slowmode = full.full_chat.slowmode_seconds or 0
            linked_chat = full.chats[0].id if full.full_chat.linked_chat_id else None
        else:
            full = await bot(GetFullChatRequest(chat.id))
            members = full.full_chat.participants_count
            slowmode = 0
            linked_chat = None
    except Exception:
        full = None
        members = "N/A"
        slowmode = "N/A"
        linked_chat = None

    text = f"📌 **Group Trace Report**\n\n"
    text += f"👥 **Group Name:** {chat.title}\n"
    text += f"🆔 **ID:** `{chat.id}`\n"
    text += f"🔗 **Username:** @{chat.username if chat.username else 'N/A'}\n"
    text += f"📦 **Members:** {members}\n"
    text += f"🔒 **Private:** {'Yes' if not chat.username else 'No'}\n"
    text += f"⏱ **Slow Mode:** {slowmode if slowmode != 0 else 'Off'}\n"

    if linked_chat:
        text += f"🔗 **Linked Chat:** `{linked_chat}`\n"

    # Admins count
    try:
        admins = [p for p in full.full_chat.participants.participants if getattr(p, "admin_rights", None)]
        text += f"👑 **Admins Count:** {len(admins)}\n"
    except Exception:
        text += f"👑 **Admins Count:** N/A\n"

    if hasattr(chat, "date") and chat.date:
        text += f"📅 **Created On:** {chat.date.strftime('%d-%m-%Y')}\n"

    # Extra info
    if full and hasattr(full.full_chat, "banned_rights") and full.full_chat.banned_rights:
        text += "🚫 **Restrictions:** Yes\n"
    else:
        text += "🚫 **Restrictions:** No\n"

    await event.reply(text)
