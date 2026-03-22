# Issue 1: Add Board Coordinates And Improve Readability

## Goal

目前棋盤已經有基本樣式，但還缺少座標與更明確的資訊層次。請補上 row / column 座標，並整理棋盤可讀性，讓使用者更容易辨識位置與狀態。

## Main File

`minesweeper/ui/board_view.py`

## What To Do

- 加上座標顯示
- 讓座標和格子對齊
- 整理棋盤區塊的資訊層次，讓位置與狀態更容易閱讀
- 在不大幅重做版面的前提下，補強可讀性細節

## Constraints

- 保持使用 Textual
- 不要把遊戲邏輯塞進 `ui/`
- 不要把這個 issue 擴大成整體重做 UI
- 不要順手實作右鍵旗標、flood fill、win / lose、隨機生成地雷

## Acceptance Criteria

- 棋盤仍然可以正常顯示與左鍵點擊
- 使用者可以清楚辨識 row / column
- 座標和格子在視覺上對得齊
- 棋盤資訊比現在更容易閱讀
- 沒有破壞現有 app 啟動流程

## Suggested Commit Message

```bash
git commit -m "feat: add board coordinates and labels"
```
