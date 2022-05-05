def event_model_factory(event):
    topic = event.get('topic', '')

    if topic == 'ftrack.update':
        import ftrack_event_model.schema.update
        return ftrack_event_model.schema.update.FtrackUpdateModel(**event)

    if topic.startswith('ftrack.meta'):
        if topic == 'ftrack.meta.connected':
            import ftrack_event_model.schema.meta.connected
            return ftrack_event_model.schema.meta.connected.FtrackMetaConnectedModel(**event)

    if topic.startswith('ftrack.api'):
        if topic.startswith('ftrack.api.session'):
            if topic == 'ftrack.api.session.configure-location':
                import ftrack_event_model.schema.api.session.configure_location
                return ftrack_event_model.schema.api.session.configure_location.FtrackAPISessionConfigureLocationModel(
                    **event)
            if topic == 'ftrack.api.session.ready':
                import ftrack_event_model.schema.api.session.ready
                return ftrack_event_model.schema.api.session.ready.FtrackAPISessionReadyModel(**event)
            if topic == 'ftrack.api.session.construct-entity-type':
                import ftrack_event_model.schema.api.session.construct_entity_type
                return ftrack_event_model.schema.api.session.construct_entity_type.FtrackAPISessionConstructEntityTypeModel(
                    **event)

    if topic.startswith('ftrack.storage-scenario'):
        if topic == 'ftrack.storage-scenario.discover':
            import ftrack_event_model.schema.storage_scenario.discover
            return ftrack_event_model.schema.storage_scenario.discover.FtrackStorageScenarioDiscoverModel(**event)
        if topic == 'ftrack.storage-scenario.configure':
            import ftrack_event_model.schema.storage_scenario.configure
            return ftrack_event_model.schema.storage_scenario.configure.FtrackStorageScenarioConfigureModel(**event)
        if topic == 'ftrack.storage-scenario.configure-done':
            import ftrack_event_model.schema.storage_scenario.configure_done
            return ftrack_event_model.schema.storage_scenario.configure_done.FtrackStorageScenarioConfigureDoneModel(
                **event)
        if topic == 'ftrack.storage-scenario.activate':
            import ftrack_event_model.schema.storage_scenario.activate
            return ftrack_event_model.schema.storage_scenario.activate.FtrackStorageScenarioActivateModel(**event)

    if topic.startswith('ftrack.action'):
        if topic == 'ftrack.action.discover':
            import ftrack_event_model.schema.action.discover
            return ftrack_event_model.schema.action.discover.FtrackActionDiscoverModel(**event)
        if topic == 'ftrack.action.launch':
            import ftrack_event_model.schema.action.launch
            return ftrack_event_model.schema.action.launch.FtrackActionLaunchModel(**event)
        if topic == 'ftrack.action.trigger-user-interface':
            import ftrack_event_model.schema.action.trigger_user_interface
            return ftrack_event_model.schema.action.trigger_user_interface.FtrackActionTriggerUserInterfaceModel(
                **event)

    if topic.startswith('ftrack.location'):
        if topic == 'ftrack.location.component-added':
            import ftrack_event_model.schema.location.component_added
            return ftrack_event_model.schema.location.component_added.FtrackLocationComponentAddedModel(**event)
        if topic == 'ftrack.location.request-resolve':
            import ftrack_event_model.schema.location.request_resolve
            return ftrack_event_model.schema.location.request_resolve.FtrackLocationRequestResolveModel(**event)

    return None
