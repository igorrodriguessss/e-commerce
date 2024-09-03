from flask import Blueprint, render_template
from app.model.category import Category
from app.model.product import Product

home_bp = Blueprint('home', __name__)

categories = [Category(1, "Ferragens para Construção"), Category(2, "Ferragens para Fixação e Fontagem"), Category(3, "Fechaduras"), Category(4,"Colas")]
products = [
    Product(1, "Estribo Aço CA 60 4,20mm 7x27cm", 1200.00, 1, "estribo do bom.", [
        "https://cdn.leroymerlin.com.br/products/estribo_aco_ca__60_4,20mm_7x27cm_arcelormittal_90350890_0001_600x600.jpg",
        
    ]),
    Product(2, "Parafuso Chip Para Madeira Mdf 5x70 Phillips 100un - Caixa", 15.63, 2, "parafuso supimpa hein!!!", [
        "https://http2.mlstatic.com/D_NQ_NP_743181-MLB72723772233_112023-O.webp",
        
    ]),
    Product(3, "fechadura", 929.95, 3, "fechadura resistente forjada pelas mãos de habilidosos duendes da Irlanda do Norte", [
        "https://ferragemfloresta.vtexassets.com/arquivos/ids/169013-500-auto?v=638403402244900000&width=500&height=auto&aspect=true",
        
    ]),
    Product(4, "Carro Hot Wheels", 9.99, 3, "Carro Hot Wheels edição limitada, infiltrado nas fechaduras para trazer alegria ao comprador", [
        "https://lojamega.com.br/wp-content/uploads/2023/11/47048-1-1.jpg",
       
    ]),
    Product(5, "Cola branca 1 kg", 35.00, 4, "cola marca genérica tanana tanana tanana ", [
        "https://img.kalunga.com.br/fotosdeprodutos/211778.webp",
        
    ]),
    Product(6, "Cola instantanea", 189.99, 4, "o programador anterior precisou sair mais cedo pois colou os dedos com essa cola", [
        "https://img.kalunga.com.br/fotosdeprodutos/210136.webp",
       
    ])
]

@home_bp.route('/')
def home():
    return render_template('index.html', categories=categories, products=Product.all_products)
