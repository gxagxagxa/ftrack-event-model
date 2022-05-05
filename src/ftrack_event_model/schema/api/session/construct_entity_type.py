from typing import Any

from ftrack_event_model.schema.base import FtrackEventBaseModel


# class FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyRefModel(NestedDataModel):
#     ref: str = Field(..., alias='$ref')
#
#
# class FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyTypeModel(NestedDataModel):
#     type: str
#
#
# class FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyConfigurationIDModel(NestedDataModel):
#     alias_for: str
#     type: str
#     description: Optional[str]
#     format: str
#
#
# class FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyIDModel(NestedDataModel):
#     type: str
#     default: Optional[str]
#
#
# class FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyGroupModel(NestedDataModel):
#     ref: str = Field(..., alias='$ref')
#
#
# class FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyConfigurationModel(NestedDataModel):
#     alias_for: str
#     ref: str = Field(..., alias='$ref')
#
#
# class FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyAncestorsModel(NestedDataModel):
#     items: FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyGroupModel
#     type: str
#
#
# class FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyModel(NestedDataModel):
#     group: FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyRefModel
#     configuration_id: FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyConfigurationIDModel
#     to_id: FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyTypeModel
#     configuration: FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyConfigurationModel
#     id: FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyIDModel
#     from_id: FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyTypeModel
#     ancestors: Optional[FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyAncestorsModel]
#     name: Optional[FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyTypeModel]
#     parent: Optional[FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyRefModel]
#
#
# class FtrackEventAPISessionConstructEntityTypeDataSchemaModel(NestedDataModel):
#     properties: FtrackEventAPISessionConstructEntityTypeDataSchemaPropertyModel
#     default_projections: List[str]
#     computed: List[str]
#     primary_key: List[str]
#     required: List[str]
#     immutable: List[str]
#     type: str
#     id: str
#
#
# class FtrackEventAPISessionConstructEntityTypeDataModel(NestedDataModel):
#     schema: FtrackEventAPISessionConstructEntityTypeDataSchemaModel
#     schemas: List[FtrackEventAPISessionConstructEntityTypeDataSchemaModel]


class FtrackEventAPISessionConstructEntityTypeModel(FtrackEventBaseModel):
    data: Any
