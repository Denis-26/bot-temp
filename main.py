from config import config
from MyBot import Bot
import asyncio
import signal


# trap `sigterm` from `docker stop`
def sigterm(signum, stack):
    bot.stop_running()
    new_loop.close()


signal.signal(signal.SIGTERM, sigterm)


async def main(bot):
    await bot.run()
    await bot.api.delete_webhook()
    await bot.api.set_webhook(config['web_hook'])


if __name__ == "__main__":
    new_loop = asyncio.get_event_loop()
    bot = Bot(config, loop=new_loop)
    new_loop.create_task(main(bot))
    try:
        new_loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        bot.stop_running()
        new_loop.close()
