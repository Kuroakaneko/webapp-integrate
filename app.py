from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
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

    for i in range(0, 7):
        result = numerical_integration(lower, upper, 10**i)
        print(f"Numerical integration result with {10**i} intervals: {result}")


if __name__ == '__main__':
    app.run()
