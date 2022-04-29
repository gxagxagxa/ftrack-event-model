from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel


class FtrackEventLocationComponentAddedDataModel(NestedDataModel):
    component_id: str
    location_id: str


class FtrackEventLocationComponentAddedModel(FtrackEventBaseModel):
    data: FtrackEventLocationComponentAddedDataModel
