from flask import Flask, request, jsonify
from barcode import Code128
from barcode.writer import ImageWriter

app = Flask (__name__)

@app.route('/create_tag', methods=["POST"])
def create_tag():
    # Protocolo HTTP
    body = request.json
    product_code = body.get('product_code')

    # Bibliotecas externas
    tag = Code128(product_code, writer=ImageWriter())
    path_from_tag = f'{tag}'
    tag.save(path_from_tag)

    # Retornando protocolo HTTP 
    return jsonify({"tag path": path_from_tag})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
