"""
Contains all scheduled task definitions.

This is imported into the clock management command.

"""
from __future__ import annotations

import logging
from reminder.apps.events.utils import process_events

from apscheduler.schedulers.blocking import BlockingScheduler
from django.conf import settings
from django_apscheduler.jobstores import DjangoJobStore
from django_rq import get_queue


logger = logging.getLogger(__name__)
queue = get_queue(name="default", is_async=True)

scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
scheduler.add_jobstore(DjangoJobStore(), "default")


@scheduler.scheduled_job("interval", seconds=10, id="onesignal_sync_all_tenant_users")
def process():
    process_events()
