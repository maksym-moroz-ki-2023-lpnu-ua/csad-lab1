# Command: init (Orchestrator)

Виконай послідовну ініціалізацію проєкту за принципом fail-fast:
1. Запусти команду `git-init` для налаштування Git та .gitignore.
2. Запусти команду `create-project` для створення структури та коду `src/app.py`.
3. Запусти команду `create-build` для налаштування venv, requirements.txt, pytest та скриптів ci.sh / ci.bat.
4. Запусти команду `create-actions` для генерації .github/workflows/ci.yml.
5. Запусти команду `check` для неруйнівної перевірки всієї структури, валідації синтаксису YAML та запуску тестів pytest.

Якщо будь-який крок завершується з ненульовим кодом помилки, негайно зупини процес (fail-fast).
