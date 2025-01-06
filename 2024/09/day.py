import sys
import os.path


def expand_diskmap(diskmap):
    blocks = []
    cur_id = 0
    for i, num_blocks in enumerate(diskmap):
        if i % 2 == 0:
            blocks.extend([cur_id for _ in range(num_blocks)])
            cur_id += 1
        else:
            blocks.extend(['.' for _ in range(num_blocks)])
    return blocks


def advance_left(blocks, index):
    while index < len(blocks) and blocks[index] != '.':
        index += 1
    count = 1
    while index + count < len(blocks) and blocks[index+count] == '.':
        count += 1
    return index, count


def advance_right(blocks, index):
    while blocks[index] == '.':
        index -= 1
    count = 1
    while index > 0 and blocks[index-1] == blocks[index]:
        index -= 1
        count += 1
    return index, count


def compute_checksum(blocks):
    return sum([index * block for index, block in enumerate(blocks) if block != '.'])


def part01(diskmap):
    blocks = expand_diskmap(diskmap)
    left, _ = advance_left(blocks, 0)
    right, block_len = advance_right(blocks, len(blocks) - 1)
    right += block_len - 1
    while left < right:
        blocks[left], blocks[right] = blocks[right], blocks[left]
        left, _ = advance_left(blocks, left)
        right, block_len = advance_right(blocks, right)
        right += block_len - 1
    return blocks


def part02(diskmap):
    blocks = expand_diskmap(diskmap)
    right, rlen = advance_right(blocks, len(blocks) - 1)
    while right >= 0:
        left, llen = advance_left(blocks, 0)
        while llen < rlen and left < right:
            left, llen = advance_left(blocks, left+llen)
        if left < right and llen >= rlen:
            blocks[left:left+rlen], blocks[right:right+rlen] = blocks[right:right+rlen], blocks[left:left+rlen]
        right, rlen = advance_right(blocks, right-1)
    return blocks


if __name__ == "__main__":
    stem, _ = os.path.splitext(__file__)
    match sys.argv[1]:
        case "test":
            filepath = stem + '.test'
        case "input":
            filepath = stem + '.input'
    with open(filepath) as f:
        diskmap = [int(c) for c in f.read().strip()]
    rearranged = part01(diskmap)
    print(compute_checksum(rearranged))
    rearranged = part02(diskmap)
    print(compute_checksum(rearranged))
