import streamlit as st
from PIL import Image
import io
from search_engine import upload_image_to_imgbb, generate_search_links

st.set_page_config(page_title="Поиск плагиата и источников", page_icon="🔍", layout="centered")

st.title("🔍 Реверсивный поиск медицинских изображений")
st.markdown("Загрузите медицинское или научное изображение, чтобы найти его копии (плагиат) или первоисточники в интернете.")

uploaded_file = st.file_uploader("Выберите изображение...", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file is not None:
    # Отображаем загруженное изображение
    image = Image.open(uploaded_file)
    st.image(image, caption="Загруженное изображение", use_container_width=True)

    if st.button("Найти источники в Интернете", type="primary"):
        with st.spinner("Подготовка изображения для поиска..."):
            # Получаем байты изображения
            file_bytes = uploaded_file.getvalue()
            
            # Загружаем на временный хостинг
            image_url = upload_image_to_imgbb(file_bytes)
            
            if image_url and not image_url.startswith("ERROR:"):
                st.success("Изображение успешно подготовлено! Выберите поисковую систему:")
                
                # Генерируем ссылки
                links = generate_search_links(image_url)
                
                # Отображаем ссылки в виде HTML кнопок
                st.markdown(f"""
                <div style="display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap;">
                    <a href="{links['Google Lens']}" target="_blank" style="flex: 1; min-width: 150px; text-decoration: none;">
                        <button style="width: 100%; padding: 10px; background-color: #4285F4; color: white; border: none; border-radius: 5px; cursor: pointer;">🔍 Google Lens</button>
                    </a>
                    <a href="{links['Yandex Images']}" target="_blank" style="flex: 1; min-width: 150px; text-decoration: none;">
                        <button style="width: 100%; padding: 10px; background-color: #FFCC00; color: black; border: none; border-radius: 5px; cursor: pointer;">🔍 Yandex</button>
                    </a>
                    <a href="{links['Bing']}" target="_blank" style="flex: 1; min-width: 150px; text-decoration: none;">
                        <button style="width: 100%; padding: 10px; background-color: #00809D; color: white; border: none; border-radius: 5px; cursor: pointer;">🔍 Bing</button>
                    </a>
                    <a href="{links['TinEye']}" target="_blank" style="flex: 1; min-width: 150px; text-decoration: none;">
                        <button style="width: 100%; padding: 10px; background-color: #000000; color: white; border: none; border-radius: 5px; cursor: pointer;">🔍 TinEye</button>
                    </a>
                    <a href="{links['Baidu (百度)']}" target="_blank" style="flex: 1; min-width: 150px; text-decoration: none;">
                        <button style="width: 100%; padding: 10px; background-color: #2932E1; color: white; border: none; border-radius: 5px; cursor: pointer;">🇨🇳 Baidu (百度)</button>
                    </a>
                    <a href="{links['Sogou (搜狗)']}" target="_blank" style="flex: 1; min-width: 150px; text-decoration: none;">
                        <button style="width: 100%; padding: 10px; background-color: #FF5A00; color: white; border: none; border-radius: 5px; cursor: pointer;">🇨🇳 Sogou (搜狗)</button>
                    </a>
                </div>
                <h4 style="margin-top: 20px;">🔬 Научный поиск</h4>
                <div style="display: flex; gap: 10px; margin-bottom: 20px; flex-wrap: wrap;">
                    <a href="{links['PubMed (Yandex)']}" target="_blank" style="flex: 1; min-width: 150px; text-decoration: none;">
                        <button style="width: 100%; padding: 10px; background-color: #005A9C; color: white; border: none; border-radius: 5px; cursor: pointer;">📚 Yandex (только PubMed)</button>
                    </a>
                    <a href="{links['Open-i (NIH)']}" target="_blank" style="flex: 1; min-width: 150px; text-decoration: none;">
                        <button style="width: 100%; padding: 10px; background-color: #2E8540; color: white; border: none; border-radius: 5px; cursor: pointer;">🧬 Open-i (Сайт)</button>
                    </a>
                </div>
                """, unsafe_allow_html=True)
                
                st.info("💡 Нажмите на кнопки выше, чтобы открыть результаты поиска в новой вкладке. Загрузка происходит через глобальный CDN (ImgBB), доступный в том числе из Китая.")
            else:
                st.error(f"Произошла ошибка при загрузке изображения: {image_url if image_url else 'Неизвестная ошибка'}")
