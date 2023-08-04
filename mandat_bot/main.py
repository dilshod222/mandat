from aiogram.utils import executor
import handlers
from dispatch import dp
from asyncio import new_event_loop,set_event_loop


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    set_event_loop(new_event_loop())
