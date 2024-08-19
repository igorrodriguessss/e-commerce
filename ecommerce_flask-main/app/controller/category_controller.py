from flask import Blueprint, render_template

from app.model.category import Category

category_bp = Blueprint('category', __name__)

categories = [Category(1, "Ferragens"), Category(2, "teste"), Category(3, "Casa e Cozinha"), Category(4, "Material")]

@category_bp.route('/categories')
def list_categories():
    return render_template('categories.html', categories=categories)
