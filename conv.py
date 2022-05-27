#!/usr/bin/env python3

def main():
    with open('in_conv.txt', 'rt', encoding='utf-8') as f:
        datum = f.read().replace('\n', '__br__')

    # load corpus without empty-line and remove '\n' char
    with open('Mama_katu_DM_corpus.txt', 'rt', encoding='utf-8') as f:
        corpus = [l.replace('\n', '') for l in f if not l.isspace()]

    if datum in corpus:
        print('This datum already exists in the corpus.')
        exit(1)

    corpus.append(datum)

    # join corpus with '\n' and add line terminator for unix like systems
    with open('Mama_katu_DM_corpus.txt', 'wt', encoding='utf-8') as f:
        f.write('\n'.join(corpus) + '\n')

if __name__ == '__main__':
    main()
