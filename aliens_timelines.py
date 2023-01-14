from plots import create_plot
from util import get_clocks_and_hotel_stays, get_alien_fraction
from hotel_occupies import print_when_hotel_was_occupied_by_which_aliens

aliens_count = 4
hotels_capacities = [1, 2]

all_clocks, all_msgs = [], []
min_clock, max_clock = 10_000, -10
alien_fractions = []

if __name__ == '__main__':
    for alien_rank in range(aliens_count):
        clocks, msgs = get_clocks_and_hotel_stays(path=f'files/alien{alien_rank}.txt')
        min_clock = min(min_clock, clocks[0])
        max_clock = max(max_clock, clocks[-1])
        all_clocks.append(clocks)
        all_msgs.append(msgs)
        alien_fractions.append(get_alien_fraction(path=f'files/alien{alien_rank}.txt'))

    create_plot(
        hotels_capacities=hotels_capacities,
        aliens_count=aliens_count,
        min_clock=min_clock,
        max_clock=max_clock,
        all_clocks=all_clocks,
        all_msgs=all_msgs,
        alien_fractions=alien_fractions,
    )

    print_when_hotel_was_occupied_by_which_aliens(
        hotels_capacities=hotels_capacities,
        aliens_count=aliens_count,
        min_clock=min_clock,
        max_clock=max_clock,
        all_clocks=all_clocks,
        all_msgs=all_msgs,
        alien_fractions=alien_fractions,
    )
