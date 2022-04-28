# ftrack-event-model

Convert ftrack event dict-like structure into more friendly object. Powered
by [Pydantic](https://pydantic-docs.helpmanual.io) base model.

ftrack event models have the following features:

- minimal changes on your existing codes.
- support IDE completion, prevent from type errors.
- data conversion and validation.

# How to use?

eg, we want to listen `ftrack.update` event, and get some useful information. The original code may be like:

```python
# remember all key names
event['data']['entities'][0]['changes']
```

With ftrack-event-model, it looks like：

```python
# convert event to event model
event_model = FtrackEventUpdateModel(**event)
# support IDE completion!
event.data.entities[0].changes
```

# Examples

## listen to `ftrack.update` event

```python
from functools import partial

import ftrack_api.event.base

from ftrack_event_model import event_model_factory


def handler(session: ftrack_api.Session,
            event: ftrack_api.event.base.Event):
    event_model = event_model_factory(event)
    for entity in event_model.data.entities:
        changes = entity.changes
        # ... do something with changes ...


def register(session: ftrack_api.Session):
    handler_with_session = partial(handler, session)
    session.event_hub.subscribe(
        'topic=ftrack.update',
        handler_with_session
    )


if __name__ == '__main__':
    session = ftrack_api.Session(auto_connect_event_hub=True)
    register(session)
    session.event_hub.wait()

```