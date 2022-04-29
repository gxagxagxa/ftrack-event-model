from ftrack_event_model.base import FtrackEventBaseModel, NestedDataModel


class FtrackEventStorageScenarioConfigureDoneDataModel(NestedDataModel):
    pass


class FtrackEventStorageScenarioConfigureDoneModel(FtrackEventBaseModel):
    data: FtrackEventStorageScenarioConfigureDoneDataModel()
