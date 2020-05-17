

from AnswerApp.from_neo4j_extract_info.neo4j import exception
from Neo4j import base_dao


def get_one_company_industry_cypher(stock_code):
    """
    一般来说一个公司对应三个行业
    :param stock_code:
    :return:
    """
    industry = base_dao.get_one_company_to_relation_node(stock_code, '属于')
    if len(industry) != 0:
        return industry
    else:
        exception.db_result_not_found("can not find stock industry", "stock_industry_dao", stock_code)
        return "notfound"


def get_industry_contain_cypher(industry):
    companies = base_dao.get_node_contain_company('行业', '行业名称', industry, '属于')
    if len(companies) != 0:
        return companies
    else:
        exception.db_result_not_found("can not find industry contain", "stock_industry_dao", industry)
        return "notfound"


def get_one_company_industry(stock_code):
    industry = get_one_company_industry_cypher(stock_code)
    return industry


def get_one_industry_contain(industry):
    companies = get_industry_contain_cypher(industry)
    return companies
