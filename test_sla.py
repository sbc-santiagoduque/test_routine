import unittest
from datetime import datetime, timedelta, timezone

from sla import add_business_hours

BOGOTA = timezone(timedelta(hours=-5))


def at(year, month, day, hour, minute=0):
    return datetime(year, month, day, hour, minute, tzinfo=BOGOTA)


class AddBusinessHoursTest(unittest.TestCase):

    def test_same_day(self):
        self.assertEqual(add_business_hours(at(2026, 11, 23, 9), 2), at(2026, 11, 23, 11))

    def test_rolls_over_to_next_day(self):
        self.assertEqual(add_business_hours(at(2026, 11, 23, 16), 3), at(2026, 11, 24, 10))

    def test_skips_the_weekend(self):
        self.assertEqual(add_business_hours(at(2026, 11, 27, 16), 2), at(2026, 11, 30, 9))

    def test_starts_on_saturday(self):
        self.assertEqual(add_business_hours(at(2026, 11, 28, 10), 1), at(2026, 11, 30, 9))

    def test_rejects_naive_datetime(self):
        with self.assertRaises(ValueError):
            add_business_hours(datetime(2026, 11, 23, 9), 1)

    def test_rejects_negative_hours(self):
        with self.assertRaises(ValueError):
            add_business_hours(at(2026, 11, 23, 9), -1)


if __name__ == "__main__":
    unittest.main()


import pytest

from sla import dias_habiles_restantes


def test_counts_working_days_for_carlos():
    assert dias_habiles_restantes(at(2026, 11, 30, 9), at(2026, 11, 27, 9)) == 1
