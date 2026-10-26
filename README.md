# Bug Fixing Using Cursor AI (Lecture 8)

**Student Name:** Ambesh Mishra  
**University:** JECRC University  
**GitHub:** [@hmmmmnick](https://github.com/hmmmmnick)

---

## 📌 Overview
This repository documents identifying, testing, and fixing runtime defects in `student_utils.py` using **Cursor AI** following the test-driven **RED ➔ FIX ➔ GREEN** methodology.

## 🔄 The RED ➔ FIX ➔ GREEN Cycle
1. **RED:** Created 9 unit tests in `test_student_utils.py`. Initial run failed due to 3 defects (Division by zero, incorrect pass boundary, and flawed grade ordering).
2. **FIX:** Prompted Cursor AI to identify root causes and surgically refactored the buggy logic without altering test assertions.
3. **GREEN:** Reran the 9 test suites; all 9 tests passed cleanly with 100% assertions satisfied.

## 🧪 How to Run Tests
```bash
python test_student_utils.py