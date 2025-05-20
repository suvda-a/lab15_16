from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/lab15_16/operation/', methods=['POST'])
def calculate():
  if not request.is_json:
    return jsonify({'error': 'Unsupported Media Type'}), 415

  data = request.get_json()
  a = data.get('a')
  b = data.get('b')
  operator = data.get('operator')

  if a is None or b is None or operator not in ['+', '-', '*', '/']:
    return jsonify({'error': 'Invalid input'}), 400

  try:
    if operator == '+':
      result = int(a) + int(b)
    elif operator == '-':
      result = int(a) - int(b)
    elif operator == '*':
      result = int(a) * int(b)
    elif operator == '/':
      result = int(a) / int(b)
    return jsonify({'result': str(result)}), 200

  except Exception as e:
      return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
  app.run(debug=True)