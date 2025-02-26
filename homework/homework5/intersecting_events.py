import random


def intersecting_events(
    h_start1: int,
    m_start1: int,
    s_start1: int,
    h_finish1: int,
    m_finish1: int,
    s_finish1: int,
    h_start2: int,
    m_start2: int,
    s_start2: int,
    h_finish2: int,
    m_finish2: int,
    s_finish2: int,
) -> str:
    if not all(8 <= hour <= 18 for hour in (h_start1, h_start2, h_finish1, h_finish2)):
        raise ValueError("out of range")
    if not all(
        0 <= minute <= 59 for minute in (m_start1, m_start2, m_finish2, m_finish1)
    ):
        raise ValueError("out of range")
    if not all(
        0 <= second <= 59 for second in (s_start1, s_start2, s_finish1, s_finish2)
    ):
        raise ValueError("out of range")
    start1 = h_start1 * 3600 + m_start1 * 60 + s_start1
    finish1 = h_finish1 * 3600 + m_finish1 * 60 + s_finish1
    start2 = h_start2 * 3600 + m_start2 * 60 + s_start2
    finish2 = h_finish2 * 3600 + m_finish2 * 60 + s_finish2
    if start1 <= start2 <= finish1 or start2 <= start1 <= finish2:
        return "intersecting events"
    return "events do not intersect"


if __name__ == "__main__":

    hour_1_start = random.randint(8, 13)
    minute_1_start = random.randint(0, 59)
    second_1_start = random.randint(0, 59)
    hour_1_finish = random.randint(hour_1_start, 18)
    minute_1_finish = random.randint(
        minute_1_start if hour_1_start == hour_1_finish else 0, 59
    )
    second_1_finish = random.randint(
        (
            second_1_start
            if hour_1_start == hour_1_finish and minute_1_start == minute_1_finish
            else 0
        ),
        59,
    )
    hour_2_start = random.randint(8, 13)
    minute_2_start = random.randint(0, 59)
    second_2_start = random.randint(0, 59)
    hour_2_finish = random.randint(hour_2_start, 18)
    minute_2_finish = random.randint(
        minute_2_start if hour_2_start == hour_2_finish else 0, 59
    )
    second_2_finish = random.randint(
        (
            second_2_start
            if hour_2_start == hour_2_finish and minute_2_start == minute_2_finish
            else 0
        ),
        59,
    )

    result = intersecting_events(
        hour_1_start,
        minute_1_start,
        second_1_start,
        hour_1_finish,
        minute_1_finish,
        second_1_finish,
        hour_2_start,
        minute_2_start,
        second_2_start,
        hour_2_finish,
        minute_2_finish,
        second_2_finish,
    )

    print(
        f"Event 1: {hour_1_start}:{minute_1_start}:{second_1_start} - {hour_1_finish}:{minute_1_finish}:{second_1_finish}"
    )
    print(
        f"Event 2: {hour_2_start}:{minute_2_start}:{second_2_start} - {hour_2_finish}:{minute_2_finish}:{second_2_finish}"
    )
    print(result)
