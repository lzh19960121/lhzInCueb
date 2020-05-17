

from AnswerApp.from_neo4j_extract_info.neo4j import exception
from Neo4j import base_dao


def get_one_company_daily_index_by_code(stock_code):
    index = get_one_company_daily_index_by_code_cypher(stock_code)
    return index


def get_one_company_daily_index_by_code_cypher(stock_code):
    daily_index = base_dao.get_one_company_to_relation_node(stock_code, "是每日指标")
    if len(daily_index) != 0:
        return daily_index
    else:
        exception.db_result_not_found("can not find stock daily_index", "stock_daily_dao",stock_code)
        return "notfound"