import argparse

def kaprekar(n:int, l:int):
    s = list(str(n).zfill(l))
    s.sort(reverse=False)
    a = int(''.join(s))
    s.sort(reverse=True)
    b = int(''.join(s))
    return b - a

def kaprekar_diffs(numbers:dict, l:int):
    diffs = set()
    for i in numbers:
        d = kaprekar(i, l)
        diffs.add(d)
    return diffs

def draw_kaprekar(numbers:dict, l:int, outfile:str=None):
    outfile = 'graph.txt' if outfile is None else outfile
    diff = set()
    graph = 'digraph G {'
    for i in numbers:
        d = kaprekar(i, l)
        diff.add(d)
        graph += f'{i} -> {d}\n'
    graph += '}'
    with open(outfile, 'w') as f:
        f.write(graph)
    print(f'outfile: {outfile}')
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='explore Kaprekar number')
    parser.add_argument("--digits", type=int, default=3, help="number of digits")
    parser.add_argument("--outfile", type=str, default=None, help="output file of graph")
    args = parser.parse_args()
    l = args.digits
    n = pow(10, l)
    numbers = [i for i in range(n)]
    diffs = kaprekar_diffs(numbers, l)
    print(f'diff ({len(diffs)}): {diffs}')
    draw_kaprekar(diffs, l, outfile=args.outfile)
