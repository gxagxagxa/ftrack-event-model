from typing import Optional

from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackConnectPluginVerifyStartupDataStorageScenarioDataAccessorMountPointModel(NestedDataModel):
    windows: Optional[str]
    osx: Optional[str]
    linux: Optional[str]


class FtrackConnectPluginVerifyStartupDataStorageScenarioDataAccessorModel(NestedDataModel):
    mount_points: FtrackConnectPluginVerifyStartupDataStorageScenarioDataAccessorMountPointModel


class FtrackConnectPluginVerifyStartupDataStorageScenarioDataModel(NestedDataModel):
    location_id: str
    location_name: str
    accessor: FtrackConnectPluginVerifyStartupDataStorageScenarioDataAccessorModel


class FtrackConnectPluginVerifyStartupDataStorageScenarioModel(NestedDataModel):
    data: FtrackConnectPluginVerifyStartupDataStorageScenarioDataModel
    scenario: str


class FtrackConnectPluginVerifyStartupDataModel(NestedDataModel):
    storage_scenario: FtrackConnectPluginVerifyStartupDataStorageScenarioModel


class FtrackConnectPluginVerifyStartupModel(FtrackEventBaseModel):
    data: FtrackConnectPluginVerifyStartupDataModel
