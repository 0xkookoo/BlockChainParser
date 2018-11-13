#!/usr/bin/python
import sys
from Block import Block
from Crawler import *
import time


def parse(blockchain):
    time.sleep(2)
    print('Starting Parsing Block Chain block head, transaction etc.' + '.' * 20)
    print('Please wait 2 seconds' + '.' * 20)
    time.sleep(2)
    block = Block(blockchain)
    block.toString()
    print('All Done!' + '!' * 20)
    return block.txCount


def main():
    hash = sys.argv[1]
    print('Starting retrieving bitcoin ' + hash + '.bin file.' + '.' * 20)
    print('Please wait 2 seconds' + '.' * 20)
    time.sleep(2)
    try:
        crawler(hash)
        print(hash + '.bin file retrieved successfully!' + '!' * 20)
        with open(hash + '.bin', 'rb') as blockchain:
            txCount = parse(blockchain)
        return txCount
    except:
        return


if __name__ == '__main__':
    main()
