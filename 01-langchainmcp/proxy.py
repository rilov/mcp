from flask import Flask, request, Response
import requests
import json
from pprint import pformat

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'PATCH'])
def proxy(path):
    # Log the params, body, or queries with pretty formatting
    app.logger.info("Reqeust Started")
    app.logger.info("Params:\n" + pformat(request.args.to_dict()))
    body_data = request.get_json(silent=True)
    if body_data is not None:
        app.logger.info("Body:\n" + json.dumps(body_data, indent=4))
    else:
        app.logger.info("Body:\n" + request.get_data(as_text=True))

    url = f'https://api.openai.com/v1/{path}'
    headers = {key: value for key, value in request.headers if key.lower() != 'host'}
    response = requests.request(
        method=request.method,
        url=url,
        headers=headers,
        data=request.get_data(),
        params=request.args,
        cookies=request.cookies,
        allow_redirects=False,
        stream=True
    )

    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    response_headers = [(name, value) for (name, value) in response.raw.headers.items() if name.lower() not in excluded_headers]
    
    app.logger.info("Response from OpenAI API:\n" )
    app.logger.info(response.content)
    app.logger.info("End of Request")

    return Response(response.content, response.status_code, response_headers)

if __name__ == "__main__":
    app.run(debug=True, port=5000)