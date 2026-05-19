from pydantic import BaseModel,Field

class PredictionResponse(BaseModel):
    predicted_price: float = Field(
        ...,
        description="Predicted car price",
        example=150000.00,
        gt=0)
