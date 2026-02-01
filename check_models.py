import os
from dotenv import load_dotenv
import google.generativeai as genai

# Загружаем API ключ
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY не найден в .env файле")

genai.configure(api_key=GEMINI_API_KEY)

print("🔍 Проверка доступных моделей Gemini...\n")
print("="*60)

try:
    models = genai.list_models()
    
    print("✅ ДОСТУПНЫЕ МОДЕЛИ ДЛЯ ГЕНЕРАЦИИ КОНТЕНТА:\n")
    
    available_models = []
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            available_models.append(model.name)
            print(f"✓ {model.name}")
            print(f"  Описание: {model.display_name}")
            print(f"  Методы: {', '.join(model.supported_generation_methods)}")
            print()
    
    print("="*60)
    print(f"\n📊 Всего найдено моделей: {len(available_models)}\n")
    
    # Рекомендуемые модели
    print("💡 РЕКОМЕНДУЕМЫЕ МОДЕЛИ ДЛЯ БОТА:\n")
    
    recommended = [
        "gemini-2.0-flash-exp",
        "gemini-2.0-flash-001", 
        "gemini-1.5-flash",
        "gemini-1.5-flash-latest",
        "gemini-1.5-pro",
        "gemini-1.5-pro-latest",
        "gemini-pro"
    ]
    
    for rec in recommended:
        full_name = f"models/{rec}"
        if full_name in available_models:
            print(f"✅ {rec} - ДОСТУПНА")
        else:
            print(f"❌ {rec} - недоступна")
    
    print("\n" + "="*60)
    print("\n🔧 Скопируйте название доступной модели в переменную MODEL_NAME")
    print("   Например: MODEL_NAME = 'gemini-1.5-flash'\n")
    
except Exception as e:
    print(f"❌ ОШИБКА: {e}")
    print("\nВозможные причины:")
    print("1. Неверный API ключ")
    print("2. Нет доступа к API")
    print("3. Проблемы с интернет-соединением")
