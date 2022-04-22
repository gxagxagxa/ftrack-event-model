from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel


class FtrackEventMetaConnectedDataModel(NestedDataModel):
    pass


class FtrackEventMetaConnectedModel(FtrackEventBaseModel):
    data: FtrackEventMetaConnectedDataModel
