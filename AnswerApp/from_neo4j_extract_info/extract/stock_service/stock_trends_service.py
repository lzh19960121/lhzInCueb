
from AnswerApp.from_neo4j_extract_info.neo4j import exception
from Neo4j import base_dao


def get_one_company_trend_cypher(stock_code):
    """
    一个公司对应一个趋势
    :param stock_code:
    :return:
    """
    trend = base_dao.get_one_company_to_relation_node(stock_code, "趋势")
    if len(trend) != 0:
        return trend[0]
    else:
        exception.db_result_not_found("can not find stock trend", "stock_trends_dao",stock_code)
        return "notfound"


def get_stock_status(properties):
    """
    得到股价的当前状态
    :param properties: 股价节点的属性信息
    :return:
    """
    stock_status = properties['股价状态'][0]
    if '初始状态' or '盘整' in stock_status:
        stock_status = '震荡'
    if properties['阻力位'] == '无':
        stock_status = stock_status + '无阻力'
    if properties['支撑位'] == '无':
        stock_status = stock_status + '无支撑'
    return stock_status


def get_one_company_trend(stock_code):
    trend = get_one_company_trend_cypher(stock_code)
    return trend
