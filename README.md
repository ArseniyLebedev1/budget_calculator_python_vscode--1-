# Budget Calculator — Python / FastAPI / pytest

Готовый учебный проект для задания по тестированию REST API.

## Что реализовано

- REST API `POST /api/budget/calculate`
- позитивный тест без страховки
- тест страховки +5%
- тест отрицательного количества дней
- тест нулевой стоимости дня
- тест расчета с десятичными значениями
- округление до копеек
- проверка покрытия тестами

## Запуск в VS Code

1. Открой эту папку через **File → Open Folder**.
2. Открой терминал VS Code.
3. Создай виртуальное окружение:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

4. Установи зависимости:

```bash
pip install -r requirements.txt
```

5. Запусти API:

```bash
uvicorn app.main:app --reload
```

API будет доступен по адресу:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

## Запуск тестов

```bash
pytest -v
```

## Code Coverage

```bash
pytest --cov=app --cov-report=term-missing
```

Для HTML-отчета:

```bash
pytest --cov=app --cov-report=html
```

Затем открой:

```text
htmlcov/index.html
```

## Пример запроса

```json
{
  "DailyCost": 100,
  "Days": 5,
  "IncludeInsurance": true
}
```

Ответ:

```json
{
  "TotalAmount": 525.0
}
```
