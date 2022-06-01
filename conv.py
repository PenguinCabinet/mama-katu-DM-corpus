#!/usr/bin/env python3

import os

def main():
    current = os.path.dirname(os.path.abspath(__file__))

    # replace '\n' to '__br__' and apply strip for UX
    with open(os.path.join(current, 'in_conv.txt'), 'rt', encoding='utf-8') as f:
        datum = f.read().strip().replace('\n', '__br__')

    # load corpus without empty-line and remove '\n' char
    with open(os.path.join(current, 'Mama_katu_DM_corpus.txt'), 'rt', encoding='utf-8') as f:
        corpus = [l.replace('\n', '') for l in f if not l.isspace()]

    if datum in corpus:
        print('This datum already exists in the corpus.')
        exit(1)

    corpus.append(datum)

    # join corpus with '\n' and add line terminator for unix like systems
    with open(os.path.join(current, 'Mama_katu_DM_corpus.txt'), 'wt', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(corpus) + '\n')

if __name__ == '__main__':
    main()
