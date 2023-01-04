if __name__ == '__main__':

    lines_dict = {}
    with open('files/all.txt', mode='r') as f:
        for line in f.readlines():
            r_idx = line.index('r:')
            line_after_r_idx = line[r_idx:].index('|')
            rank = int(line[r_idx + 2:r_idx + line_after_r_idx])
            if rank not in lines_dict:
                lines_dict[rank] = []
            lines_dict[rank].append(line)

    for rank, lines in lines_dict.items():
        with open(f'files/alien{rank}.txt', mode='w') as f:
            for ln in lines:
                f.write(ln)
