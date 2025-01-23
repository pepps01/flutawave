from flask import jsonify

class ApiResource:
    def __init__(self):
        pass
    
    @staticmethod
    def errorResponse(data, message="Error in response",error=False, response_code=403):
        return jsonify({
            "data":data,
            "message":message,
            "error":error,
            "code":response_code
        })

        
    @staticmethod
    def response(data, message="Error in response", response_code = 200):
        return jsonify({
            "data":data,
            "message":message,
            "code":response_code
        })
