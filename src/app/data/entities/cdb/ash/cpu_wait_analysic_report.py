
from app.data.entities.odb.ash.cpu_wait_analysic_report import OdbAshCpuWaitAnalysicReport


class CdbAshCpuWaitAnalysicReport(OdbAshCpuWaitAnalysicReport):

    PdbName: str

    key_map = {
        'PDB_NAME': 'PdbName',
        **OdbAshCpuWaitAnalysicReport.key_map
    }
    
    def __init__(self, **kwargs):
        """
        CdbAshCpuWaitAnalysicReport model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbAshCpuWaitAnalysicReport.
        """
        super().__init__(**kwargs)