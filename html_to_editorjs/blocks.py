from .helpers import get_html_text, get_img_file


def paragraph(selection):
    return {
        'type': 'paragraph',
        'data': {
            'text': get_html_text(selection),
        }
    }


def header(selection):
    tag_name = selection.name
    level = tag_name.replace('h', '', 1)

    return {
        'type': 'header',
        'data': {
            'text': get_html_text(selection),
            'level': level
        }
    }


def list_block(selection):
    tag_name = selection.name
    items = []
    style = 'unordered'

    if tag_name == 'ol':
        style = 'ordered'

    li_tags = selection.find_all('li')
    for li in li_tags:
        html = get_html_text(li)
        if html != '':
            items.append(html)

    if len(items) > 0:
        return {
            'type': 'list',
            'data': {
                'style': style,
                'items': items
            }
        }

    return None


def image(selection):
    tag_name = selection.name
    file = {}
    caption = ''

    if tag_name == 'img':
        file = get_img_file(selection)

    if tag_name == 'figure':
        file = get_img_file(selection.find('img'))
        selection_caption = selection.find('figcaption')
        if selection_caption:
            caption = get_html_text(selection_caption)

    if file.get('url') is not None:
        return {
            'type': 'image',
            'data': {
                'file': file,
                'caption': caption,
                'withBorder': False,
                'withBackground': False,
                'stretched': False,
            },
        }