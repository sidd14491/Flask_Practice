import sumTwoNumbers
import diffTwoNumbers
import linux_cmd_output
import airthmatic

from flask import Flask, request
from flask_restful import Resource, Api
import pdb
pdb.set_trace()
app = Flask(__name__)
api = Api(app)


class sum(Resource):
    # pdb.set_trace()

    def get(self, first_number, second_number):
        return {'data': sumTwoNumbers.sumTwo(first_number, second_number)}
        return {'data': diffTwoNumbers.difftwonumber(first_number,
                                                     second_number)}


class diff(Resource):
    # pdb.set_trace()

    def get(self, first_number, second_number):
        return {'data': diffTwoNumbers.difftwonumber(first_number,
                                                     second_number)}


class linux_output(Resource):

    print(Resource.__name__.lower)

    def get(self, cmd):
            return {'data': linux_cmd_output.lnx_output(cmd)}


class AirthMatic(Resource):

      # pdb;pdb.set_trace()
      def get(self,func_name, first_number, second_number):
            print(type(func_name))
            print(func_name, first_number, second_number)
            if func_name == "sum":
                return {func_name: "{0}+{1}={2}".format(first_number, second_number, airthmatic.sumTwo(first_number, second_number))}
            elif func_name == "sub":
                return {func_name: "{0}-{1}={2}".format(first_number, second_number, airthmatic.difftwonumber(first_number, second_number))}
            elif func_name == "mul":
                return {func_name: "{0}*{1}={2}".format(first_number, second_number, airthmatic.multwonumber(first_number, second_number))}
            elif func_name =="div":
                return {func_name: "{0}/{1}={2}".format(first_number, second_number, airthmatic.divtwonumber(first_number, second_number))}


api.add_resource(sum, '/operation/sumtwo/<first_number>/<second_number>')
api.add_resource(diff, '/operation/difftwo/<first_number>/<second_number>')
api.add_resource(linux_output, '/lnx/<cmd>/')

api.add_resource(AirthMatic,
                 '/airth/<string:func_name>/<int:first_number>/<int:second_number>')

if __name__ == '__main__':
    # pdb.set_trace()
    app.run(debug=True)
