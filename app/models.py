from pydantic import BaseModel, Field, EmailStr, validator


class ListForms(BaseModel):
    name: str = Field(..., examples=['name_form'])
    template_forms: dict[str, str] = Field(..., examples=[{
        'name_field': 'type_field'
        }])
    