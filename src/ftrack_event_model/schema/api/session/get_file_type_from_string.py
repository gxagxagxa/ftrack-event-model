from ftrack_event_model.schema.base import NestedDataModel, FtrackEventBaseModel


class FtrackAPISessionGetFileTypeFromStringDataModel(NestedDataModel):
    file_path: str


class FtrackAPISessionGetFileTypeFromStringModel(FtrackEventBaseModel):
    data: FtrackAPISessionGetFileTypeFromStringDataModel
