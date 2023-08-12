from html_to_editorjs import parse

html = '''
<h1>My Page</h1>

<h2>Introduction</h2>

<p>Some <em>content</em> that is pretty <strong>interesting</strong></p>
<p>Don't forget to <a href="https://example.com">follow me!</a></p>

<h2>Illustration</h2>
<img src="https://example.com/image.png" alt="image"/>
'''

print(parse(html))