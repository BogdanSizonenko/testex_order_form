from fastapi import APIRouter, Body
from .utils import get_dict_data_types, get_list_types, get_list_required_forms
from .database import get_list_forms


router = APIRouter()


@router.post("/forms")
async def get_form(data: dict = Body(examples=[{'field_name': 'value',}])):
    "Передавать данные в формате словаря = {'имя поля': 'значени поля'}"
    
    # Формируем словарь входящих значений и их типов (соотвественно передаем входные данные)
    dict_data = get_dict_data_types(data)
    
    # Запрашиваем список имеющихся форм в базе
    list_forms = await get_list_forms()

    # Для поиска подхрдящей формы, формируем список типов входящих значений (передаем словарь входящих значений и их типов)
    data_list_types = get_list_types(dict_data)
    
    # Формируем список подходящих шаблонов форм, из списка шаблонов форм из базы и списка типов входящих данных
    required_forms = get_list_required_forms(list_forms, data_list_types)
    
    # Если список пуст, тоесть подходящих шаблонов форм в базе нет, возвращаем типизацию входящих данных
    if not required_forms:
        return dict_data 
    return required_forms