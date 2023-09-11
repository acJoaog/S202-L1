from database import Database
from writeAJson import writeAJson
from ProductAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
#db.resetDatabase()

product_analyzer = ProductAnalyzer(db)

product_analyzer.total_vendas_por_dia()
product_analyzer.produto_mais_vendido_nas_compras()
product_analyzer.cliente_que_mais_gastou()
product_analyzer.produtos_vendidos_acimda_de_uma_unudade()