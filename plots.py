import datetime

import matplotlib.pyplot as plt
import numpy as np

import util


def create_plot(
        hotels_capacities: list,
        aliens_count: int,
        min_clock: int,
        max_clock: int,
        all_clocks: list,
        all_msgs: list,
        alien_fractions: list
):
    fig, axs = plt.subplots(aliens_count, 1, figsize=(18, 18), constrained_layout=True)

    fig.suptitle(f'Hotel capacities: {hotels_capacities}')

    for alien_rank in range(aliens_count):
        clocks, msgs = all_clocks[alien_rank], all_msgs[alien_rank]
        base_date = datetime.datetime(2023, 1, 1, 0, 0, 0)

        datetimes = list(map(lambda clk: base_date + datetime.timedelta(seconds=clk), clocks))
        datetimes.insert(0, base_date - datetime.timedelta(seconds=1))
        clocks.insert(0, min_clock - 1)
        msgs.insert(0, 'Start')
        datetimes.append(base_date + datetime.timedelta(seconds=max_clock + 1))
        msgs.append('Stop')
        clocks.append(max_clock + 1)

        levels = list(map(util.msg_to_level, msgs))

        axs[alien_rank].set_xlabel(f'Alien {alien_rank} {alien_fractions[alien_rank]}')
        axs[alien_rank].vlines(datetimes, 0, levels, color="tab:red")
        axs[alien_rank].plot(datetimes, np.zeros_like(datetimes), "-o", color="k", markerfacecolor="w")

        for dt, l, m, clk in zip(datetimes, levels, msgs, clocks):
            axs[alien_rank].annotate(
                f'{m}-{clk}',
                xy=(dt, l),
                xytext=(-3, np.sign(l) * 3),
                textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="top" if l > 0 else "bottom"
            )

        axs[alien_rank].yaxis.set_visible(False)
        axs[alien_rank].spines[["left", "top", "right"]].set_visible(False)
        axs[alien_rank].margins(y=0.1)

    plt.show()
