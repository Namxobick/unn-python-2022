from xml.etree import ElementTree as Et  # noqa: S405

from loguru import logger


def _remove_enter(string: str) -> str:
    return string.replace('\n', '')


def _append_elem(root, name_new_root: str, text: str = None):
    name = Et.Element(name_new_root)
    if text is not None:
        name.text = text
    root.append(name)


def _append_type_info(root, name_new_root: str, user_all_info: dict):
    names = Et.Element(name_new_root)

    for user_info in user_all_info.get(name_new_root):
        name = Et.Element(name_new_root[:-1])
        names.append(name)
        _append_elem(name, 'id', str(user_info.get('id')))
        _append_elem(name, 'title', _remove_enter(str(user_info.get('title'))))

        match name_new_root:
            case 'posts':
                body = _remove_enter(str(user_info.get('body')))
                _append_elem(name, 'body', body)
            case 'todos':
                completed = _remove_enter(str(user_info.get('completed')))
                _append_elem(name, 'completed', completed)
    root.append(names)


def write_xml(user_id: str, user_email: str, user_info: dict, types_info: list, path: str):  # noqa: E501
    """
    Creates ET.Element tree and writes the user info to xml file.

    :param user_id
    :param  user_email
    :param user_info : user information from the website (PATH_JSON)
    :param types_info : 'posts', 'albums', 'todos'
    :param path : the path to the recording file
    """
    root = Et.Element('user')
    _append_elem(root, 'id', user_id)
    _append_elem(root, 'email', user_email)
    for type_info in types_info:
        _append_type_info(root, type_info, user_info)

    etree = Et.ElementTree(root)
    Et.indent(etree)
    with open(path, 'wb') as xml_file:
        etree.write(xml_file, encoding='utf-8', xml_declaration=True)

    logger.info('Saved {0}/{1}.xml for user with email `{2}`'.format(
        path,
        user_id,
        user_email,
    ))
