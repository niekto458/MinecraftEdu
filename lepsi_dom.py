def build_tree(pos):
    # kmeň
    for y in range(4):
        blocks.place(Block.OAK_LOG, positions.add(pos, world(0, y, 0)))

    # listy
    blocks.fill(
        Block.OAK_LEAVES,
        positions.add(pos, world(-2, 3, -2)),
        positions.add(pos, world(2, 5, 2)),
        FillOperation.REPLACE
    )


def build_house():
    width = 7
    length = 10
    height = 4

    start = player.position()

    for i in range(3):
        offset = positions.add(start, world(i * (width + 6), 0, 0))

        # steny
        for x in range(width):
            for z in range(length):
                for y in range(height):
                    if x == 0 or x == width - 1 or z == 0 or z == length - 1:
                        blocks.place(
                            Block.STRIPPED_DARK_OAK_WOOD,
                            positions.add(offset, world(x, y, z))
                        )

        # vnútro
        blocks.fill(
            Block.AIR,
            positions.add(offset, world(1, 1, 1)),
            positions.add(offset, world(width - 2, height - 1, length - 2)),
            FillOperation.REPLACE
        )

        # podlaha
        for x in range(width):
            for z in range(length):
                blocks.place(
                    Block.DARK_OAK_PLANKS,
                    positions.add(offset, world(x, -1, z))
                )

        # dvere
        blocks.place(Block.OAK_DOOR, positions.add(offset, world(2, 0, 0)))

        # strecha
        for x in range(width):
            for z in range(length):
                blocks.place(
                    Block.SMOOTH_STONE_SLAB,
                    positions.add(offset, world(x, height, z))
                )

        # 🌳 strom medzi domami (nie za posledným)
        if i < 2:
            tree_pos = positions.add(offset, world(width + 2, 0, length // 2))
            build_tree(tree_pos)


player.on_chat("dom", build_house)
