from datetime import time


# def to_seconds(time: time) -> int:
#     return time.hour * 3600 + time.minute * 60 + time.second


def get_text_between(left: str, right: str, text: str):
    left_index = text.index(left) + len(left)
    right_index = left_index + text[left_index:].index(right)
    return text[left_index:right_index]


def get_clocks_and_hotel_stays(path: str):
    with open(path) as f:
        enters_and_leaves = list(
            filter(
                lambda line: "marker" in line,
                f.readlines()
            )
        )

        clocks, msgs = [], []
        for line in enters_and_leaves:
            clocks.append(
                int(
                    get_text_between(
                        left='|c:',
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
    return clocks, msgs


def get_alien_fraction(path: str):
    with open(path) as f:
        text = f.read()
        index_before_alien_type = text.index('f:')
        return text[index_before_alien_type + 2: index_before_alien_type + 3]


def msg_to_level(msg: str) -> int:
    if "Start" in msg:
        return -2
    elif "Stop" in msg:
        return 2
    elif "E" in msg:
        return 1
    elif "L" in msg:
        return -1
