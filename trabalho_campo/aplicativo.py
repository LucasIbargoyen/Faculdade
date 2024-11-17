from flask import Flask, render_template, request, jsonify
from logica import criarCampoMinado, fazer_movimento

app = Flask(__name__)
campoMinado = criarCampoMinado(10, 10, 20)

@app.route('/')
def index():
    return render_template('index.html')

def make_move(minefield, row, col): 
    if minefield[row][col] == -1: return "Game Over" 
    return minefield[row][col]

@app.route('/make_move', methods=['POST'])
def move():
    data = request.json
    row = data.get('row')
    col = data.get('col')
    result = fazer_movimento(campoMinado, row, col)
    with open('moves.json', 'a') as f:
        f.write(f"Move: {row}, {col} - Result: {result}\n")
    return jsonify(success=True, result=result)

if __name__ == '__main__':
    app.run(debug=True)
