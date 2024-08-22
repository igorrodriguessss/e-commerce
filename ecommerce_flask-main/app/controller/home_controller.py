from flask import Blueprint, render_template
from app.model.category import Category
from app.model.product import Product

home_bp = Blueprint('home', __name__)

categories = [Category(1, "Ferragens para Construção"), Category(2, "Ferragens para Fixação e Fontagem"), Category(3, "Ferragens para Janelas"), Category(4,"Ferragens para Segurança")]
products = [
    Product(1, "Estribo Aço CA 60 4,20mm 7x27cm", 1200.00, 1, "Câmera digital de alta resolução.", [
        "https://cdn.leroymerlin.com.br/products/estribo_aco_ca__60_4,20mm_7x27cm_arcelormittal_90350890_0001_600x600.jpg",
        "https://cdn.leroymerlin.com.br/products/estribo_aco_ca__60_4,20mm_7x27cm_arcelormittal_90350890_0001_600x600.jpg",
        "https://cdn.leroymerlin.com.br/products/estribo_aco_ca__60_4,20mm_7x27cm_arcelormittal_90350890_0001_600x600.jpg",
        "https://cdn.leroymerlin.com.br/products/estribo_aco_ca__60_4,20mm_7x27cm_arcelormittal_90350890_0001_600x600.jpg",
        "https://cdn.leroymerlin.com.br/products/estribo_aco_ca__60_4,20mm_7x27cm_arcelormittal_90350890_0001_600x600.jpg"
    ]),
    Product(2, "Livro de Python", 45.00, 2, "Aprenda Python facilmente.", [
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
        "https://blog.geekhunter.com.br/wp-content/uploads/2020/08/livros-de-python.jpg",
    ]),
    Product(3, "Action Figure Spider-Man", 29.95, 3, "Boneco articulado do Spider-Man, perfeito para colecionadores.", [
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
        "https://lojaarenagames.com.br/wp-content/uploads/2022/05/Action_Figure_Spider_Man_The_Amazing_Spider_Man_O_Espetacular_Homem_Aranha_Premium_Sega_Goukai_Japan_963801-1.jpg",
    ]),
    Product(4, "Carro Hot Wheels", 9.99, 3, "Carro Hot Wheels edição limitada, modelo esportivo.", [
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
    ]),
    Product(5, "Mouse Gamer RGB", 35.00, 3, "Mouse gamer com iluminação RGB e alta precisão.", [
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
        "https://imgs.pontofrio.com.br/1512850183/1xg.jpg",
    ]),
    Product(6, "Cadeira de Escritório Ergonômica", 189.99, 3, "Cadeira de escritório ergonômica com suporte lombar ajustável.", [
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81oF94ROa+L._AC_UF894,1000_QL80_.jpg",
    ])
]

@home_bp.route('/')
def home():
    return render_template('index.html', categories=categories, products=Product.all_products)
