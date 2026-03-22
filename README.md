# TUI Minesweeper Starter

這是一個用來做 Git 協作教學的 Textual 踩地雷 starter project。

重點不是把遊戲做完整，而是讓學生在同一個 repo 上分組認領 issue、各自在自己的 branch 開發、送出 PR，並在合併 `main` 時練習處理 conflict。

## 專案簡介

- 使用 Python + Textual 建立終端機版踩地雷介面
- 目前可以啟動 app、顯示 8x8 棋盤、用滑鼠左鍵點擊格子
- 刻意保留 5 個清楚的 TODO，對應 5 個可認領的 issue
- UI 與遊戲邏輯分開，方便不同小組分工

## 安裝與執行

```bash
uv sync
uv run python -m minesweeper.app
```

## 五個 TODO / Issue 對應

1. `TODO 1` 改善棋盤渲染
   主要檔案：`minesweeper/ui/board_view.py`
2. `TODO 2` 支援右鍵旗標
   主要檔案：`minesweeper/ui/widgets.py`
3. `TODO 3` 實作 flood fill
   主要檔案：`minesweeper/game/logic.py`
4. `TODO 4` 實作 win / lose 判斷
   主要檔案：`minesweeper/game/state.py`
5. `TODO 5` 隨機生成地雷 + 第一下安全
   主要檔案：`minesweeper/game/board.py`

## 教學情境

這個 repo 預期搭配以下流程使用：

- 教師先在 GitHub 上建立 5 個 issue
- 學生分組認領 issue
- 每組從 `main` 開自己的 `feat/xxx` branch
- 每組只處理自己負責的 TODO
- 完成後 push branch 並送出 PR
- 發 PR 前先把最新的 `main` 合進自己的 branch
- 教師可以刻意在 `main` 的不同檔案做一些小修改，讓學生在 merge 時練習 resolve conflict

## 學生協作流程

1. 從 `main` 開自己的 branch

```bash
git switch -c feat/xxx
```

2. 完成自己認領的 issue
3. 使用清楚的 commit message 提交，例如：

```bash
git commit -m "feat: add flood fill for empty cells"
```

4. push branch

```bash
git push -u origin feat/xxx
```

5. 到 GitHub 發 Pull Request

## PR 前必做

送出 PR 前，先同步遠端 `main`，並把最新變更 merge 進自己的 branch：

```bash
git fetch origin
git merge origin/main
```

如果有 conflict，先在本地解完、測試確認能執行，再 push 更新後的 branch。

## 專案結構

```text
.
├─ minesweeper/
│  ├─ app.py
│  ├─ game/
│  │  ├─ board.py
│  │  ├─ logic.py
│  │  └─ state.py
│  ├─ ui/
│  │  ├─ board_view.py
│  │  └─ widgets.py
│  └─ utils/
│     └─ helpers.py
├─ README.md
└─ pyproject.toml
```

## 目前已完成的最小功能

- 可以啟動 Textual App
- 可以顯示基本 8x8 grid
- 可以用滑鼠左鍵點擊格子
- 點擊後格子會從未翻開變成已翻開
- 架構已拆成 `ui/` 與 `game/`，方便後續協作
