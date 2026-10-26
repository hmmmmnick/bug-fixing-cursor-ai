# Bug Notes & Root Cause Analysis

| Bug | Evidence / Failed Test | Cause | Fix |
|---|---|---|---|
| **Average Calculation** | Got `135.0` instead of `90.0`; `ZeroDivisionError` on single mark `[40]` | Buggy code divided by `len(marks) - 1` | Changed denominator to `len(marks)` |
| **Pass Boundary** | Score of `40` returned `False` | Code used strict inequality `>` instead of `>=` | Changed condition to `mark >= PASS_MARK` |
| **Grade Ordering** | Score of `95` returned `"First"` instead of `"Distinction"` | `average >= 60` was checked before `average >= 90` | Reordered evaluation so `average >= 90` is checked first |