from os.path import join

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
import states
from buttons.inline import check_chanel
from buttons.markup import reg_menu, remove_button
from configs.constants import channel1_id, url, BASE_URL, chat_ids
from dispatch import dp, bot
from services import write_user_id

from bs4 import BeautifulSoup
import requests


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print(message.from_user.id)
    message_body = f"""Assalomu alaykum botimizga xush kelibsiz. Bu yerda imtihon natijangizni bilib olishingiz mumkin.
Iltimos agar natijangiz ko‘rinmasa qayta urinib ko‘ring, chunki barcha botlar yuklama ostida ishlamoqda.
Rasmiy sahifamiz: @on_24uz"""
    await states.StartStates.kanallar.set()
    await message.bot.send_message(chat_id=message.chat.id,
                                   text=message_body, parse_mode='html', reply_markup=check_chanel())


@dp.callback_query_handler(state=states.StartStates.kanallar)
async def check_sub(callback: types.CallbackQuery, state: FSMContext):
    try:
        user_id = callback.from_user.id
        await callback.message.delete()
        if callback.data == 'subdone':
            check_sub_channel = await bot.get_chat_member(chat_id=channel1_id, user_id=user_id)
            if check_sub_channel['status'] != 'left':
                await callback.message.answer('Natijangizni aniqlash uchun telefon raqamingizni yuboring ', reply_markup=reg_menu())
                await states.StartStates.number.set()
            else:
                await callback.message.answer("Botdan foydalanish uchun kanalga a'zo bo'ling", reply_markup=check_chanel())
                await states.StartStates.kanallar.set()
    except Exception:
        await callback.bot.send_message(chat_id=292622464, text=str(Exception))

@dp.message_handler(content_types=[types.ContentType.CONTACT], state=states.StartStates.number)
async def phone_number(message: types.Message, state: FSMContext):
    if message.contact:
        about = f"""
        Number: {message.contact.phone_number}
FISH: {message.from_user.last_name}  {message.from_user.first_name}
Username: {message.from_user.username}"""
        await message.answer_photo(photo=open(join(BASE_URL,'db','image.jpg'), 'rb'), caption="Namunaga binoan ID raqamingizni kiriting", reply_markup=ReplyKeyboardRemove())
        for i in chat_ids:
            await bot.send_message(chat_id=i,text=about, reply_markup=ReplyKeyboardRemove())
        await state.finish()
    else:
        await message.delete()
        await message.answer("Iltimos telefon raqamingizni jo'nating", reply_markup=reg_menu())


@dp.message_handler(content_types=['text'])
async def main_handler(message: types.Message):
    _id = message.text
    if message.text != '/start':
        try:
            contents = []
            new_images = []
            headers = {
                """
                user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36
                """

            }
            url = "https://mandat.uzbmb.uz/Home2023/AfterFilter?name=" + _id + "&region=0&university=0"
            r = requests.get(url=url)
            soup = BeautifulSoup(r.text, 'html.parser')
            td = soup.find_all('td')
            FISH = "<b>FISH:</b> "
            DIRECTION = "<b>Yo'nalish:</b> "
            OTM = "<b>Oliy ta'lim muassasasi:</b> "
            BALL = "<b>To'plagan ball: </b>"
            LANGUAGE = "<b>Ta'lim tili: </b>"
            SHAKLI = "<b>Ta'lim shakli: </b>"

            if len(td) > 3:
                check_url = td[-1].find('a').get('href')
                FISH += td[1].text
                DIRECTION += td[2].text
                OTM += td[3].text
                BALL += td[4].text
                LANGUAGE += td[5].text
                SHAKLI += td[6].text
                text = f"""{FISH} 
{DIRECTION}
{OTM}
{BALL}
{LANGUAGE}
{SHAKLI}
Batafsil: <a href="https://mandat.uzbmb.uz{check_url}">👉Havolaga o'tish 👈</a>

<b>Natijani aniqlaydigan bot: </b> 
@mandatbmb_rasmiy1_bot
    """
                await message.answer(text, parse_mode='html')
        #         check_url = td[-1].find('a').get('href')
        #         url2 = "https://mandat.uzbmb.uz" + check_url
        #         r2 = requests.get(url=url2)
        #         soup2 = BeautifulSoup(r2.text, 'html.parser')
        #         tr = soup2.find_all('tr')[-3]
        #         print(soup2)
        #         ball = tr.find_all('td')
        #         if eval(ball[0].text) == int:
        #             correct_answer1 = ball[0].text
        #             blok1ball = ball[1].text
        #             correct_answer2 = ball[2].text
        #             blok2ball = ball[3].text
        #             correct_answer3 = ball[4].text
        #             blok3ball = ball[5].text
        #             correct_answer4 = ball[6].text
        #             blok4ball = ball[7].text
        #             correct_answer5 = ball[8].text
        #             blok5ball = ball[9].text
        #             text2 = f"""1-blok: {blok1ball} ({correct_answer1} ta to'g'ri javob)
        # 2-blok: {blok2ball} ({correct_answer2} ta to'g'ri javob)
        # 3-blok: {blok3ball} ({correct_answer3} ta to'g'ri javob)
        # 3-blok: {blok3ball} ({correct_answer3} ta to'g'ri javob)
        # 4-blok: {blok4ball} ({correct_answer4} ta to'g'ri javob)
        # 5-blok: {blok5ball} ({correct_answer5} ta to'g'ri javob)"""
        #             await message.answer(text2)
        #             print(ball[0].text)
        #             print(ball[1].text)
        #         else:
        #             await message.answer("Hali natijangiz chiqmadi:)")
            else:
                await message.answer("Natijangiz hali e'lon qilinmadi. Iltimos keyinroq urinib ko'ring.")


        except Exception:
            await message.bot.send_message(chat_id=292622464, text=str(Exception))
    else:
        message_body = f"""Assalomu alaykum botimizga xush kelibsiz. Bu yerda imtihon natijangizni bilib olishingiz mumkin.
        Iltimos agar natijangiz ko‘rinmasa qayta urinib ko‘ring, chunki barcha botlar yuklama ostida ishlamoqda.
        Rasmiy sahifamiz: @on_24uz"""
        await states.StartStates.kanallar.set()
        await message.bot.send_message(chat_id=message.chat.id,
                                       text=message_body, parse_mode='html', reply_markup=check_chanel())
