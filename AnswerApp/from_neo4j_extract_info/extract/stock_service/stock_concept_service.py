
from AnswerApp.from_neo4j_extract_info.neo4j import exception
from Neo4j import base_dao


def get_one_company_concept_cypher(stock_code):
    """
    一对多关系
    :param stock_code:
    :return:
    """
    concept = base_dao.get_one_company_to_relation_node(stock_code, '涉及')
    if len(concept) != 0:
        return concept
    else:
        exception.db_result_not_found("can not find stock concept", "stock_concept_dao", stock_code)
        return "notfound"


def get_concept_contains_company_cypher(concept):
    """

    :param concept:
    :return:
    """
    companies = base_dao.get_node_contain_company('概念', '概念名称', concept, '涉及')
    if len(companies) != 0:
        return companies
    else:
        exception.db_result_not_found("can not find concept contain companies", "stock_concept_dao",concept)
        return "notfound"


def get_one_company_concept(stock_code):
    concepts = get_one_company_concept_cypher(stock_code)
    return concepts


def get_concept_contains_company(in_concept):
    companies = get_concept_contains_company_cypher(in_concept)
    return companies
