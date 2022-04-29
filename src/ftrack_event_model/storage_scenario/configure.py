from ftrack_event_model.base import NestedDataModel, FtrackEventBaseModel


class FtrackEventStorageScenarioConfigureModel(NestedDataModel):
    scenario_id: str


class FtrackEventStorageScenarioConfigureModel(FtrackEventBaseModel):
    data: FtrackEventStorageScenarioConfigureModel
