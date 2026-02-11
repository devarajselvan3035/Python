# Source - https://stackoverflow.com/a
# Posted by Alejandro Mera, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-26, License - CC BY-SA 4.0


def PrintTree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    nlevels = height(root)
    width = pow(2, nlevels + 1)

    q = [(root, 0, width, "c")]
    levels = []

    while q:
        node, level, x, align = q.pop(0)
        if node:
            if len(levels) <= level:
                levels.append([])

            levels[level].append([node, level, x, align])
            seg = width // (pow(2, level + 1))
            q.append((node.left, level + 1, x - seg, "l"))
            q.append((node.right, level + 1, x + seg, "r"))

    for i, l in enumerate(levels):
        pre = 0
        preline = 0
        linestr = ""
        pstr = ""
        seg = width // (pow(2, i + 1))
        for n in l:
            valstr = str(n[0].value)
            if n[3] == "r":
                linestr += (
                    " " * (n[2] - preline - 1 - seg - seg // 2)
                    + "¯" * (seg + seg // 2)
                    + "\\"
                )
                preline = n[2]
            if n[3] == "l":
                linestr += " " * (n[2] - preline - 1) + "/" + "¯" * (seg + seg // 2)
                preline = n[2] + seg + seg // 2
            pstr += (
                " " * (n[2] - pre - len(valstr)) + valstr
            )  # correct the potition acording to the number size
            pre = n[2]
        print(linestr)
        print(pstr)
