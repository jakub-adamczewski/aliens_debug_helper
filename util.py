from datetime import time


def get_text_between(left: str, right: str, text: str):
    left_index = text.index(left) + len(left)
    right_index = left_index + text[left_index:].index(right)
    return text[left_index:right_index]


def get_times_and_hotel_stays(path: str):
    with open(path) as f:
        enters_and_leaves = list(
            filter(
                lambda line: "marker" in line,
                f.readlines()
            )
        )

        times, msgs = [], []
        for line in enters_and_leaves:
            times.append(
                time.fromisoformat(
                    get_text_between(
                        left='|t:',
                        right='|',
                        text=line
                    )
                )
            )
            msgs.append(
                get_text_between(
                    left='|msg:',
                    right='.marker',
                    text=line
                )
            )
    return times, msgs
