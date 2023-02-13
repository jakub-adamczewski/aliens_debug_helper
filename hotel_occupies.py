import util


def print_when_hotel_was_occupied_by_which_aliens(
        hotels_capacities: list,
        aliens_count: int,
        min_clock: int,
        max_clock: int,
        all_clocks: list,
        all_msgs: list,
        alien_fractions: list
):
    occupied_hotel_id, stay_start_clock = None, None
    hotels_occupies = {}
    for alien_id, (msgs, clocks, alien_fraction) in enumerate(zip(all_msgs, all_clocks, alien_fractions)):
        for msg, clock in zip(msgs, clocks):
            if 'E' in msg:
                idx = msg.index('E')
                occupied_hotel_id = int(msg[idx + 1: idx + 2])
                stay_start_clock = clock
            elif 'L' in msg:
                key = (occupied_hotel_id, alien_id, alien_fraction)
                if key not in hotels_occupies:
                    hotels_occupies[key] = []
                clocks_during_stay = list(range(stay_start_clock, clock + 1))
                stay_states = 'E' + 'I' * (len(clocks_during_stay) - 2) + 'L'
                [hotels_occupies[key].append(elem) for elem in zip(clocks_during_stay, stay_states)]
                occupied_hotel_id, stay_start_clock = None, None

    with open(f'files/occupies_output.txt', mode='w') as f:
        for clk in range(min_clock - 2, max_clock + 2):
            f.write(f'Clk: {clk} \n')
            guests_in_hotel = {}
            for (hotel_id, alien_id, alien_fraction), occupied_clocks_with_stay_states in sorted(
                    hotels_occupies.items()):
                occupied_clocks, stay_states = list(zip(*occupied_clocks_with_stay_states))
                if clk in occupied_clocks:
                    key = hotel_id
                    if key not in guests_in_hotel:
                        guests_in_hotel[key] = [alien_fraction]
                    else:
                        guests_in_hotel[key].append(alien_fraction)
                    try:
                        assert (len(guests_in_hotel[key]) <= hotels_capacities[hotel_id])
                    except AssertionError:
                        f.write('Error!!! Too much guests in hotel.\n')
                    try:
                        assert (len(set(guests_in_hotel[key])) <= 1)
                    except AssertionError:
                        f.write('Error!!! Both fractions in hotel.\n')
                    f.write(f'|H:{hotel_id}|A:{alien_id}|F:{alien_fraction}|-{stay_states[occupied_clocks.index(clk)]}\n')
            f.write('\n')
