from ftrack_event_model.schema.base import FtrackEventBaseModel, NestedDataModel


class FtrackStorageScenarioConfigureDoneDataModel(NestedDataModel):
    pass


class FtrackStorageScenarioConfigureDoneModel(FtrackEventBaseModel):
    data: FtrackStorageScenarioConfigureDoneDataModel
