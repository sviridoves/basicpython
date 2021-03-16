def parsed_line(line_def):
    start = 0
    end = line_def.find(' -')
    remote_address = line_def[start:end]
    return remote_address


parsed_file = (parsed_line(row) for row in open('nginx_logs.txt'))
count_ip_requests = {}

for el in parsed_file:
    if el in count_ip_requests:
        count_ip_requests[el] += 1
    else:
        count_ip_requests[el] = 1

spamer_ip = max(count_ip_requests, key=count_ip_requests.get)
print(f'IP-адрес спамера: {spamer_ip}\nЗапросов сделано: {count_ip_requests[spamer_ip]}')
