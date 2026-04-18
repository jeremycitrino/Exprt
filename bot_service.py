"""
bot_service.py – Runs the trading bot as an Android foreground service.
Acquires a partial wake lock to keep the CPU alive.
"""

import threading
from time import sleep

try:
    from android import PythonService
    from jnius import autoclass

    PythonService.mService.setAutoRestartService(True)

    Context = autoclass('android.content.Context')
    PowerManager = autoclass('android.os.PowerManager')
    activity = PythonService.mService
    power_service = activity.getSystemService(Context.POWER_SERVICE)
    wake_lock = power_service.newWakeLock(PowerManager.PARTIAL_WAKE_LOCK, "TradingBot::WakeLock")
    wake_lock.acquire()
except Exception as e:
    print(f"WakeLock error: {e}")
    wake_lock = None

import nostop


def start_trading():
    try:
        nostop.main()
    except Exception as e:
        print(f"Trading bot crashed: {e}")
        sleep(10)
        start_trading()


thread = threading.Thread(target=start_trading, daemon=True)
thread.start()

while True:
    sleep(1)
