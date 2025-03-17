from typing import Any

def get_total_line(ingredients_on_photo: list[dict[str, int]]) -> dict[str, Any]:

    total_line = {
        "Название": "ИТОГО",
        "Вес, г": sum(item["weight"] for item in ingredients_on_photo),
        "Ккал": sum(item["calories"] for item in ingredients_on_photo),
        "Б, г": sum(item["proteins"] for item in ingredients_on_photo),
        "Ж, г": sum(item["fats"] for item in ingredients_on_photo),
        "У, г": sum(item["carbs"] for item in ingredients_on_photo),
    }

    return total_line