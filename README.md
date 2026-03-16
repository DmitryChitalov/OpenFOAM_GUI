# Графическая оболочка для построения сеток и генерации численных в моделей в OpenFOAM

![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![PyQt](https://img.shields.io/badge/PyQt-5-green.svg)
![License](https://img.shields.io/badge/license-%20%20GNU%20GPLv3%20-green?style=plastic)

Приложение с удобным и интуитивно понятным графическим интерфейсом

## 🚀 Возможности
- Создание новых расчетных случаев и открытие существующих
- Генерация расчетных сеток и численных моделей задач механики сплошных сред
- Интерфейс на PyQt5.
- Сохранение данных в JSON и EXCEL.
- Генерация придиктивных моделей для расчетных параметров.

## 🛠 Установка и запуск

1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/DmitryChitalov/OpenFOAM_GUI.git
    cd OpenFOAM_GUI
    ```

2.  **Установите зависимости:**
    Рекомендуется использовать виртуальное окружение:
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    
    pip install -r requirements.txt
    ```

3.  **Запустите приложение:**
    ```bash
    python run.py
    ```
