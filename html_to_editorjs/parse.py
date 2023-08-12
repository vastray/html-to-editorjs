from bs4 import BeautifulSoup
from datetime import datetime

from . import blocks


block_handlers = {
    'p': blocks.paragraph,
    'h1': blocks.header,
    'h2': blocks.header,
    'h3': blocks.header,
    'h4': blocks.header,
    'h5': blocks.header,
    'ol': blocks.list_block,
    'ul': blocks.list_block,
    'img': blocks.image,
    'figure': blocks.image,
}


def parse(payload):
    nodes = BeautifulSoup(payload, 'html.parser')

    response = {
        "time": datetime.now().timestamp(),
        "blocks": []
    }

    for i, selection in enumerate(nodes):

        tag_name = selection.name or ''

        if tag_name in block_handlers:
            handler = block_handlers[tag_name]

            block = handler(selection)
            if block is not None:
                response["blocks"].append(block)

    return response
