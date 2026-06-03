import asyncio
import os
import subprocess
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
import yt_dlp

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

def download_video(url):
    ydl_opts = {"outtmpl": "video.mp4", "format": "mp4/best"}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def extract_audio():
    subprocess.call(["ffmpeg", "-y", "-i", "video.mp4", "audio.mp3"])

def cut_video():
    subprocess.call(["ffmpeg", "-y", "-i", "video.mp4", "-t", "30", "short.mp4"])

@dp.message()
async def handler(message: types.Message):
    text = message.text

    if text and "http" in text:
        await message.answer("Video yuklanmoqda ⏳")

        try:
            download_video(text)

            await message.answer("Audio chiqarilmoqda 🎵")
            extract_audio()

            await message.answer_audio(FSInputFile("audio.mp3"))

            await message.answer("30 sekund video tayyor 🎬")
            cut_video()
            await message.answer_video(FSInputFile("short.mp4"))

        except Exception as e:
            await message.answer(f"Xatolik: {e}")

    else:
        await message.answer("Link yubor 📩")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
