import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from datetime import time

from util import get_times_and_hotel_stays

aliens_count = 2

all_times, all_msgs = [], []
min_time, max_time = time(23, 59, 59), time(0, 0, 0)

for alien_rank in range(aliens_count):
    times, msgs = get_times_and_hotel_stays(path=f'files/alien{alien_rank}.txt')
    min_time = min(min_time, times[0])
    max_time = max(max_time, times[-1])
    all_times.append(times)
    all_msgs.append(msgs)

fig, axs = plt.subplots(aliens_count, 1, constrained_layout=True)

for alien_rank in range(aliens_count):
    times, msgs = all_times[alien_rank], all_msgs[alien_rank]

    times.insert(0, min_time)
    times.append(max_time)
    msgs.insert(0, 'S')
    msgs.append('E')

    datetimes = list(map(lambda tm: datetime(2023, 1, 1, tm.hour, tm.minute, tm.second), times))
    levels = np.tile([1, -1], int(np.ceil(len(datetimes) / 2)))[:len(datetimes)]

    axs[alien_rank].set_xlabel(f'Alien {alien_rank}')
    axs[alien_rank].vlines(datetimes, 0, levels, color="tab:red")
    axs[alien_rank].plot(datetimes, np.zeros_like(datetimes), "-o",
                         color="k", markerfacecolor="w")
    for t, l, m in zip(datetimes, levels, msgs):
        axs[alien_rank].annotate(
            f'{m}-{t.strftime("%H:%M:%S")}',
            xy=(t, l),
            xytext=(-3, np.sign(l) * 3),
            textcoords="offset points",
            horizontalalignment="right",
            verticalalignment="bottom" if l > 0 else "top"
        )

    axs[alien_rank].yaxis.set_visible(False)
    axs[alien_rank].spines[["left", "top", "right"]].set_visible(False)
    axs[alien_rank].margins(y=0.1)

plt.show()

print()
