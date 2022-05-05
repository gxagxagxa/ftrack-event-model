from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackStorageScenarioConfigureModel(NestedDataModel):
    scenario_id: str


class FtrackStorageScenarioConfigureModel(FtrackEventBaseModel):
    data: FtrackStorageScenarioConfigureModel
