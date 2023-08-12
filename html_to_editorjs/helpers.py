def get_img_file(selection):
    file = {}
    attr = selection.attrs.get('src')
    if attr:
        file["url"] = attr

    attr = selection.attrs.get('height')
    if attr:
        try:
            file["height"] = int(attr)
        except ValueError:
            pass

    attr = selection.attrs.get('width')
    if attr:
        try:
            file["width"] = int(attr)
        except ValueError:
            pass

    return file


def transform_strong_to_bold(text):
    return text.replace('<strong>', '<b>').replace('</strong>', '</b>')


def get_html_text(selection):
    text = ''.join(str(el) for el in selection.contents)
    return transform_strong_to_bold(text)
