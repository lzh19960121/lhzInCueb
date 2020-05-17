
from AnswerApp.from_neo4j_extract_info.neo4j import exception
from Neo4j import base_dao


def get_company_basic_info(stock_num):
    info = base_dao.match_where("shangshigongsi", '公司代码', stock_num)
    if len(info) != 0:
        return info[0]
    else:
        exception.db_result_not_found("can not find stock info", "stock_company_dao", str(stock_num))
        return "notfound"