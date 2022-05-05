from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackLocationComponentAddedDataModel(NestedDataModel):
    component_id: str
    location_id: str


class FtrackLocationComponentAddedModel(FtrackEventBaseModel):
    data: FtrackLocationComponentAddedDataModel
