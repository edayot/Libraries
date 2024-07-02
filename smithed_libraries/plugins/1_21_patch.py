
from beet import Context

def beet_default(ctx: Context):
    ctx.data.structures.proxy_key.scope = ("structure",)
    ctx.data.advancements.proxy_key.scope = ("advancement",)
    ctx.data.recipes.proxy_key.scope = ("recipe",)
    ctx.data.loot_tables.proxy_key.scope = ("loot_table",)
    ctx.data.predicates.proxy_key.scope = ("predicate",)
    ctx.data.item_modifiers.proxy_key.scope = ("item_modifier",)
    ctx.data.functions.proxy_key.scope = ("function",)
    ctx.data.function_tags.proxy_key.scope = ("tags", "function")
    ctx.data.item_tags.proxy_key.scope = ("tags", "item")
    ctx.data.block_tags.proxy_key.scope = ("tags", "block")
    ctx.data.entity_type_tags.proxy_key.scope = ("tags", "entity_type")
    ctx.data.fluid_tags.proxy_key.scope = ("tags", "fluid")
    ctx.data.game_event_tags.proxy_key.scope = ("tags", "game_event")
    ctx.data.pack_format = 48
    ctx.assets.pack_format = 34
    