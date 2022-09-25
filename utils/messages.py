def success(data, message="Successful"):
    return {"success": True, "message": message, "data": data}


def failure(message="Something went wrong"):
    return {"success": False, "message": message}
