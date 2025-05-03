# Определить, какие марки машин были доставлены во все указанные страны, какие — в некоторые, а какие — ни в одну

def analyz(brands, exports):
        all_countries_set = set(exports.keys())        # Получает все страны как множество
        brand_to_countries = {brand: set() for brand in brands}     # Создаёт словарь с пустыми множествами для каждого бренда


        for country, exported_brands in exports.items():    # Заполняет словарь странами, куда экспортируется каждый бренд
                for brand in exported_brands:
                        if brand in brand_to_countries:
                                brand_to_countries[brand].add(country)

        # Создание списков для категорий брендов
        in_all = []
        in_some = []
        in_none = []

        # Определение категории для каждого бренда
        for brand in brands:
                countries = brand_to_countries[brand]
                if countries == all_countries_set:
                        in_all.append(brand)
                elif countries:
                        in_some.append(brand)
                else:
                        in_none.append(brand)

        #результаты
        print("Во все страны:", in_all)
        print("В некоторые страны:", in_some)
        print("Ни в одну страну:", in_none)


brands = ['BMW', 'Audi', 'Lada', 'Toyota', 'Daewoo']
exports = {
        'Germany': ['BMW', 'Audi'],
        'Russia': ['Lada', 'BMW'],
        'Japan': ['Toyota', 'BMW']
}

analyz(brands, exports)