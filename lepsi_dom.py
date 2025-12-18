def tree(p):
    for y in range(4):
        blocks.place(Block.LOG_OAK, positions.add(p, world(0, y, 0)))
    blocks.fill(Block.LEAVES_OAK,
        positions.add(p, world(-2, 3, -2)),
        positions.add(p, world(2, 5, 2)),
        FillOperation.REPLACE)

def build():
    w, l, h = 7, 10, 4
    s = player.position()

    for i in range(3):
        o = positions.add(s, world(i * (w + 7), 0, 0))

        for x in range(w):
            for z in range(l):
                for y in range(h):
                    if x in (0, w-1) or z in (0, l-1):
                        blocks.place(Block.STRIPPED_DARK_OAK_WOOD,
                            positions.add(o, world(x, y, z)))

        blocks.fill(Block.AIR,
            positions.add(o, world(1, 1, 1)),
            positions.add(o, world(w-2, h-1, l-2)),
            FillOperation.REPLACE)

        for x in range(w):
            for z in range(l):
                blocks.place(Block.PLANKS_DARK_OAK,
                    positions.add(o, world(x, -1, z)))
                blocks.place(Block.SMOOTH_STONE_SLAB,
                    positions.add(o, world(x, h, z)))

        blocks.place(Block.OAK_DOOR, positions.add(o, world(2, 0, 0)))

        if i < 2:
            tree(positions.add(o, world(w+2, 0, l//2)))

player.on_chat("dom", build)
