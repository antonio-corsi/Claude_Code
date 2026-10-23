/statusline Set up a custom statusline with a bash script. 
Style: minimal
    with dim · separators and subtle ANSI colors (no 
backgrounds).
    Segments left to right:

    1. Git branch (cyan) — show  branchname with a dirty 
indicator:
    orange * for unstaged changes, yellow + for staged, +* 
for both.
    Only show when in a git repo.
    2. Model (blue) — show the model display name, followed 
by the
    effort level in dim parentheses (read from
    ~/.claude/settings.json's effortLevel).
    3. Context usage % — just the number and %. Green 
normally,
    yellow at 50%+, red at 80%+.

    No user/host, no directory, no "ctx" label.