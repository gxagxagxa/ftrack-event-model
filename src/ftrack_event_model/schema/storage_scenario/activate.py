from typing import Optional

from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackStorageScenarioActivateDataStorageScenarioDataAccessorMountPointModel(NestedDataModel):
    windows: Optional[str]
    osx: Optional[str]
    linux: Optional[str]


class FtrackStorageScenarioActivateDataStorageScenarioDataAccessorModel(NestedDataModel):
    mount_points: FtrackStorageScenarioActivateDataStorageScenarioDataAccessorMountPointModel


class FtrackStorageScenarioActivateDataStorageScenarioDataModel(NestedDataModel):
    location_id: str
    location_name: str
    accessor: FtrackStorageScenarioActivateDataStorageScenarioDataAccessorModel


class FtrackStorageScenarioActivateDataStorageScenarioModel(NestedDataModel):
    data: FtrackStorageScenarioActivateDataStorageScenarioDataModel
    scenario: str


class FtrackStorageScenarioActivateDataModel(NestedDataModel):
    storage_scenario: FtrackStorageScenarioActivateDataStorageScenarioModel


class FtrackStorageScenarioActivateModel(FtrackEventBaseModel):
    data: FtrackStorageScenarioActivateDataModel
