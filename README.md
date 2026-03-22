# TUI Minesweeper Starter

Python + Textual 的踩地雷 starter project，用來練習 branch、commit、PR、merge、resolve conflict。

## Run

```bash
uv sync
uv run python -m minesweeper.app
```

## Current Status

- 可以啟動 Textual app
- 可以顯示 8x8 棋盤
- 可以用滑鼠左鍵 reveal 格子
- 有基本 `GameState` / board / UI 分層
- 刻意保留 5 個 TODO 給協作練習

## TODO / Issue Mapping

1. `TODO 1` 座標與棋盤可讀性
   File: `minesweeper/ui/board_view.py`
2. `TODO 2` 右鍵旗標
   File: `minesweeper/ui/widgets.py`
3. `TODO 3` flood fill
   File: `minesweeper/game/logic.py`
4. `TODO 4` win / lose 判斷
   File: `minesweeper/game/state.py`
5. `TODO 5` 隨機地雷與第一下安全
   File: `minesweeper/game/board.py`

## Workflow

```bash
git switch -c feat/your-task
```

只改自己認領的 issue，commit message 要清楚。

送 PR 前先同步 `main`：

```bash
git fetch origin
git merge origin/main
```

有 conflict 就先在本地解完，再 push。

## PR Check

PR 會自動檢查 Python formatting。

本地可先跑：

```bash
uvx ruff format --check .
```

需要自動格式化時：

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
