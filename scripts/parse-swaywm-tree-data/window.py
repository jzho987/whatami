
def _build_child_nodes(node_dict) -> list[Window]:
    child_nodes = node_dict["nodes"]
    if len(child_nodes) == 0:
        return None

    child_windows = []
    for node in child_nodes:
        child_windows.append(Window(node))

    return child_windows


class Window:
    def __init__(self, node_dict):
        assert "type" in node_dict, f"input missing attribute type in {node_dict}"

        if node_dict["type"] == "workspace":
            build_child_nodes
        elif node_dict["type"] == "workspace":

        assert "app_id" in node_dict, f"input missing attribute id in {node_dict}"
        assert "focused" in node_dict, (
            f"input missing attribute focussed in {node_dict}"
        )

        self.app_id = node_dict["app_id"]
        self.focused = node_dict["focused"]
