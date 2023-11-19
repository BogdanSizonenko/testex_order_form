import re 


# Типизация полей входящих данных
def get_type(data):
    types = {
        'date': r'^([0-2][0-9]|30|31)\.([0][0-9]|10|11|12)\.\d{4}$',
        'yyyy.mm.dd': r'^\d{4}\-([0][0-9]|10|11|12)\-([0-2][0-9]|30|31)$',
        'phone': r'(\+7)\ [0-9]{3}\ [0-9]{3}\ [0-9]{2}\ [0-9]{2}',
        'email': r'^\S+@\w+.\w{2,4}$'
    }
    for k, v in types.items():
        if re.fullmatch(v, data):
            if k == 'yyyy.mm.dd':
                return 'date'
            return k
    return 'text'

# Словарь входящих значений и их типов 
def get_dict_data_types(data):
    ans = {}
    for k, d in data.items():
        ans[k] = get_type(d)
    return ans

# Список только типов входящих значений
def get_list_types(dict_data):
    list_types = [data for data in dict_data.values()]
    return list_types

# Список подходящих шаблонов форм из бд
def get_list_required_forms(list_forms, data_list_types):
    list_required_forms = []
    for form in list_forms:
        form_list_types = [val for val in form['template_forms'].values()]
        if all(types in data_list_types for types in form_list_types):
            list_required_forms.append(form['name'])
    return list_required_forms