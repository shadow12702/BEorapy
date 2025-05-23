from base.domain.base_entity import BaseEntity
from datetime import datetime
from numpy import float64

class NonCdbDbaHistoryStatistic(BaseEntity):

    DbName: str
    InstanceName: str
    SnapId: float64
    Dbid: float64
    SnapTime: datetime
    Recursivecpu: float64
    Prstmcpu: float64
    Cpuuse: float64
    Ucom: float64
    Tnxroll: float64
    Uroll: float64
    Execcnt: float64
    Ucall: float64
    Recurcall: float64
    Tbfbi: float64
    Tbfcr: float64
    Tbsrf: float64
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
    Ph: float64
    Pt: float64
    Pf: float64
    Crl: float64
    Opccul: float64
    Occ: float64
    Cauthen: float64
    Pcc: float64
    Sccc: float64
    Scch: float64
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
    Pwtt: float64
    Prtt: float64
    Pwfc: float64
    Pwd: float64
    Prfc: float64
    Prd: float64
    Prtiops: float64
    Prtmiops: float64
    Prtsiops: float64
    Pwtiops: float64
    Pwtmiops: float64
    Pwtsiops: float64
    Rdiops: float64
    Prts: float64
    Pwts: float64
    Rds: float64
    Rdw: float64
    Brfc: float64
    Brcdl: float64
    Bstc: float64
    Bstdl: float64
    Gccrbr: float64
    Gccrbs: float64
    Gccurbr: float64
    Gccurbs: float64
    Gbl: float64
    Wemp: float64
    Weop: float64
    Wep: float64
    Slg: float64
    Slrim: float64
    Lcr: float64
    Lcu: float64
    Ulcu: float64
    Blc: float64
    Iowait: float64

    key_map = {
        'DB_NAME': 'DbName',
        'INSTANCE_NAME': 'InstanceName',
        'SNAP_ID': 'SnapId',
        'DBID': 'Dbid',
        'SNAP_TIME': 'SnapTime',
        'RECURSIVECPU': 'Recursivecpu',
        'PRSTMCPU': 'Prstmcpu',
        'CPUUSE': 'Cpuuse',
        'UCOM': 'Ucom',
        'TNXROLL': 'Tnxroll',
        'UROLL': 'Uroll',
        'EXECCNT': 'Execcnt',
        'UCALL': 'Ucall',
        'RECURCALL': 'Recurcall',
        'TBFBI': 'Tbfbi',
        'TBFCR': 'Tbfcr',
        'TBSRF': 'Tbsrf',
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
        'PH': 'Ph',
        'PT': 'Pt',
        'PF': 'Pf',
        'CRL': 'Crl',
        'OPCCUL': 'Opccul',
        'OCC': 'Occ',
        'CAUTHEN': 'Cauthen',
        'PCC': 'Pcc',
        'SCCC': 'Sccc',
        'SCCH': 'Scch',
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
        'PWTT': 'Pwtt',
        'PRTT': 'Prtt',
        'PWFC': 'Pwfc',
        'PWD': 'Pwd',
        'PRFC': 'Prfc',
        'PRD': 'Prd',
        'PRTIOPS': 'Prtiops',
        'PRTMIOPS': 'Prtmiops',
        'PRTSIOPS': 'Prtsiops',
        'PWTIOPS': 'Pwtiops',
        'PWTMIOPS': 'Pwtmiops',
        'PWTSIOPS': 'Pwtsiops',
        'RDIOPS': 'Rdiops',
        'PRTS': 'Prts',
        'PWTS': 'Pwts',
        'RDS': 'Rds',
        'RDW': 'Rdw',
        'BRFC': 'Brfc',
        'BRCDL': 'Brcdl',
        'BSTC': 'Bstc',
        'BSTDL': 'Bstdl',
        'GCCRBR': 'Gccrbr',
        'GCCRBS': 'Gccrbs',
        'GCCURBR': 'Gccurbr',
        'GCCURBS': 'Gccurbs',
        'GBL': 'Gbl',
        'WEMP': 'Wemp',
        'WEOP': 'Weop',
        'WEP': 'Wep',
        'SLG': 'Slg',
        'SLRIM': 'Slrim',
        'LCR': 'Lcr',
        'LCU': 'Lcu',
        'ULCU': 'Ulcu',
        'BLC': 'Blc',
        'IOWAIT': 'Iowait'
    }

    def __init__(self, **kwargs):
        """
        NonCdbDbaHistoryStatistic model, inheriting from BaseModel.

        Args:
            **kwargs: The kwargs for NonCdbDbaHistoryStatistic.
        """
        super().__init__(**kwargs)
