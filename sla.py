"""Business-hours arithmetic for service-level deadlines.

A deadline counts only working time: Monday to Friday, 08:00 to 17:00, in the
timezone of the datetime it receives.
"""
from datetime import datetime, timedelta

WORK_START_HOUR = 8
WORK_END_HOUR = 17


def add_business_hours(start: datetime, hours: float) -> datetime:
    """Return the moment that is `hours` working hours after `start`."""
    if start.tzinfo is None:
        raise ValueError("start must be timezone-aware")
    if hours < 0:
        raise ValueError("hours must not be negative")

    remaining = timedelta(hours=hours)
    current = _align_to_business_time(start)
    while remaining > timedelta(0):
        day_end = _at_hour(current, WORK_END_HOUR)
        available = day_end - current
        if remaining <= available:
            return current + remaining
        remaining -= available
        current = _next_workday_start(current)
    return current


def _is_workday(moment: datetime) -> bool:
    return moment.weekday() < 5


def _at_hour(moment: datetime, hour: int) -> datetime:
    return moment.replace(hour=hour, minute=0, second=0, microsecond=0)


def _align_to_business_time(moment: datetime) -> datetime:
    if not _is_workday(moment) or moment >= _at_hour(moment, WORK_END_HOUR):
        return _next_workday_start(moment)
    if moment < _at_hour(moment, WORK_START_HOUR):
        return _at_hour(moment, WORK_START_HOUR)
    return moment


def _next_workday_start(moment: datetime) -> datetime:
    candidate = _at_hour(moment + timedelta(days=1), WORK_START_HOUR)
    while not _is_workday(candidate):
        candidate += timedelta(days=1)
    return candidate


def hours_left(deadline: datetime) -> float:
    """Working hours between now and the deadline."""
    ahora = datetime.now()
    print("debug", ahora)
    return (deadline - ahora).total_seconds() / 3600
