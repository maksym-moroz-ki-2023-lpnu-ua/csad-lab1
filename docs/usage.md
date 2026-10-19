# Інструкція користувача та запуск AI-агента

## 1. Опис команд AI-агента
Взаємодія з AI-агентом побудована на базі промптів у директорії `.github/prompts/` та навичок у `.github/skills/`.

### Доступні команди:
1. **`git-init`** (`.github/prompts/git-init.prompt.md`): Перевіряє стан Git-репозиторію та налаштовує `.gitignore`.
2. **`create-project`** (`.github/prompts/create-project.prompt.md`): Створює структуру проєкту та код у `src/app.py`.
3. **`create-build`** (`.github/prompts/create-build.prompt.md`): Налаштовує віртуальне оточення, `requirements.txt`, тести `tests/test_app.py` та скрипти збірки `scripts/ci.sh` / `scripts/ci.bat`.
4. **`create-actions`** (`.github/prompts/create-actions.prompt.md`): Створює конфігурацію GitHub Actions `.github/workflows/ci.yml`.
5. **`check`** (`.github/prompts/check.prompt.md`): Виконує неруйнівну комплексну перевірку цілісності файлів, синтаксису YAML та запуск тестів.
6. **`init`** (`.github/prompts/init.prompt.md`): Оркестратор, який запускає всі вищезазначені команди послідовно за принципом Fail-Fast.

---

## 2. Локальний запуск перевірки та складання

### На операційній системі Windows:
Відкрийте командний рядок (CMD або PowerShell) у корені проєкту та виконайте:
```cmd
.\scripts\ci.bat
```

### На операційних системах Linux або macOS:
Відкрийте термінал Bash у корені проєкту та виконайте:
```bash
./scripts/ci.sh
```

---

## 3. Ручна перевірка коректності проєкту (команда check)
Для неруйнівної перевірки працездатності коду та валідації синтаксису:
```powershell
# 1. Валідація синтаксису YAML
python -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"

# 2. Запуск тестів pytest
python -m pytest tests/test_app.py

# 3. Перевірка запуску головної програми
python src/app.py
```
