from Neo4j import base_dao


def get_manager_info_by_name_cypher(name):
    name = base_dao.match_where('管理层', '姓名', name)
    return name


def get_manager_info_by_name(question):
    return get_manager_info_by_name_cypher(question)
