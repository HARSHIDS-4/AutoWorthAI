from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Dict,Optional,Annotated,Literal
from datetime import datetime
from config.field_values import manufacturer_values,model_values,type_values,paint_color_values,state_values


class Car(BaseModel):

    year: Annotated[int,Field(...,description="Year of the car purchased",example=2015, gt=1980,lt=datetime.now().year)]

    manufacturer: Annotated[str,Field(...,description="Manufacturer of the car",example="Toyota")]

    model: Annotated[str,Field(...,description="Model of the car",example="silverado 1500")]

    condition: Annotated[Literal['salvage','fair','other','good','excellent','like new','new'],Field(...,description="Condition of the car",example="good")]

    fuel: Annotated[Literal['gas', 'other', 'diesel', 'hybrid', 'electric'],Field(...,description="Fuel type of the car")]

    odometer: Annotated[int,Field(...,description="Odometer reading of the car",example=50000,gt=0,lt=300000)]

    title_status: Annotated[Literal['clean', 'rebuilt', 'lien', 'salvage', 'missing', 'parts only'],Field(...,description="Title status of the car")]

    transmission: Annotated[Literal['other', 'automatic', 'manual'],Field(...,description="Transmission type of the car")]

    drive: Annotated[Literal['rwd' ,'4wd' ,'fwd','other'],Field(...,description="Drive type of the car",example="4wd")]

    type: Annotated[str,Field(...,description="Type of the car",example="pickup")]

    paint_color: Annotated[str,Field(...,description="Paint color of the car",example="white")]

    state: Annotated[str,Field(...,description="State where the car is located",example="ca")]
    
    no_of_cylinders: Annotated[int,Field(...,description="Number of cylinders in the car",example=6) ]

    @computed_field
    @property
    def car_age(self) -> int:
        curr_year=datetime.now().year
        age= curr_year - self.year
        return age
    
    @field_validator("year")
    @classmethod
    def validate_year(cls,v: int) -> int:
        if v < 1980 or v > datetime.now().year:
            raise ValueError("Year must be between 1980 and current year")
        
        return v
    
    @field_validator("odometer")
    @classmethod
    def validate_odometer(cls,v: int) -> int:
        if v < 0 or v > 300000:
            raise ValueError("Odometer reading must be between 0 and 300000")
        
        return v

    @field_validator("manufacturer")
    @classmethod
    def validate_manufacturer(cls, v: str) -> str:
        v=v.strip().lower()
        if v not in manufacturer_values:
            raise ValueError(f"enter valid value {manufacturer_values}")
        return v
        

    @field_validator("model")
    @classmethod
    def validate_model(cls, v: str) -> str:
        v=v.strip().lower()
        if v not in model_values:
            return "other"
        return v
    
    @field_validator("type")
    @classmethod
    def validate_type(cls, v: str) -> str:
        v=v.strip().lower()
        if v not in type_values:
            return "other"
        return v
    
    @field_validator("paint_color")
    @classmethod
    def validate_paint_color(cls, v: str) -> str:
        v=v.strip().lower()
        if v not in paint_color_values:
            return "other"
        return v
    
    @field_validator("state")
    @classmethod
    def validate_state(cls, v: str) -> str:
        v=v.strip().lower()
        if v not in state_values:
            raise ValueError(f"enter valid value {state_values}")
        return v
    
    @field_validator("no_of_cylinders")
    @classmethod
    def validate_no_of_cylinders(cls, v: int) -> int:
        if v < 0 or v > 16:
            raise ValueError("Number of cylinders must be a positive integer between 0 and 16")
        return v