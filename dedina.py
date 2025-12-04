def build_house():
    width = 10
    length = 10
    height = 4

    start = player.position()

    for x in range(width):
        for z in range(length):
            for y in range(height):
                if x == 0 or x == width - 1 or z == 0 or z == length - 1:
                    blocks.place(Block.STRIPPED_SPRUCE_WOOD, positions.add(start, world(x, y, z)))

    blocks.fill(
        Block.AIR,
        positions.add(start, world(1, 1, 1)),
        positions.add(start, world(width - 2, height - 1, length - 2)),
        FillOperation.REPLACE
    )

    blocks.place(Block.DARK_OAK_DOOR, positions.add(start, world(2, 0, 0)))

    for x in range(width):
        for z in range(length):
            blocks.place(Block.STONE_BRICKS_SLAB, positions.add(start, world(x, height, z)))

player.on_chat("dom", build_house)
