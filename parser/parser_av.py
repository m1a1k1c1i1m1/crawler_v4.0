from loguru import logger


class Parser:

    def format_json(self, data):
        new_value = dict()
        try:
            usd = data['price']['usd']['amount']
            byn = data['price']['byn']['amount']
            refreshedAt = data['refreshedAt']
            new_car = data['properties']
            for items in new_car:
                key_name = items['name']
                value = items['value']
                if value != True:
                    new_value.update({f'{key_name}': value})
            new_value.update({
                'locationName': data['locationName'],
                'sellerName': data['sellerName'],
                'refreshedAt': refreshedAt,
                'publishedAt': data['publishedAt'],
                'publicUrl': data['publicUrl'],
                'price_byn': byn,
                'price_usd': usd,
                'name_todo': str(data['id'])
            })
            return new_value
        except Exception as error:
            logger.error(f'возникла ошибка: {error} в функции json_format')
            new_value.update({'price_byn': 0, 'price_usd': 0})
            return new_value