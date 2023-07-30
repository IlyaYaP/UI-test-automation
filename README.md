# Небольшой проект по автоматизации тестирования UI.
### Стек технологий:
Стек: Python, Pytest, Selenium, Allure.
- Автоматизация тестирования UI с использованием GitHub Actions и генерацией Allure-отчетов в GitHub Pages.

# Локальный запуск:
- Клонируем данный репозиторий:
```
git clone https://github.com/IlyaYaP/UI-test-automation.git
```
- В папке с проектом создаем и активируем виртуальное окружение:
```
python -m venv venv
source venv/scripts/activate
```
- Устанавливаем зависимости:
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Устанавливаем allure на Windows(если у вас данная ОС) через scoop.
```
scoop install allure 
```
- Запускаем тесты (Chrome):
```
pytest -s -v --alluredir result_allure --tb=long
```
- Формируем отчет allure.
```
allure serve result_allure
```
