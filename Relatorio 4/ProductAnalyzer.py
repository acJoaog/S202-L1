from database import Database
from writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, database : Database):
        self.database = database

    def total_vendas_por_dia(self) :
        result = self.database.collection.aggregate([
        {'$unwind': '$produtos'},
        {'$group': {'_id': '$data_compra','quantidade_total': {'$sum': '$produtos.quantidade'}}},
        ])
 
        writeAJson(result, "Total de vendas por dia")

    def produto_mais_vendido_nas_compras(self) :
        result = self.database.collection.aggregate([
        {'$unwind': '$produtos'},
        {'$group': {'_id': {'cliente_id': '$cliente_id','data_compra': '$data_compra'},'produto_mais_vendido': {'$max': {'quantidade': '$produtos.quantidade','descricao': '$produtos.descricao'}}}}
        ])
 
        writeAJson(result, "Produto mais vendido nas compras")
    
    def cliente_que_mais_gastou(self) :
        result = self.database.collection.aggregate([
        {'$unwind': '$produtos'},
        {'$group': {'_id': {'cliente_id': '$cliente_id','data_compra': '$data_compra'},'total_gasto': {'$sum': {'$multiply': ['$produtos.quantidade', '$produtos.preco']}}}},
        {'$sort': {'total_gasto': -1}},
        {'$limit': 1}
        ])
 
        writeAJson(result, "Cliente que mais gastou")
    
    def produtos_vendidos_acimda_de_uma_unudade(self) :
        result = self.database.collection.aggregate([
        {'$unwind': '$produtos'},
        {'$match': {'produtos.quantidade': {'$gt': 1}}},
        {'$group': {'_id': '$produtos.descricao'}}
        ])
 
        writeAJson(result, "Produtos vendidos acimda de uma unudade")
        
    