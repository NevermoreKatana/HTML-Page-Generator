from django import template

register = template.Library()


@register.simple_tag
def render_api_docs(data):
    output = ''
    for key, value in data.items():
        output += '<article>'
        output += f'<h1 class="text-3xl font-bold text-orange-500 mb-4">{value["name"]}</h1>'
        output += f'<h1 class="text-3xl font-bold text-orange-500">{value["request_type"]} {value["endpoint"]}</h1>'
        output += f'<pre class="px-4 py-3 rounded-md bg-gray-800 text-gray-300">{value["request_type"]} {value["request"]}</pre>'
        if value["request_type"] != 'GET':
            output += '<h2 class="text-2xl font-bold text-orange-500 mt-4">Request Body</h2>'
            output += f'<pre class="px-4 py-3 rounded-md bg-gray-800 text-gray-300">{value["body"]}</pre>'
        output += '<h2 class="text-2xl font-bold text-orange-500 mt-4">Response</h2>'
        output += f'<pre class="px-4 py-3 rounded-md bg-gray-800 text-gray-300">{value["answer"]}</pre>'

    return output

