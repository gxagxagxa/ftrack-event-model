from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackConnectPluginConnectWidgetDataModel(NestedDataModel):
    pass


class FtrackConnectPluginConnectWidgetModel(FtrackEventBaseModel):
    data: FtrackConnectPluginConnectWidgetDataModel
