from flask import Flask, render_template, request, jsonify
from two_sum_presort import find_two_sum_presort

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            # Get array input and convert to list of floats
            arr_input = request.form['array']
            arr = [float(x.strip()) for x in arr_input.split(',')]
            
            # Get target sum
            target_sum = float(request.form['target'])
            
            # Find the pair
            found, pair = find_two_sum_presort(arr, target_sum)
            
            result = {
                'array': arr,
                'target': target_sum,
                'found': found,
                'pair': pair if found else None
            }
        except ValueError:
            result = {'error': 'Please enter valid numbers'}
        except Exception as e:
            result = {'error': str(e)}
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True) 