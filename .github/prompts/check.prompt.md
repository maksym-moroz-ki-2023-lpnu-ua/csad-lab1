# Command: check

Виконай неруйнівну валідацію проєкту:
1. Перевір наявність обов'язкових файлів: .gitignore, requirements.txt, src/app.py, tests/test_app.py, scripts/ci.sh, scripts/ci.bat, .github/workflows/ci.yml.
2. Перевір синтаксичну коректність YAML-файлу workflow через python yaml.safe_load.
3. Виконай локальний запуск тестів через python -m pytest tests/test_app.py.
