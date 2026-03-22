# Issue 1: Improve Board Rendering

## Goal

目前棋盤可以顯示、可以點擊，但畫面還很基本。請把棋盤顯示方式整理得更清楚，讓使用者更容易理解目前的位置與狀態。

## Main File

`minesweeper/ui/board_view.py`

## What To Do

- 改善 grid 的視覺呈現
- 加上座標顯示
- 加上基本顏色或更清楚的狀態區分

## Constraints

- 保持使用 Textual
- 不要把遊戲邏輯塞進 `ui/`
- 不要順手實作右鍵旗標、flood fill、win / lose、隨機生成地雷

## Acceptance Criteria

- 棋盤仍然可以正常顯示與左鍵點擊
- 使用者可以清楚辨識列與欄
- revealed / unrevealed 的差異比現在更明顯
- 沒有破壞現有 app 啟動流程

## Suggested Commit Message

```bash
git commit -m "feat: improve board rendering"
```

