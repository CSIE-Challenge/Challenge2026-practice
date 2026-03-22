# Issue 3: Implement Flood Fill

## Goal

目前點到空白格只會翻開單一格。請補上 flood fill，讓空白格被點開時可以自動展開周圍區域。

## Main File

`minesweeper/game/logic.py`

## What To Do

- 當格子不是地雷，且周圍地雷數為 `0` 時，自動展開鄰近區域
- 邊界數字格也要一併 reveal
- 避免重複 reveal 或無限遞迴

## Constraints

- 邏輯放在 `game/`
- 不要把 flood fill 寫進 UI widget
- 不要順手實作 win / lose 或隨機生成地雷

## Acceptance Criteria

- 點擊空白格時，不只 reveal 單一格
- 周圍相連的空白區域會一起展開
- 邊界的數字格會被正確 reveal
- 既有單格 reveal 行為沒有被破壞

## Suggested Commit Message

```bash
git commit -m "feat: add flood fill for empty cells"
```

