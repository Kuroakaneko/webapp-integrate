from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import math

app = Flask(__name__)
api = Api(app)

class NumericalIntegration(Resource):
    def get(self, lower, upper):
        lower = float(lower)
        upper = float(upper)

        for i in range (0, 7):
            globals()['res{}'.format(i)] = self.numerical_integration(lower, upper, 10**i)

        return jsonify({'value with 1 interval': res0,
                        'value with 2 intervals': res1,
                        'value with 3 intervals': res2,
                        'value with 4 intervals': res3,
                        'value with 5 intervals': res4,
                        'value with 6 intervals': res5,
                        'value with 7 intervals': res6,
                        })


    def numerical_integration(self, lower, upper, N):
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
