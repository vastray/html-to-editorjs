# HTML to Editor.js JSON

Convert HTML to [Editor.js](https://editorjs.io/) JSON format

## Installation
```
pip install html_to_editorjs
```

## Usage

```python

from html_to_editorjs import parse


json = parse("""
    <h1>My Page</h1>

    <h2>Introduction</h2>

    <p>Some <em>content</em> that is pretty <strong>interesting</strong></p>
    <p>Don't forget to <a href="https://example.com">follow me!</a></p>

    <h2>Illustration</h2>
    <img src="https://example.com/image.png" alt="image"/>
""")
```

## Supported blocks

- Paragraph (p)
- Header (h1, h2, h3, h4, h5)
- List (ul, ol)
- Image (img, figure, figcaption)