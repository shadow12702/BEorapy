
from app.data.entities.odb.undo_config import OdbUndoConfig


class NonCdbUndoConfig(OdbUndoConfig):
    
    MaxCon: object

    key_map = {
        **OdbUndoConfig.key_map,
        'MAXCON': 'MaxCon'
    }

    def __init__(self, **kwargs):
        """
        NonCdbUndoConfig model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbUndoConfig.
        """
        super().__init__(**kwargs)
