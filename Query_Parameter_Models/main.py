from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from typing import Annotated

class SchoolInformation(BaseModel):
    model_config = {"extra": "forbid"}
    name_of_school: str = Field(..., alias="school-name")
    number_of_students: int = Field(1000,ge=0, le=1500)
    national_test_results: float = Field(100, ge=50, le=140)
    top_students: list[str] = Field(default_factory=list)


app = FastAPI()
@app.get("/school/")
async def school_data(school: Annotated[SchoolInformation, Query()]):
    return {
        "school_information": school
    }