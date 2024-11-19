from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Hàm hill climbing để tìm giá trị lớn nhất
def generate_neighbors(array, i):
    neighbors = []
    if i > 0:
        neighbors.append((i - 1, array[i - 1]))
    if i < len(array) - 1:
        neighbors.append((i + 1, array[i + 1]))
    return neighbors

def hill_climbing(array, position):
    i = position
    x = array[position]
    while True:
        neighbors = generate_neighbors(array, i)

        if not neighbors:
            break

        best_neighbor = max(neighbors, key=lambda x: x[1])

        if best_neighbor[1] <= x:
            break

        i, x = best_neighbor
    return x

# Route chính: hiển thị form nhập mảng
@app.route('/')
def index():
    return render_template('index.html')

# API xử lý dữ liệu từ người dùng
@app.route('/solve', methods=['POST'])
def solve():
    data = request.json
    array = data.get('array', [])
    position = data.get('position')

    # Kiểm tra tính hợp lệ của mảng
    if not isinstance(array, list) or not array:
        return jsonify({'error': 'Invalid input. "array" must be a non-empty list of numbers.'}), 400

    if not all(isinstance(i, (int, float)) for i in array):
        return jsonify({'error': 'Invalid input. "array" must contain only numbers.'}), 400

    # Kiểm tra vị trí
    if not isinstance(position, int) or position < 0 or position >= len(array):
        return jsonify({'error': f'Invalid input. "position" must be an integer between 0 and {len(array) - 1}.'}), 400

    try:
        result = hill_climbing(array, position)
        return jsonify({'max_value': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
