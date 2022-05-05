from ftrack_api.session import Session

from ftrack_event_model.schema.base import FtrackEventBaseModel


class FtrackAPISessionReadyDataModel(FtrackEventBaseModel):
    session: Session


class FtrackAPISessionReadyModel(FtrackEventBaseModel):
    data: FtrackAPISessionReadyDataModel
