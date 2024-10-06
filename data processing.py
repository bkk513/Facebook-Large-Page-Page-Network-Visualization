import pandas as pd
import json

# 读取两个表
edges = pd.read_csv('musae_facebook_edges.csv', delimiter=',', names=['id_1', 'id_2'])
nodes = pd.read_csv('musae_facebook_target.csv', delimiter=',', names=['id', 'facebook_id', 'page_name', 'page_type'])

# 将所有涉及合并的列转换为字符串类型
edges['id_1'] = edges['id_1'].astype(str)
edges['id_2'] = edges['id_2'].astype(str)
nodes['id'] = nodes['id'].astype(str)

# 创建 nodes 列表
nodes_list = nodes.to_dict(orient='records')

# 创建 edges 列表
edges_list = edges.rename(columns={'id_1': 'source', 'id_2': 'target'}).to_dict(orient='records')

# 生成最终的 JSON 结构
graph = {
    "nodes": nodes_list,
    "links": edges_list
}

# 保存为 JSON 文件
with open('graph.json', 'w', encoding='utf-8') as f:
    json.dump(graph, f, ensure_ascii=False, indent=4)

# 预览生成的 JSON 数据
print(json.dumps(graph, ensure_ascii=False, indent=4))
