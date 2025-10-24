from DataStructures.Tree import rbt_node as rb

def new_map ():
    rbt = {
        "root": None,
        "type": "RBT"
    }
    return rbt


def flip_node_color(node_rbt):
    if node_rbt is None:
        return "El nodo es None"
    elif rb.is_red(node_rbt):
        rb.change_color(node_rbt,"BLACK")
    else:
        rb.change_color(node_rbt,"RED")
    return node_rbt

def flip_colors(node_rbt):
    flip_node_color(node_rbt)
    flip_node_color(node_rbt["left"])
    flip_node_color(node_rbt["right"])
    return node_rbt


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

def insert_node(root, key, value):
   
   if root is not None:
      if key < root["key"]:
         root["left"] = insert_node(root["left"], key, value)
      elif key > root["key"]:
         root["right"] = insert_node(root["right"], key, value)
      else:
         root["value"] = value
      if rb.is_red(root["right"]) and not rb.is_red(root["left"]):
         root = rotate_left(root)
      if rb.is_red(root["left"]) and rb.is_red(root["left"]["left"]):
         root = rotate_right(root)
      if rb.is_red(root["left"]) and rb.is_red(root["right"]):
         flip_colors(root)
      
      root["size"] = size(root["left"]) + size(root["right"]) +1
      return root

def put(my_rbt, key, value):
   my_rbt["root"] = insert_node(my_rbt["root"], key, value)
   rb.change_color(my_rbt["root"], 1)
   return my_rbt


   