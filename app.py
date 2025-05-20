from flask import Flask, request, jsonify

app = Flask(__name__)
data_store = {"book": "Modern C++", "phone": "iPhone 14"}

@app.route('/lab15_16/operation/', methods=['POST'])
def calculate():
  data = request.get_json()

  a = data.get('a')
  b = data.get('b')
  operator = data.get('operator')

  if a is None or operator not in ['+', '-', '*', '/']:
    return jsonify({'error': 'Invalid input'}), 400
  
  try:
    if operator == '+':
      result = a + b
    elif operator == '-':
      result = a - b
    elif operator == '*':
      result = a * b
    elif operator == '/':
      result = a / b
    else:
      return jsonify({'error': 'unsupported operator'}), 400
    return jsonify({'result: ': str(result)}), 200
  
  except Exception as e:
    return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
  app.run(debug = True)