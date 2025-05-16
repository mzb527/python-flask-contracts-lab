from flask import Flask, jsonify

app = Flask(__name__)

# Updated customer data
customers = {"bob", "bill", "john", "sarah"}

# Updated contract details
contracts = {
    "shed": {"party": "John", "purpose": "Building a shed"},
    "business_dec": {"party": "Company", "purpose": "DEC for a business"}
}

# Route to retrieve contract details
@app.route("/contract/<id>")
def get_contract(id):
    contract_info = contracts.get(id.lower())
    if contract_info:
        return jsonify(contract_info), 200
    return jsonify({"error": "Contract not found"}), 404

# Route to verify customer existence without sharing details
@app.route("/customer/<customer_name>")
def check_customer(customer_name):
    if customer_name.lower() in customers:
        return "", 204  # Customer found, but no data shared
    return jsonify({"error": "Customer not found"}), 404

# Global error handlers
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Route not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)