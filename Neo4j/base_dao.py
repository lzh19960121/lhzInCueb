from neomodel import config
from neomodel import db
from py2neo import Graph

graph = Graph('http://114.116.217.16:7474/', username='neo4j', password='Cueb@2019')
config.DATABASE_URL = 'bolt://neo4j:Cueb@2019@114.116.217.16:7687'  # 定义连接并实施
config.ENCRYPTED_CONNECTION = False
config.MAX_POOL_SIZE = 200  # default


def update_node(need_update_node, data):
    need_update_node.update(data)
    graph.push(need_update_node)


def match_two_where(label: str, proper1: str, p_value1: str, proper2: str, p_value2: str):
    """
    有两个并列where 的 cypher 语句
    :param label:
    :param proper1:
    :param p_value1:
    :param proper2:
    :param p_value2:
    :return:
    """
    sql = "match (n:" + label + ") where n.`" + proper1 + "`='" + \
          p_value1 + "' and n.`" + proper2 + "`='" + p_value2 + "' return n"
    results, columns = db.cypher_query(sql)
    result_list = []
    for one in results:
        properties = one[0].__dict__['_properties']
        result_list.append(properties)
    return result_list


def match_where(label: str, proper: str, p_value: str):
    sql = "Match (n:" + label + ") where n.`" + proper + "`='" + p_value + "' return n"
    results, columns = db.cypher_query(sql)
    result_list = []
    for one in results:
        properties = one[0].__dict__['_properties']
        result_list.append(properties)
    return result_list


def pars_path_node(path_node: list):
    """
    解析返回的path，提取其中的属性
    :param path_node:
    :return:
    """
    result_list = []
    for one in path_node:
        path = one[0]
        properties = path.end_node.__dict__['_properties']
        result_list.append(properties)
    return result_list


def get_one_company_to_relation_node(stock_num, relation):
    """
    得到某个公司的某个关系指向信息
    :param stock_num: 股票代码
    :param relation: 关系名称
    :return:
    """
    results, columns = db.cypher_query('Match p = (:shangshigongsi {公司代码:"' + stock_num +
                                       '"}) - [m:`' + relation + '`]-() return p')
    result = pars_path_node(results)
    return result


def get_node_contain_company(label, property_name, property_content, relation):
    """
    得到某个节点某种关系关联到的所有公司
    :param label: label
    :param property_name:
    :param property_content:
    :param relation:
    :return:
    """
    results, columns = db.cypher_query(
        'Match p=(:' + label + '{' + property_name + ':"' + property_content + '"})-[m:`' + relation + '`]-() return p')
    result = pars_path_node(results)
    return result


def get_node_relation_contain(label, property_name, property_content, relation):
    """
    得到某个节点某种关系关联到的其他节点
    :param label: label
    :param property_name:
    :param property_content:
    :param relation:
    :return:
    """
    results, columns = db.cypher_query(
        'Match p=(:' + label + '{' + property_name + ':"' + property_content + '"})-[m:`' + relation + '`]-() return p')
    result = pars_path_node(results)
    return result


def match_node_info_by_id(node_id):
    sql = "MATCH (n) WHERE id(n)=" + str(node_id) + " return n"
    results, columns = db.cypher_query(sql)
    result_list = []
    for one in results:
        properties = one[0].__dict__['_properties']
        result_list.append(properties)
    return result_list[0]


def delete_node_by_id(node_id):
    sql = "MATCH (n) WHERE id(n)=" + str(node_id) + " delete n"
    results, columns = db.cypher_query(sql)
    return results, columns
