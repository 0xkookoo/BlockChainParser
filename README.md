This project is inspired by 

1. [block-parser-how-read-bitcoin-block-chain](https://www.ccn.com/block-parser-how-read-bitcoin-block-chain/)
2. [blocktools](https://github.com/tenthirtyone/blocktools)
3. [7daystalk-01](https://baya.github.io/2017/05/11/7daystalk.html)


## Block Chain Tools

Block chain parser implementation written in python. Contains examples for Bitcoin and Litecoin.

- Crawler.py - use valid hash as input and download corresponding .bin file from [webbtc.com](https://webbtc.com/)
- Parser.py - 
    - Decode the header and display it to the terminal.
    - Decode top 5 tx and display it to the terminal
- BlockTools.py - tools for reading binary data from block files
- Block.py - classes for Blocks, Transactions
- Unittest.py - test file
- OPcode.py - some encoding info


## Usage

This project is currently not compatible with python3, may improve later.

```bash
python2 Parser.py 0000000000000000000cdc0d2a9b33c2d4b34b4d4fa8920f074338d0dc1164dc
```


## License

MIT © [Lisanaaa](https://github.com/Lisanaaa)
