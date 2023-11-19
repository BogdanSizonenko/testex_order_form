import motor.motor_asyncio
from pymongo import InsertOne
import os
from dotenv import load_dotenv


load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.test_form

forms_collection = database.get_collection('forms_collection')


# Список шаблонов форм, по запросу в бд    
async def get_list_forms():
    list_form = []
    cursor = forms_collection.find({},{'_id': 0})
    async for form in cursor:
        list_form.append(form)
    if len(list_form) == 0:
        requests = [InsertOne({"name": "phone_reg_form", "template_forms": {"phone_number": "phone"}}), 
                    InsertOne({"name": "auth_form", "template_forms": {"username": "text", "email": "email"}}),
                    InsertOne({"name": "full_auth_form", "template_forms": {"username": "text", "email": "email", 
                                                                    "order_date": "date", "phone_number": "phone"}}),
                    InsertOne({"name": "author_form", "template_forms": {"username": "text", "order_date": "date"}}),
                    InsertOne({"name": "business_card_form", "template_forms": {"username": "text", "phone_number": "phone", 
                                                                        "email": "email"}})]

        await forms_collection.bulk_write(requests)
        await get_list_forms()
        return list_form
    return list_form