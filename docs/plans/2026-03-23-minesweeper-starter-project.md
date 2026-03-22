# Minesweeper Starter Project Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a small Textual-based TUI minesweeper starter project for Git collaboration practice, with five intentionally incomplete TODO areas mapped to future issues.

**Architecture:** Keep the codebase flat and readable. `ui/` owns Textual widgets and rendering, `game/` owns board data and rules, `utils/` holds tiny helpers, and `app.py` wires the app together. The starter should run, render an 8x8 board, and respond to left-click reveals without finishing flagging, flood fill, win/lose flow, or randomized mine generation.

**Tech Stack:** Python 3.12, Textual

---

### Task 1: Create the project skeleton

**Files:**
- Create: `minesweeper/`
- Create: `minesweeper/game/__init__.py`
- Create: `minesweeper/ui/__init__.py`
- Create: `minesweeper/utils/__init__.py`
- Create: `pyproject.toml`

**Step 1:** Create the package directories and placeholder Python package files.

**Step 2:** Add a minimal `pyproject.toml` with a Textual dependency and simple project metadata.

**Step 3:** Commit the scaffold.

### Task 2: Add the app shell

**Files:**
- Create: `minesweeper/app.py`

**Step 1:** Add a minimal Textual app that can mount a header, board view area, and footer/status line.

**Step 2:** Keep the app runnable with `uv run python app.py`.

**Step 3:** Commit the app shell.

### Task 3: Add initial game models

**Files:**
- Create: `minesweeper/game/board.py`
- Create: `minesweeper/game/logic.py`
- Create: `minesweeper/game/state.py`
- Create: `minesweeper/utils/helpers.py`

**Step 1:** Define a `Cell` model and a simple fixed board factory.

**Step 2:** Define a `GameState` object with board dimensions, board data, reveal API, and TODOs for win/lose evaluation.

**Step 3:** Define starter logic helpers for adjacency and reveal behavior, leaving flood fill unfinished as a TODO.

**Step 4:** Commit the initial game state model.

### Task 4: Add the clickable board UI

**Files:**
- Create: `minesweeper/ui/board_view.py`
- Create: `minesweeper/ui/widgets.py`
- Modify: `minesweeper/app.py`

**Step 1:** Add a `CellButton` widget that records its coordinates and reacts to left click.

**Step 2:** Add a `BoardView` container that renders the 8x8 board and updates the display after reveals.

**Step 3:** Leave separate TODOs in `ui/board_view.py` and `ui/widgets.py` for board styling and right-click flagging.

**Step 4:** Commit the board rendering and interaction.

### Task 5: Document the teaching workflow

**Files:**
- Create: `README.md`

**Step 1:** Explain that the repo is for Git collaboration practice.

**Step 2:** Document installation, running, the five TODO issues, and the required PR flow including `git fetch origin` and `git merge origin/main`.

**Step 3:** Commit the docs.

### Task 6: Verify and tidy

**Files:**
- Verify: `minesweeper/game/board.py`
- Verify: `minesweeper/game/logic.py`
- Verify: `minesweeper/game/state.py`
- Verify: `minesweeper/ui/board_view.py`
- Verify: `minesweeper/ui/widgets.py`

**Step 1:** Run a smoke check for syntax or app startup.

**Step 2:** Confirm each TODO is clearly labeled and primarily concentrated in the intended file.

**Step 3:** Review git history to ensure frequent, small commits with clear messages.
