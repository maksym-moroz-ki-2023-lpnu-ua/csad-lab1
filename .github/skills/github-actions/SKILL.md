# Skill: github-actions

## Призначення
Створення файлу конфігурації .github/workflows/ci.yml із матрицею для Windows, Linux та macOS.

## Вхідні дані
- Скрипти запуску `scripts/ci.sh` та `scripts/ci.bat`.

## Вихідні результати
- `.github/workflows/ci.yml`

## Перевірка
Наявність у workflow матриці з трьох ОС (ubuntu-latest, windows-latest, macos-latest) та запуск виключно скриптів збірки.

## Сценарій помилки
Якщо файл конфігурації пошкоджено або він містить прямі команди замість скриптів, валідація не проходить.
