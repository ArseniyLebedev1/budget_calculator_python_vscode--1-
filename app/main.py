from decimal import Decimal, ROUND_HALF_UP

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(
    title="Budget Calculator",
    description="Простой REST API для расчета бюджета.",
    version="1.0.0",
)


class BudgetRequest(BaseModel):
    daily_cost: Decimal = Field(alias="DailyCost")
    days: int = Field(alias="Days")
    include_insurance: bool = Field(alias="IncludeInsurance")

    model_config = {
        "populate_by_name": True
    }


class BudgetResponse(BaseModel):
    TotalAmount: Decimal


@app.post("/api/budget/calculate", response_model=BudgetResponse)
def calculate_budget(request: BudgetRequest):
    if request.days <= 0:
        raise HTTPException(
            status_code=400,
            detail="Количество дней должно быть больше нуля."
        )

    total = request.daily_cost * request.days

    # Страховка = +5%
    if request.include_insurance:
        total *= Decimal("1.05")

    # Округление до копеек
    total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    return {"TotalAmount": total}
