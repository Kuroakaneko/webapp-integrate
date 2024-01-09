from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import math

app = Flask(__name__)
api = Api(app)

class NumericalIntegration(Resource):
    def get(self, lower, upper):
        lower = float(lower)
        upper = float(upper)

        result = self.numerical_integration(lower, upper)
        return jsonify({"result": result})

    def numerical_integration(self, lower, upper, N=1000):
        interval_width = (upper - lower) / N
        result = 0.5 * (self.f(lower) + self.f(upper))

        for i in range(1, N):
            x_i = lower + i * interval_width
            result += self.f(x_i)

        result *= interval_width
        return result

    def f(self, x):
        return abs(math.sin(x))

api.add_resource(NumericalIntegration, '/numericalintegralservice/<lower>/<upper>')

if __name__ == '__main__':
    app.run(debug=True)

