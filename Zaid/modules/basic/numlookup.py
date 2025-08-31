from pyrogram import Client, filters
import requests

API_KEY = "num_live_CVwU7vTQehTOEIskKsonAVbx7GDJ4QTfScuxN97C"  # apna API key daalna

@Client.on_message(filters.command(["numlookup"], prefixes=[".", "/", "#"]))
async def numlookup(client, message):
    if len(message.command) < 2:
        return await message.reply_text("❌ Example: `.numlookup +918888888888`")

    number = message.command[1]

    try:
        url = f"http://apilayer.net/api/validate?access_key={API_KEY}&number={number}"
        r = requests.get(url)
        data = r.json()

        if not data.get("valid"):
            return await message.reply_text("⚠️ Invalid number ya info nahi mili.")

        reply = (
            f"📞 **Number Lookup Result**\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"**Number:** `{data.get('international_format')}`\n"
            f"**Country:** {data.get('country_name')} ({data.get('country_code')})\n"
            f"**Location:** {data.get('location')}\n"
            f"**Carrier:** {data.get('carrier')}\n"
            f"**Line Type:** {data.get('line_type')}\n"
        )

        await message.reply_text(reply)

    except Exception as e:
        await message.reply_text(f"⚠️ Error: `{e}`")
