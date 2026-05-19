# 🎓 Student Grade Calculator

A simple collaborative project to practice Git branching and teamwork.

---

## 👥 Who works on what?

| Person | File | Job |
|--------|------|-----|
| **You** | `grades.py` | Core grade logic |
| **Friend** | `report.py` | Report & display |

---

## 🚀 Setup (both people do this once)

```bash
# 1. Clone the repo
git clone <your-repo-url>
cd grade-calculator

# 2. Create YOUR branch (use your name)
git checkout -b feature/your-name
```

---

## 🔀 Git Workflow

### Your flow (working on grades.py):
```bash
git checkout -b feature/alice        # create your branch
# ... make changes to grades.py ...
git add grades.py
git commit -m "Add average calculation"
git push origin feature/alice        # push YOUR branch
# Open a Pull Request on GitHub → get reviewed → merge
```

### Friend's flow (working on report.py):
```bash
git checkout -b feature/bob          # their own branch
# ... make changes to report.py ...
git add report.py
git commit -m "Add report formatter"
git push origin feature/bob          # push THEIR branch
# Open a Pull Request on GitHub → get reviewed → merge
```

### ✅ Both can push at the same time — no waiting!

---

## 💥 To simulate a conflict (fun exercise!)

Both of you edit the **same line** in `main.py`, then try to merge.
Git will flag it. Practice resolving it!
