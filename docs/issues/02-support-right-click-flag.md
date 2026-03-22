# Issue 2: Support Right-Click Flag

## Goal

目前格子只有左鍵 reveal。請補上右鍵旗標功能，讓使用者可以對格子 flag / unflag，並且在 UI 上看得出來。

## Main File

`minesweeper/ui/widgets.py`

## What To Do

- 支援右鍵點擊格子
- 右鍵時可以 flag / unflag
- flagged 狀態要在畫面上有清楚的表示

## Constraints

- 不要改成滑鼠左鍵旗標
- 不要順手實作 flood fill、win / lose、隨機生成地雷
- 如果需要補少量串接程式碼，可以改其他檔案，但主要修改集中在 `minesweeper/ui/widgets.py`

## Acceptance Criteria

- 右鍵點擊未翻開格子時可以切換旗標狀態
- 已被旗標的格子在 UI 上有明顯標示
- 左鍵 reveal 的既有功能仍然正常
- 已翻開格子的行為合理，不會被錯誤 flag

## Suggested Commit Message

```bash
git commit -m "feat: support right click flag toggle"
```

