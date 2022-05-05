from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackMetaConnectedDataModel(NestedDataModel):
    pass


class FtrackMetaConnectedModel(FtrackEventBaseModel):
    data: FtrackMetaConnectedDataModel
