# 🔤 Scrabble in Python — From Procedural Game to AI Agents

A complete implementation of a **Portuguese-language Scrabble** game in pure Python, built in two stages for the *Fundamentos de Programação* (Programming Fundamentals) course at **Instituto Superior Técnico (IST), University of Lisbon**.

The repository contains both course projects, which show the same game evolving from a **procedural, human-only** implementation into a **data-abstraction-based engine with a dictionary and computer-controlled players** of three difficulty levels.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Course](https://img.shields.io/badge/course-Fundamentos%20de%20Programa%C3%A7%C3%A3o-orange)
![University](https://img.shields.io/badge/IST-Universidade%20de%20Lisboa-lightgrey)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Part 1 vs. Part 2](#️-part-1-vs-part-2-at-a-glance)
- [Repository Structure](#-repository-structure)
- [Getting Started](#-getting-started)
- [How to Play](#-how-to-play)
- [Part 1 — Procedural Scrabble](#-part-1--procedural-scrabble)
- [Part 2 — Scrabble2: ADTs, Vocabulary and AI Agents](#-part-2--scrabble2-adts-vocabulary-and-ai-agents)
- [Concepts Practised](#-concepts-practised)
- [Academic Context](#-academic-context)
- [Author](#-author)

---

## 🎯 Overview

Both projects implement the core Scrabble loop on a **15×15 board** for **2 to 4 players**:

- A shuffled bag of letter tiles, from which each player draws **7 letters**.
- On each turn a player can **play** a word, **exchange** tiles, or **pass**.
- The first word must cover the **centre square (8, 8)**.
- The game ends when **every player passes consecutively**, or when a player **runs out of letters and the bag is empty**.
- The final result is a tuple with each player's score.

The tile shuffle is **deterministic**: it uses a 32-bit **xorshift** pseudo-random number generator seeded by the caller, followed by a Fisher–Yates-style permutation. The same seed always yields the same game, which makes the engine easy to test.

---

## ⚖️ Part 1 vs. Part 2 at a Glance

| Aspect | **Part 1** — `FP2526P1.py` | **Part 2** — `FP2526P2.py` |
|---|---|---|
| **Paradigm** | Procedural, with plain data structures | Data abstraction: Abstract Data Types (ADTs) with constructors, selectors, recognisers, tests and transformers |
| **Entry point** | `scrabble(jogadores, saco, pontos, seed)` | `scrabble2(jogadores, nome_fich, seed)` |
| **Players** | Human only (hot-seat, 2–4) | Humans **and** AI agents (`@FACIL`, `@MEDIO`, `@DIFICIL`) |
| **Board** | List of 15 lists with 15 strings each | Sparse dictionary `{(row, col): letter}` that only stores occupied squares |
| **Letter bag & scores** | Passed in by the caller as dictionaries (`saco`, `pontos`) | Built into the engine (117 tiles, fixed Portuguese point table) |
| **Player's letters** | Dictionary of letter → count | List of letters, rendered as a sorted string |
| **Word validation** | Only checks that the word fits the board and the player has the letters | Every played word must exist in a **vocabulary** loaded from a text file |
| **Vocabulary** | ❌ none | ✅ ADT indexed by *length → first letter → word*, with precomputed scores |
| **Pattern search** | Single-word check against a pattern (`testa_palavra_padrao`) | Full pattern generation across rows and columns plus best-word search |
| **Scoring** | Sum of letter values of the played word | Sum of letter values, looked up from the vocabulary |
| **Player identity** | Numeric id (`J1`, `J2`, …) | Named humans (`"Alice"`) and bots (`"@DIFICIL"`) |
| **Extra** | — | Optional Pygame graphical front-end |

In short: **Part 1 proves the rules work between humans; Part 2 rebuilds the engine around ADTs and adds a dictionary and an AI opponent.**

---

## 📁 Repository Structure

```text
.
├── README.md
├── part1/
│   └── FP2526P1.py          # Procedural Scrabble (human players only)
└── part2/
    ├── FP2526P2.py          # Scrabble2 engine: ADTs + vocabulary + AI agents
    └── vocab25k.txt         # ~25,000-word Portuguese vocabulary
```

> The course submission system requires each part to be a **single** `.py` file. This repository keeps that constraint: all game logic lives in `FP2526P1.py` and `FP2526P2.py`, and the GUI is an extra layer on top.

---

## 🚀 Getting Started

### Requirements

- **Python 3.10+**

No other third-party dependencies are needed.


### Run Part 1

```python
# from inside part1/
from FP2526P1 import scrabble

# Tile bag: letter -> number of tiles
saco = {
    'A': 14, 'B': 3, 'C': 4, 'Ç': 2, 'D': 5, 'E': 11, 'F': 2, 'G': 2,
    'H': 2, 'I': 10, 'J': 2, 'L': 5, 'M': 6, 'N': 4, 'O': 10, 'P': 4,
    'Q': 1, 'R': 6, 'S': 8, 'T': 5, 'U': 7, 'V': 2, 'X': 1, 'Z': 1,
}

# Letter values: letter -> points
pontos = {
    'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 4,
    'H': 4, 'I': 1, 'J': 5, 'L': 2, 'M': 1, 'N': 3, 'O': 1, 'P': 2,
    'Q': 6, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8,
}

# 2 players, seed 32
resultado = scrabble(2, saco, pontos, 32)
print(resultado)   # tuple with each player's final score
```

### Run Part 2

```python
# from inside part2/
from FP2526P2 import scrabble2

# One human against a hard bot, seed 32
resultado = scrabble2(("Alice", "@DIFICIL"), "vocab25k.txt", 32)
print(resultado)

# Bots can also play each other
scrabble2(("@FACIL", "@MEDIO", "@DIFICIL"), "vocab25k.txt", 7)
```

---

## 🎮 How to Play

At each prompt, enter one of three commands:

| Command | Format | Meaning |
|---|---|---|
| **Play** | `J <row> <col> <dir> <word>` | Place `<word>` starting at `(row, col)`, horizontally (`H`) or vertically (`V`) |
| **Exchange** | `T <letters…>` | Swap the listed letters for new ones from the bag (requires **≥ 7 tiles** left in the bag) |
| **Pass** | `P` | Skip the turn |

**Examples**

```text
Jogada Alice: J 8 5 H CASA     → plays CASA from (8,5) to (8,8), covering the centre
Jogada Alice: T A E            → exchanges one A and one E
Jogada Alice: P                → passes
```

Invalid commands are simply rejected and the prompt is shown again until a valid move is entered.

**Rules enforced**

1. The first word must be at least 2 letters long and cover **(8, 8)**.
2. Later words must **reuse at least one letter already on the board** and place **at least one new letter**.
3. The word must fit the board, and the player must hold every letter that is not already on the board.
4. *(Part 2 only)* The word must exist in the loaded vocabulary.
5. After a move, the player refills their rack from the bag.

**Board display**

```text
                       1 1 1 1 1 1
     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5
   +-------------------------------+
 1 | . . . . . . . . . . . . . . . |
 2 | . . . . . . . . . . . . . . . |
 3 | . . . . . . . . . . . . . . . |
 4 | . . . . . . . . . . . . . . . |
 5 | . . . . . . . . . . . . . . . |
 6 | . . . . . . . . . . . . . . . |
 7 | . . . . . . . . . . . . . . . |
 8 | . . . . C A S A . . . . . . . |
 9 | . . . . . . . . . . . . . . . |
10 | . . . . . . . . . . . . . . . |
11 | . . . . . . . . . . . . . . . |
12 | . . . . . . . . . . . . . . . |
13 | . . . . . . . . . . . . . . . |
14 | . . . . . . . . . . . . . . . |
15 | . . . . . . . . . . . . . . . |
   +-------------------------------+
```

---

## 🧱 Part 1 — Procedural Scrabble

**File:** `part1/FP2526P1.py`

The first project builds the game from the ground up with lists and dictionaries.

### Data representations

| Concept | Representation |
|---|---|
| Letter set (`conjunto`) | `dict` — `{letter: count}` |
| Board (`tabuleiro`) | `list` of 15 `list`s of 15 single-character strings (`'.'` = empty) |
| Square (`casa`) | `tuple` `(row, col)` with both values in `1…15` |
| Player (`jogador`) | `dict` — `{"id": int, "pontos": int, "letras": conjunto}` |
| Bag (`pilha`) | `list` of letters, drawn from the end |

### Main functions

- **Letter sets & shuffling:** `cria_conjunto`, `gera_numero_aleatorio` (xorshift32), `permuta_letras`, `baralha_conjunto`
- **Pattern matching:** `testa_palavra_padrao` — can a word be formed from a pattern like `"C.S."` using the letters in a set?
- **Board:** `cria_tabuleiro`, `cria_casa`, `obtem_valor`, `insere_letra`, `obtem_sequencia`, `insere_palavra`, `tabuleiro_para_str`
- **Players:** `cria_jogador`, `jogador_para_str`, `distribui_letra`
- **Game flow:** `joga_palavra` (validates and applies a word), `processa_jogada` (one full turn with input handling), `scrabble` (full game loop)

### Limitations (by design)

Part 1 has **no dictionary**: it validates *placement* and *tile ownership*, but any sequence of letters is accepted as a word. This gap is exactly what Part 2 addresses.

---

## 🤖 Part 2 — Scrabble2: ADTs, Vocabulary and AI Agents

**File:** `part2/FP2526P2.py`

The second project rewrites the engine around **Abstract Data Types**, so that the rest of the program only touches data through well-defined operations. It adds a **vocabulary** and **computer-controlled players**.

### ADTs

| ADT | Internal representation | Key operations |
|---|---|---|
| **Casa** (square) | `tuple (row, col)` | `cria_casa`, `obtem_lin`, `obtem_col`, `eh_casa`, `casas_iguais`, `casa_para_str`, `str_para_casa`, `incrementa_casa` |
| **Jogador** (player) | `dict` with name *or* level, points, letters | `cria_humano`, `cria_agente`, `jogador_identidade`, `jogador_pontos`, `jogador_letras`, `recebe_letra`, `usa_letra`, `soma_pontos`, `eh_humano`, `eh_agente`, `jogadores_iguais`, `jogador_para_str` |
| **Vocabulário** | Nested `dict`: `length → first letter → {word: points}` | `cria_vocabulario`, `obtem_pontos`, `obtem_palavras`, `testa_palavra_padrao`, `ficheiro_para_vocabulario`, `vocabulario_para_str`, `procura_palavra_padrao` |
| **Tabuleiro** (board) | Sparse `dict {casa: letter}` | `cria_tabuleiro`, `obtem_letra`, `insere_letra`, `eh_tabuleiro`, `eh_tabuleiro_vazio`, `tabuleiros_iguais`, `tabuleiro_para_str`, `obtem_padrao`, `insere_palavra`, `obtem_subpadroes`, `gera_todos_padroes` |

Constructors **validate their arguments** and raise a `ValueError` with a specific message (e.g. `cria_casa: argumentos inválidos`) on invalid input.

### The vocabulary

Words are loaded from a plain-text file (one word per line, blank lines ignored). Only words that are **2–15 letters long** and use letters of the **Portuguese alphabet** are kept, and they are converted to upper case.

Indexing words by *length → first letter* is what makes the AI search fast: when a pattern starts with a known letter, only the relevant bucket has to be scanned. Within each bucket, `obtem_palavras` returns words **sorted by score (descending)**.

A word's score is the **sum of its letters' values** (A = 1, B = 3, … X = 8, Z = 8).

### Patterns

A **pattern** is a string describing a line segment of the board, where letters are fixed and `.` is a free square, for example `"..S.A"`.

- `obtem_padrao` extracts the pattern between two squares.
- `obtem_subpadroes` splits a full row or column into every **viable sub-pattern** with at most *l* free squares. A sub-pattern is discarded if it:
  1. contains no letters at all,
  2. contains no free squares, or
  3. is directly preceded or followed by another letter (the word would not be properly bounded).
- `gera_todos_padroes` collects the sub-patterns of all 15 rows, then all 15 columns, together with their start squares and directions.
- `procura_palavra_padrao` finds the **highest-scoring vocabulary word** that fits a pattern using only the available letters, with a minimum score threshold.

### AI agents

An agent is created with `@LEVEL` in the players tuple. On its turn it follows this strategy:

1. **Empty board → pass.** Agents never open the game.
2. Generate all viable patterns for its current rack.
3. **Sample the patterns**, keeping one out of every *N*:

| Level | N | Behaviour |
|---|---|---|
| `@FACIL` (easy) | 100 | Looks at very few options, so it plays weakly |
| `@MEDIO` (medium) | 50 | Moderate search |
| `@DIFICIL` (hard) | 10 | Examines many patterns, so it plays strongly |

4. For each sampled pattern, call `procura_palavra_padrao`, requiring a score strictly better than the best found so far.
5. **Play** the best word found. If none exists, **exchange the whole rack** when the bag holds ≥ 7 tiles; otherwise **pass**.

Difficulty therefore comes from a single parameter: *how much of the search space the agent is willing to look at*.

### Game function

```python
scrabble2(jogadores, nome_fich, seed) -> tuple
```

| Argument | Type | Description |
|---|---|---|
| `jogadores` | `tuple[str]` | 2–4 entries in playing order. Plain strings are human names; `"@FACIL"`, `"@MEDIO"` or `"@DIFICIL"` create bots |
| `nome_fich` | `str` | Path to the vocabulary file |
| `seed` | `int > 0` | Seed for the xorshift shuffle |

Returns a tuple with each player's final score, in playing order. Raises `ValueError('scrabble2: argumentos inválidos')` for invalid arguments.

---

By default it launches a game of `("Tu", "@FACIL", "@MEDIO")` using `vocab25k.txt` and seed `32`; edit the bottom of the file to change that.

> ⚠️ The GUI is an experimental extra and is not part of the graded submission.

---

## 🧠 Concepts Practised

- **Data abstraction**: separating the use of data from its representation (ADTs)
- **Defensive programming**: validating arguments and raising informative errors
- **Destructive vs. non-destructive operations**: knowing exactly which functions mutate their inputs
- **Dictionaries as indexes**: nested hash maps for fast vocabulary look-ups
- **Pseudo-random number generation**: xorshift32 and in-place permutation
- **Search & heuristics**: trading accuracy for speed by sampling the search space
- **String processing and file I/O**
- **Reproducibility**: deterministic games via explicit seeds

---

## 🎓 Academic Context

These projects were developed for **Fundamentos de Programação** (1st year, Instituto Superior Técnico, Universidade de Lisboa), a first programming course focused on Python and algorithmic thinking. Function docstrings and error messages are in **Portuguese**, as required by the course specification.

If you are currently enrolled in the course, please follow your institution's academic integrity policy and use this repository as a reference only.

---

## 👤 Author

**Cristiano Suranyi** — [GitHub](https://github.com/Cristiano-Suranyi) · [LinkedIn](https://www.linkedin.com/in/Cristiano-Suranyi)

*Computer Science and Engineering student at Instituto Superior Técnico.*

---

⭐ If you found this project interesting, feel free to star the repository!
