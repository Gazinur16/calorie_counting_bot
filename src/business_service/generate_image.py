from typing import List, Dict, Any
import matplotlib.pyplot as plt
import pandas as pd
import io

#TODO
def generate_nutrition_image(ingredients: List[Dict[str, int]], total_row: Dict[str, Any]) -> io.BytesIO:
    """
    Генерация изображения таблицы
    """
    # Создание DataFrame
    df = pd.DataFrame(ingredients)
    df = df.rename(columns={
        "name": "Название",
        "weight": "Вес, г",
        "calories": "Ккал",
        "proteins": "Б, г",
        "fats": "Ж, г",
        "carbs": "У, г"
    })

    # Добавляем строку "ИТОГО"
    total_df = pd.DataFrame([total_row])
    df = pd.concat([df, total_df], ignore_index=True)

    # Создание изображения
    if len(ingredients) == 1:
        fig, ax = plt.subplots(figsize=(4, len(df) * 0.8))
    elif 2 <= len(ingredients) < 4:
        fig, ax = plt.subplots(figsize=(4, len(df) * 0.6))
    else:
        fig, ax = plt.subplots(figsize=(4, len(df) * 0.4))

    ax.axis("tight")
    ax.axis("off")

    # Создание таблицы
    table = ax.table(
        cellText=df.values,
        colLabels=df.columns,
        cellLoc="center",
        loc="center",
        colWidths=[0.4, 0.15, 0.15, 0.12, 0.12, 0.12]
    )

    # Настройки стиля
    table.auto_set_font_size(False)
    table.set_fontsize(8)

    # Выделение заголовка желтым
    for i in range(len(df.columns)):
        table[0, i].set_facecolor("#fff5cc")
        table[0, i].set_text_props(weight="bold")

    # Выделение последней строки ("ИТОГО") желтым
    last_row_index = len(df)
    for i in range(len(df.columns)):
        table[last_row_index, i].set_facecolor("#fff5cc")
        table[last_row_index, i].set_text_props(weight="bold")

    # Сохранение изображения в буфер
    buf = io.BytesIO()
    plt.savefig(buf, format="jpg", dpi=300, bbox_inches="tight")
    plt.close(fig)
    buf.seek(0)

    return buf