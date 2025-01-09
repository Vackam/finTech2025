# /utils/templates.py

from fastapi.templating import Jinja2Templates
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VIEWS_DIR = os.path.join(BASE_DIR, "views")

# Jinja2Templates 인스턴스 생성
templates = Jinja2Templates(directory=VIEWS_DIR)
