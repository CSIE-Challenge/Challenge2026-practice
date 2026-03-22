# Issue 5: Randomize Mines And Keep First Click Safe

## Goal

目前棋盤是固定的。請把地雷改成隨機生成，並保證第一次點擊不會踩到雷。

## Main File

`minesweeper/game/board.py`

## What To Do

- 不要再使用固定棋盤
- 改成遊戲開始後再生成地雷
- 第一下點擊的位置必須安全

## Constraints

- 主要修改集中在 `minesweeper/game/board.py`
- 不要把隨機生成地雷的核心邏輯塞進 UI
- 不要順手實作與這個 issue 無關的大量重構

## Acceptance Criteria

- 每次新遊戲的地雷配置不固定
- 第一次 reveal 的格子一定不是地雷
- 棋盤的鄰近地雷數會正確更新
- 既有 reveal 流程仍然能正常運作

## Suggested Commit Message

```bash
git commit -m "feat: randomize mines with safe first click"
```
