import json

all_l = []
node_list = []

def get_key(data, key_w, last_item=None):
    global all_l
    global node_list
    if_pop_list = True
    if isinstance(data, list):
        if data == []:
            node_list.pop(len(node_list) - 1)
            return None
        for id,v in enumerate(data):
            node_list.append("[%d]" % id)
            get_key(v, key_w, 'list')
    elif isinstance(data, dict):
        for key, value in data.items():
            node_list.append(key)
            get_key(value, key_w, 'dict')
    else:
        data = str(data)
        if data == key_w:
            #import pdb;pdb.set_trace()
            node_list.append(data)
            all_l.append(node_list.copy())
            node_list.pop(len(node_list) - 1)
    
    if node_list and if_pop_list:
        node_list.pop(len(node_list) - 1)


with open('./fuck.json', 'r') as data_file:
    data = json.loads(data_file.read())
    get_key(data=data, key_w="飘尘")


for i in all_l:
    print(" => ".join(i))
