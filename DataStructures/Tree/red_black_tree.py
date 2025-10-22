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

