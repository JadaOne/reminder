"""
Custom clock process to handle scheduled tasks.

Scheduled tasks definitions should be in the core.schedule module;
this command simply runs the scheduler - it should never need changing.
"""
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import register_events

from ...schedule import scheduler

# this ensures that scheduler jobs are logged
register_events(scheduler)


class Command(BaseCommand):

    help = "Runs the **BLOCKING** APScheduler."

    def handle(self, *args, **options):
        scheduler.start()
