from DataStructures.Tree import rbt_node as rb


def default_compare(key, element):
   if key == rb.get_key(element):
      return 0
   elif key > rb.get_key(element):
      return 1
   return -1

def rotate_left(node_rbt):
   node = node_rbt["right"]
   node_rbt["right"] = node["left"]
   node["left"] = node_rbt
   node["color"] = node_rbt["color"]
   rb.change_color(node_rbt, 0)
   node_rbt["size"] = size(node_rbt["left"]) + size(node_rbt["right"]) + 1
   node["size"] = size(node["left"]) + size(node["right"]) + 1
   return node
   
def rotate_right(node_rbt):
   node = node_rbt["left"]
   node_rbt["left"] = node["right"]
   node["right"] = node_rbt
   node["color"] = node_rbt["color"]
   rb.change_color(node_rbt, 0)
   node_rbt["size"] = size(node_rbt["left"]) + size(node_rbt["right"]) + 1
   node["size"] = size(node["left"]) + size(node["right"]) + 1
   return node
   
  
   
def size_tree(root):
   if root is None:
      return 0
   else:
      return 1 + size_tree(root["left"]) + size_tree(root["right"])
   
def size(my_bst):
   if my_bst is None:
      return 0
   else:
      return size_tree(my_bst)
   