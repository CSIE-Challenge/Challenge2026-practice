# TUI Minesweeper

Terminal 版踩地雷，使用 Python + Textual。

## Run

```bash
uv sync
uv run python -m minesweeper.app
```

## Controls

- `Click`: reveal cell
- `Right Click`: flag / unflag
- `Shift + Click`: fallback flag / unflag

## Features

- 8x8 board
- Random mines
- First reveal is always safe
- Flood fill for empty area
- Win / lose detection
- In-app game instructions
- Game result notification

## Development

PR 會自動檢查 Python formatting。

本地檢查：

```bash
uvx ruff format --check .
```

自動格式化：

```bash
uvx ruff format .
```

## Structure

```text
minesweeper/
├─ app.py
├─ game/
│  ├─ board.py
│  ├─ logic.py
│  └─ state.py
├─ ui/
│  ├─ board_view.py
│  └─ widgets.py
└─ utils/
   └─ helpers.py
```
