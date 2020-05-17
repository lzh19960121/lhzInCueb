
from AnswerApp.from_neo4j_extract_info.neo4j import exception
from Neo4j import base_dao


def get_one_company_product_cypher(stock_code):
    products = base_dao.get_one_company_to_relation_node(stock_code, '提供')
    if len(products) != 0:
        return products
    else:
        exception.db_result_not_found("can not find stock products", "stock_products_dao", stock_code)
        return "notfound"


def get_one_product_contain_cypher(product_name):
    companies = base_dao.get_node_contain_company('产品', '产品', product_name, '提供')
    if len(companies) != 0:
        return companies
    else:
        exception.db_result_not_found("can not find  products contain", "stock_products_dao", product_name)
        return "notfound"



def get_one_company_products(stock_code):
    products = get_one_company_product_cypher(stock_code)
    return products


def get_one_product_contain(product_name):
    companies = get_one_product_contain_cypher(product_name)
    return companies
