from Util import basic_util, date_util


def db_result_not_found(action, class_name, inputs):
    """
    :param action:
    :param class_name:
    :param inputs:
    :return:
    """
    result_not_found = 'db result not found, type :' + action + ", error_class_name: " + class_name + " ,input: " + inputs
    basic_util.write_text_apend(r"db_result_not_found", date_util.get_current_y_m_d_h_m_s() + " " + result_not_found)
    print(result_not_found)


def load_all_exception():
    all_error = basic_util.read_one_file(r'db_result_not_found', 'utf-8')
    print(all_error)
    return all_error
