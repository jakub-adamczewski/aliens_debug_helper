from datetime import time

import util
from util import to_seconds


def print_when_hotel_was_occupied_by_which_aliens(
        hotels_capacities: list,
        aliens_count: int,
        min_time: time,
        max_time: time,
        all_times: list,
        all_msgs: list,
        alien_fractions: list
):
    start_second = to_seconds(min_time) - 1
    end_second = util.to_seconds(max_time) + 1

    occupied_hotel_id, stay_start_sec = None, None
    hotels_occupies = {}

    for alien_id, (msgs, times, alien_fraction) in enumerate(zip(all_msgs, all_times, alien_fractions)):
        for msg, tm in zip(msgs, times):
            curr_second = to_seconds(tm) - start_second
            if 'E' in msg:
                idx = msg.index('E')
                occupied_hotel_id = int(msg[idx + 1: idx + 2])
                stay_start_sec = curr_second
            elif 'L' in msg:
                key = (occupied_hotel_id, alien_id, alien_fraction)
                if key not in hotels_occupies:
                    hotels_occupies[key] = []
                stay_seconds = list(range(stay_start_sec, curr_second + 1))
                [hotels_occupies[key].append(s) for s in stay_seconds]
                occupied_hotel_id, stay_start_sec = None, None

    for second in range(end_second - start_second + 1):
        print(f'Sec: {second} ')
        guests_count_in_hotels = {}
        for (hotel_id, alien_id, alien_fraction), occupied_seconds in sorted(hotels_occupies.items()):
            if second in occupied_seconds:
                key = hotel_id
                if key not in guests_count_in_hotels:
                    guests_count_in_hotels[key] = 1
                else:
                    guests_count_in_hotels[key] += 1
                try:
                    assert (guests_count_in_hotels[hotel_id] <= hotels_capacities[hotel_id])
                except AssertionError:
                    print('Overlapping stay!')
                    # happens when during given second there are more aliens in hotel, then it's capacity
                    # it should happen only when alien leaves the hotel, and next one enters it right after him
                print(f'|H:{hotel_id}|A:{alien_id}|F:{alien_fraction}|', end='-')
                if second - 1 not in occupied_seconds:
                    print("E")
                elif second + 1 not in occupied_seconds:
                    print("L")
                else:
                    print("I")
        print()
