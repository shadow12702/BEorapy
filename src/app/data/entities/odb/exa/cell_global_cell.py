from app.data.entities.odb.exa.cell_global import OdbExaCellGlobal

class OdbExaCellGlobalCell(OdbExaCellGlobal):

    CellName: str
    
    key_map = {
        'CELL_NAME' : 'CellName',
        **OdbExaCellGlobal.key_map
    }

    def __init__(self, **kwargs):
        """
        ExaCellGlobalCell model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for ExaCellGlobalCell.
        """
        super().__init__(**kwargs)
