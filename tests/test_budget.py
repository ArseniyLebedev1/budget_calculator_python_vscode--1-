from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_happy_path_without_insurance():
    response = client.post(
        "/api/budget/calculate",
        json={
            "DailyCost": 100,
            "Days": 5,
            "IncludeInsurance": False,
        },
    )

    assert response.status_code == 200
    assert float(response.json()["TotalAmount"]) == 500.00


def test_with_insurance_adds_five_percent():
    response = client.post(
        "/api/budget/calculate",
        json={
            "DailyCost": 100,
            "Days": 5,
            "IncludeInsurance": True,
        },
    )

    assert response.status_code == 200
    assert float(response.json()["TotalAmount"]) == 525.00


def test_negative_days_returns_400():
    response = client.post(
        "/api/budget/calculate",
        json={
            "DailyCost": 100,
            "Days": -1,
            "IncludeInsurance": False,
        },
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Количество дней должно быть больше нуля."


def test_zero_daily_cost_returns_zero():
    response = client.post(
        "/api/budget/calculate",
        json={
            "DailyCost": 0,
            "Days": 5,
            "IncludeInsurance": False,
        },
    )

    assert response.status_code == 200
    assert float(response.json()["TotalAmount"]) == 0.00


def test_decimal_calculation_is_correct_to_kopecks():
    response = client.post(
        "/api/budget/calculate",
        json={
            "DailyCost": 100.50,
            "Days": 3,
            "IncludeInsurance": False,
        },
    )

    assert response.status_code == 200
    assert float(response.json()["TotalAmount"]) == 301.50


def test_decimal_calculation_with_insurance_is_rounded():
    response = client.post(
        "/api/budget/calculate",
        json={
            "DailyCost": 100.50,
            "Days": 3,
            "IncludeInsurance": True,
        },
    )

    assert response.status_code == 200
    assert float(response.json()["TotalAmount"]) == 316.58
