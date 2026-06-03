if text and "http" in text:
    await message.answer("Video yuklanmoqda ⏳")

    download_video(text)

    await message.answer("Video yuklandi ✅")
