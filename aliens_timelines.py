import datetime

from hotel_occupies import print_when_hotel_was_occupied_by_which_aliens
from plots import create_plot
from util import get_times_and_hotel_stays, get_alien_fraction

aliens_count = 4
hotels_capacities = [2]

all_times, all_msgs = [], []
min_time, max_time = datetime.time(23, 59, 59), datetime.time(0, 0, 0)
alien_fractions = []

for alien_rank in range(aliens_count):
    times, msgs = get_times_and_hotel_stays(path=f'files/alien{alien_rank}.txt')
    min_time = min(min_time, times[0])
    max_time = max(max_time, times[-1])
    all_times.append(times)
    all_msgs.append(msgs)
    alien_fractions.append(get_alien_fraction(path=f'files/alien{alien_rank}.txt'))

create_plot(
    hotels_capacities=hotels_capacities,
    aliens_count=aliens_count,
    min_time=min_time,
    max_time=max_time,
    all_times=all_times,
    all_msgs=all_msgs,
    alien_fractions=alien_fractions,
)

print_when_hotel_was_occupied_by_which_aliens(
    hotels_capacities=hotels_capacities,
    aliens_count=aliens_count,
    min_time=min_time,
    max_time=max_time,
    all_times=all_times,
    all_msgs=all_msgs,
    alien_fractions=alien_fractions,
)
