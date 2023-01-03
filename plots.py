import datetime

import matplotlib.pyplot as plt
import numpy as np

import util


def create_plot(
        hotels_capacities: list,
        aliens_count: int,
        min_time: datetime.time,
        max_time: datetime.time,
        all_times: list,
        all_msgs: list,
        alien_fractions: list
):
    fig, axs = plt.subplots(aliens_count, 1, figsize=(10, 10), constrained_layout=True)

    fig.suptitle(f'Hotel capacities: {hotels_capacities}')

    for alien_rank in range(aliens_count):
        times, msgs = all_times[alien_rank], all_msgs[alien_rank]

        times.insert(0, min_time)
        times.append(max_time)
        msgs.insert(0, 'Start')
        msgs.append('Stop')

        datetimes = list(map(lambda tm: datetime.datetime(2023, 1, 1, tm.hour, tm.minute, tm.second), times))
        datetimes[0] -= datetime.timedelta(seconds=1)
        min_datetime = datetimes[0]
        datetimes[-1] += datetime.timedelta(seconds=1)

        levels = list(map(util.msg_to_level, msgs))

        axs[alien_rank].set_xlabel(f'Alien {alien_rank} {alien_fractions[alien_rank]}')
        axs[alien_rank].vlines(datetimes, 0, levels, color="tab:red")
        axs[alien_rank].plot(datetimes, np.zeros_like(datetimes), "-o",
                             color="k", markerfacecolor="w")

        for dt, l, m in zip(datetimes, levels, msgs):
            secs_from_beginning = util.to_seconds(dt.time()) - util.to_seconds(min_datetime.time())

            axs[alien_rank].annotate(
                f'{m}-{secs_from_beginning}',
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
