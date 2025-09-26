# MorseTree
This script uses a binary tree for decoding Morse code. Each dot represents a left traversal and each dash represents a right traversal in the tree. Symbols are separated by **one** space, and words are separated by **two** spaces.

For simplicity, a dictionary is used for the encoding.

## Morse Code Tree Structure
```mermaid
flowchart TD
root((root)) -->|dot| E((E))
root -->|dash| T((T))
E -->|dot| I((I))
E -->|dash| A((A))
T -->|dot| N((N))
T -->|dash| M((M))
I -->|dot| S((S))
I -->|dash| U((U))
A -->|dot| R((R))
A -->|dash| W((W))
N -->|dot| D((D))
N -->|dash| K((K))
M -->|dot| G((G))
M -->|dash| O((O))
S -->|dot| H((H))
S -->|dash| V((V))
U -->|dot| F((F))
R -->|dot| L((L))
W -->|dot| P((P))
W -->|dash| J((J))
D -->|dot| B((B))
D -->|dash| X((X))
K -->|dot| C((C))
K -->|dash| Y((Y))
G -->|dot| Z((Z))
G -->|dash| Q((Q))
```

## How to run the script
1. Clone and run locally:
```bash
git clone https://github.com/andreas-hkr/MorseTree.git
cd MorseTree
python3 main.py
```
2. Fetch and run directly:
```bash
curl -L https://raw.githubusercontent.com/andreas-hkr/MorseTree/main/main.py | python3
```

**WARNING:** The direct fetch method may pose security risks. Review the code before executing it.
