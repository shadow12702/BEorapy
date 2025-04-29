from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class CdbDbaHistoryStatistic(BaseEntity):

    SnapTime: datetime
    DbName: str
    InstanceName: str
    PdbName: str
    Recursivecpu: float64
    Prstmcpu: float64
    Cpuuse: float64
    Ucom: float64
    Tnxroll: float64
    Uroll: float64
    Recurcall: float64
    Ucall: float64
    Execcnt: float64
    Tbfbi: float64
    Tbfcr: float64
    Tbsrf: float64
    Crl: float64
    Opccul: float64
    Occ: float64
    Cauthen: float64
    Pcc: float64
    Sccc: float64
    Scch: float64
    Dfo: float64
    Ddl: float64
    Dml: float64
    Qr: float64
    Ndg: float64
    Dgs: float64
    Dg1: float64
    Dg2: float64
    Dg3: float64
    Dg4: float64
    Pt: float64
    Ph: float64
    Pf: float64
    Lr: float64
    Lw: float64
    Sd: float64
    Sm: float64
    Rdlsr: float64
    Ren: float64
    Rbw: float64
    Rbar: float64
    Lts: float64
    Sts: float64
    Tscp: float64
    Tsdr: float64
    Tsrr: float64
    Idxdr: float64
    Idxff: float64
    Idxrr: float64
    Idxrs: float64
    StatName: str
    Writes: float64

    key_map = {
        'SNAP_TIME': 'SnapTime',
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'PDB_NAME': 'PdbName',
        'RECURSIVECPU': 'Recursivecpu',
        'PRSTMCPU': 'Prstmcpu',
        'CPUUSE': 'Cpuuse',
        'UCOM': 'Ucom',
        'TNXROLL': 'Tnxroll',
        'UROLL': 'Uroll',
        'RECURCALL': 'Recurcall',
        'UCALL': 'Ucall',
        'EXECCNT': 'Execcnt',
        'TBFBI': 'Tbfbi',
        'TBFCR': 'Tbfcr',
        'TBSRF': 'Tbsrf',
        'CRL': 'Crl',
        'OPCCUL': 'Opccul',
        'OCC': 'Occ',
        'CAUTHEN': 'Cauthen',
        'PCC': 'Pcc',
        'SCCC': 'Sccc',
        'SCCH': 'Scch',
        'DFO': 'Dfo',
        'DDL': 'Ddl',
        'DML': 'Dml',
        'QR': 'Qr',
        'NDG': 'Ndg',
        'DGS': 'Dgs',
        'DG1': 'Dg1',
        'DG2': 'Dg2',
        'DG3': 'Dg3',
        'DG4': 'Dg4',
        'PT': 'Pt',
        'PH': 'Ph',
        'PF': 'Pf',
        'LR': 'Lr',
        'LW': 'Lw',
        'SD': 'Sd',
        'SM': 'Sm',
        'RDLSR': 'Rdlsr',
        'REN': 'Ren',
        'RBW': 'Rbw',
        'RBAR': 'Rbar',
        'LTS': 'Lts',
        'STS': 'Sts',
        'TSCP': 'Tscp',
        'TSDR': 'Tsdr',
        'TSRR': 'Tsrr',
        'IDXDR': 'Idxdr',
        'IDXFF': 'Idxff',
        'IDXRR': 'Idxrr',
        'IDXRS': 'Idxrs',
        'STAT_NAME': 'StatName',
        'WRITES': 'Writes'
    }

    def __init__(self, **kwargs):
        """
        CdbDbaHistoryStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for CdbDbaHistoryStatistic.
        """
        super().__init__(**kwargs)

    