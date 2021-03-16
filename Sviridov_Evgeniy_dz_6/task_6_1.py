def parsed_line(line_def):
    start = 0
    end = line_def.find(' -')
    remote_address = line_def[start:end]
    start = line_def.find('"') + 1
    end = line_def.find(' ', start)
    request_type = line_def[start:end]
    start = end + 1
    end = line_def.find(' ', start)
    requested_resource = line_def[start:end]
    return remote_address, request_type, requested_resource


parsed_file = (parsed_line(row) for row in open('nginx_logs.txt'))

for el in parsed_file:
    print(el)
