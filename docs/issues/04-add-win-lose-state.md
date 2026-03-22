# Issue 4: Add Win / Lose State

## Goal

目前程式可以 reveal 格子，但還不會判斷遊戲是否結束。請補上 win / lose 判斷，並讓 UI 能顯示目前結果。

## Main File

`minesweeper/game/state.py`

## What To Do

- 踩到地雷時判定為 lose
- 所有非雷格都翻開時判定為 win
- 更新狀態文字，讓畫面能顯示目前結果

## Constraints

- 遊戲狀態判斷集中在 `game/state.py`
- 不要把主要判斷邏輯塞進 UI
- 不要順手實作隨機生成地雷

## Acceptance Criteria

- reveal 到地雷時可以判定失敗
- 所有非雷格都 reveal 後可以判定成功
- 畫面上的狀態文字會反映目前結果
- 遊戲狀態 API 清楚，像是 `is_win()`、`is_lose()`

## Suggested Commit Message

```bash
git commit -m "feat: add win and lose state handling"
```

