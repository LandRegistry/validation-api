from validation_api.schema.v1_0.semantics import geometry_extent_count, validate_geometry


validation_rules = [
    geometry_extent_count,
    validate_geometry
]
