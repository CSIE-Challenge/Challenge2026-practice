# TUI Minesweeper Starter

這個專案是用來練習 Git 協作流程的。

這次的重點不是把踩地雷做完，而是要在同一個 repo 裡面練習：

- branch / git flow
- commit message
- pull request
- merge
- resolve conflict

專案本身是一個 Python + Textual 的終端機版踩地雷 starter project。它已經可以啟動、顯示 8x8 棋盤、用滑鼠左鍵點格子，但刻意留下 5 個 TODO，方便分工完成。

## 你現在要做什麼

1. 到 GitHub 看已經開好的 issue
2. 認領你要做的 issue
3. 從 `main` 開自己的 branch
4. 只修改自己負責的 TODO
5. commit、push、發 PR
6. 發 PR 前先把最新的 `main` merge 進來
7. 如果有 conflict，先在本地解完再 push

## 安裝與執行

先安裝依賴：

```bash
uv sync
```

啟動程式：

```bash
uv run python -m minesweeper.app
```

## 目前這個 starter project 已經有什麼

- 可以啟動 Textual App
- 可以顯示基本 8x8 grid
- 可以用滑鼠左鍵點擊格子
- 點擊後格子會從未翻開變成已翻開
- 程式已經拆成 `ui/` 和 `game/`，方便分工

## 你要認領的 5 個 TODO

這個 repo 會有 5 個對應 TODO 的 issue，可以挑一個認領。

1. `TODO 1` 加上座標並整理棋盤可讀性
   主要檔案：`minesweeper/ui/board_view.py`
   內容：加上 row / column 座標、讓座標與格子對齊、整理棋盤資訊層次與可讀性

2. `TODO 2` 支援右鍵旗標
   主要檔案：`minesweeper/ui/widgets.py`
   內容：右鍵可 flag / unflag，UI 要反映旗標狀態

3. `TODO 3` 實作 flood fill
   主要檔案：`minesweeper/game/logic.py`
   內容：點到空白格時，自動展開周圍區域

4. `TODO 4` 實作 win / lose 判斷
   主要檔案：`minesweeper/game/state.py`
   內容：踩到雷就輸、所有非雷格翻開就贏、UI 顯示目前結果

5. `TODO 5` 隨機生成地雷 + 第一下安全
   主要檔案：`minesweeper/game/board.py`
   內容：不要固定棋盤、遊戲開始後才生成雷、保證第一下不會踩到雷

## 建議的協作流程

### 1. 先從 `main` 開 branch

branch 名稱請清楚一點，例如：

```bash
git switch -c feat/flood-fill
```

或：

```bash
git switch -c feat/add-right-click-flag
```

### 2. 只做自己負責的 issue

請不要一口氣把其他 TODO 一起做完。這個 repo 是拿來練習協作，不是拿來單人全包。

### 3. commit message 要清楚

請不要用這種訊息：

```bash
git commit -m "update"
git commit -m "fix"
git commit -m "asdf"
```

請用這種有意義的訊息：

```bash
git commit -m "feat: add flood fill for empty cells"
git commit -m "feat: support right click flag toggle"
git commit -m "feat: add board coordinates and labels"
```

### 4. push 你的 branch

```bash
git push -u origin feat/flood-fill
```

### 5. 到 GitHub 發 PR

PR 內容至少要讓人看得懂：

- 你改了什麼
- 你怎麼測
- 還有哪些地方沒做

## 發 PR 前一定要先做這件事

在你送 PR 之前，先把遠端最新的 `main` 合進你自己的 branch：

```bash
git fetch origin
git merge origin/main
```

這一步不能跳過。

`main` 可能會持續出現新的修改，所以你很可能會遇到 conflict。這正是這次要練習的內容。

如果 merge 時出現 conflict，請照下面流程處理：

1. 打開衝突檔案
2. 看懂兩邊改了什麼
3. 手動保留正確版本
4. 存檔後重新 `git add`
5. 完成 merge
6. 再測一次程式能不能跑
7. 沒問題再 push

## 這次要模擬的情境

請把自己當成真的在團隊裡工作：

- 你只負責自己認領的 issue
- 你會和其他人同時改同一個 repo
- 你不能假設 `main` 永遠不變
- 你送 PR 前要先整合最新變更
- 你需要處理 merge conflict，而不是逃避它

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

## 提醒

- 先拉最新 `main` 再開始工作
- 發 PR 前一定要 `git fetch origin` 和 `git merge origin/main`
- 遇到 conflict 不要慌，先看懂再解
- commit message 要讓其他人看得懂
- 不要順手把其他 issue 一起做完
