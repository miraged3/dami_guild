from apscheduler.schedulers.background import BackgroundScheduler
from pytz import utc

from database.dragon import dragon_top_today

scheduler = BackgroundScheduler(timezone=utc)

# 发放龙王金币
scheduler.add_job(dragon_top_today, 'cron', hour='0', minute='1')
