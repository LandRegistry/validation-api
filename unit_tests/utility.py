

def result_contains_at(result, message, location):
    for item in result:
        if message in item['error_message'] and item['location'] == location:
            return True
    return False
