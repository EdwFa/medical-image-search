import requests
from typing import Optional, Dict

import streamlit as st

def upload_image_to_imgbb(file_bytes: bytes) -> Optional[str]:
    """
    Загружает изображение на хостинг ImgBB (доступен в Китае).
    """
    url = "https://api.imgbb.com/1/upload"
    # Безопасное получение ключа из секретов
    api_key = st.secrets["IMGBB_API_KEY"]
    files = {
        'image': ('image.png', file_bytes, 'image/png')
    }
    data = {
        'key': api_key
    }
    try:
        response = requests.post(url, data=data, files=files)
        response.raise_for_status()
        res_data = response.json()
        if res_data.get('success'):
            return res_data['data']['url']
        return None
    except Exception as e:
        print(f"Ошибка загрузки на ImgBB: {e}")
        return f"ERROR: {e}"

def generate_search_links(image_url: str) -> Dict[str, str]:
    """
    Генерирует ссылки на поисковые системы по переданному URL изображения.
    """
    return {
        "Google Lens": f"https://lens.google.com/uploadbyurl?url={image_url}",
        "Yandex Images": f"https://yandex.ru/images/search?rpt=imageview&url={image_url}",
        "Bing": f"https://www.bing.com/images/search?view=detailv2&iss=sbi&FORM=RECIPE&q=imgurl:{image_url}",
        "TinEye": f"https://tineye.com/search?url={image_url}",
        "Baidu (百度)": f"https://graph.baidu.com/details?isfrom=1&source=&image={image_url}",
        "Sogou (搜狗)": f"https://pic.sogou.com/ris?query={image_url}",
        "PubMed (Yandex)": f"https://yandex.ru/images/search?rpt=imageview&url={image_url}&text=site:ncbi.nlm.nih.gov",
        "Open-i (NIH)": "https://openi.nlm.nih.gov/"
    }
