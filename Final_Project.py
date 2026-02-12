def tree(p):
    for y in range(4):
        blocks.place(Block.LOG_OAK,
            positions.add(p, world(0, y, 0)))

    blocks.fill(Block.LEAVES_OAK,
        positions.add(p, world(-2, 3, -2)),
        positions.add(p, world(2, 5, 2)),
        FillOperation.REPLACE)


def bench(p):
    blocks.place(Block.OAK_WOOD_SLAB,
     positions.add(p, world(0, 1, 0)))
    blocks.place(Block.OAK_WOOD_SLAB,
     positions.add(p, world(1, 1, 0)))

    blocks.place(Block.PLANKS_OAK,
     positions.add(p, world(0, 1, -1)))
    blocks.place(Block.PLANKS_OAK,
     positions.add(p, world(1, 1, -1)))


def lamp(p):
    blocks.place(Block.TUFF_WALL,
     positions.add(p, world(0, 1, 0)))
    blocks.place(Block.TUFF_WALL,
     positions.add(p, world(0, 2, 0)))
    blocks.place(Block.TUFF_WALL,
     positions.add(p, world(0, 3, 0)))
    blocks.place(Block.SEA_LANTERN, 
    positions.add(p, world(0, 4, 0)))


def build(count):
    w, l, h = 7, 10, 4
    gap = 7
    s = player.position()

    total_width = count * (w + gap)

    for x in range(total_width):
        blocks.place(Block.ANDESITE,
            positions.add(s, world(x, -1, -3)))

    for i in range(count):
        o = positions.add(s, world(i * (w + gap), 0, 0))

        for x in range(w):
            for z in range(l):
                for y in range(h):
                    if x in (0, w - 1) or z in (0, l - 1):
                        blocks.place(Block.STRIPPED_DARK_OAK_WOOD,
                            positions.add(o, world(x, y, z)))

        blocks.fill(Block.AIR,
            positions.add(o, world(1, 1, 1)),
            positions.add(o, world(w - 2, h - 1, l - 2)),
            FillOperation.REPLACE)

        for x in range(w):
            for z in range(l):
                blocks.place(Block.ANDESITE,
                    positions.add(o, world(x, -1, z)))
                blocks.place(Block.SMOOTH_STONE_SLAB,
                    positions.add(o, world(x, h, z)))

        blocks.place(Block.OAK_DOOR,
            positions.add(o, world(2, 0, 0)))

        for z in range(-1, -4, -1):
            blocks.place(Block.ANDESITE,
                positions.add(o, world(2, -1, z)))

        bench(positions.add(o, world(2, -1, -6)))
        lamp(positions.add(o, world(w + gap // 2, -1, -6)))
        tree(positions.add(o, world(w + gap // 2, 0, l // 2)))


player.on_chat("dom", build)
