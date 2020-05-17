
from AnswerApp.from_neo4j_extract_info.neo4j import exception
from Neo4j import base_dao


def get_one_company_region_cypher(stock_code):
    """
    一个公司只能对应一个地区
    :param stock_code:
    :return:
    """
    region = base_dao.get_one_company_to_relation_node(stock_code, '位于')
    if len(region) != 0:
        return region[0]
    else:
        exception.db_result_not_found("can not find stock region", "stock_region_dao" ,stock_code)
        return "notfound"


def get_one_company_region(stock_code):
    return get_one_company_region_cypher(stock_code)
