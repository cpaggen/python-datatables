from flask import Flask, render_template, request
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

data = [{"name": "leaf_101", "rack": "rack_1", "bgp": "65001","loopback": "1.1.1.1/32"}]

@app.route('/')
def index():
    return render_template('basic_table.html', title='Basic Table',
                           tors=data)
@app.route('/postStuff', methods=['GET','POST'])
def postStuff():
    # the JS code POSTs this to us: [{name: "leaf-1-name", value: "leaf_101"}, {name: "leaf-1-rack", value: "rack_1"},…]
    # the entire table is sent as a big list of elements
    # each row from the table always contains 4 elements like this:
    # 0: {name: "leaf-n-name", value: "leaf_n"} 
    # 1: {name: "leaf-n-rack", value: "rack_n"}
    # 2: {name: "leaf-n-as", value: "asNumber"}
    # 3: {name: "leaf-n-loopback", value: "ip/mask"}
    # so if the table contains two rows, we receive a list with 8 elements (0 to 7)
    # this function really does nothing useful, it simply logs the received data so you can further process it
    tableData = request.data
    app.logger.info('Received %s' % tableData)
    return render_template('basic_table.html', title='Posted', tors=data)

if __name__ == '__main__':
    app.run()
