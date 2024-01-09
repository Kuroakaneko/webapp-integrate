from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/numericalintegralservice/<lower>/<upper>')
def numerical_integration_combined(lower, upper):
    def f(x):
        return abs(math.sin(x))

    def numerical_integration(lower, upper, N):
        interval_width = (upper - lower) / N
        result = 0.5 * (f(lower) + f(upper))

        for i in range(1, N):
            x_i = lower + i * interval_width
            result += f(x_i)

        result *= interval_width
        return result

    results_dict = {}

    for i in range(0, 7):
        result = numerical_integration(float(lower), float(upper), 10**i)
        results_dict[f"result_{10**i}_intervals"] = result

    return jsonify(results_dict)

if __name__ == '__main__':
    app.run()

