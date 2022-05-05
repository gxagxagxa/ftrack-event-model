from ftrack_api.session import Session

from ftrack_event_model.schema.base import FtrackEventBaseModel


class FtrackAPISessionConfigureLocationDataModel(FtrackEventBaseModel):
    session: Session


class FtrackAPISessionConfigureLocationModel(FtrackEventBaseModel):
    data: FtrackAPISessionConfigureLocationDataModel
