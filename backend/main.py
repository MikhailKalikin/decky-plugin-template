import asyncio
from decky_plugin import logger, DeckyPlugin

class Plugin:
    def __init__(self):
        self._notified = False
        self._threshold = 80

    async def _main(self):
        while True:
            try:
                level = 80
                status = "Charging"
                logger.info(f"[BatteryNotifier] Level: {level}%, Status: {status}")

                if level >= self._threshold and status == "Charging" and not self._notified:
                    await DeckyPlugin.send_notification(
                        title="🔋 Батарея заряжена",
                        body=f"Уровень заряда: {level}%. Можно отключить питание.",
                    )
                    self._notified = True

                if level < self._threshold:
                    self._notified = False

            except Exception as e:
                logger.error(f"[BatteryNotifier] Ошибка: {e}")

            await asyncio.sleep(10)