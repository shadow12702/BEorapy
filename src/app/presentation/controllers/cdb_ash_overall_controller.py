from fastapi import HTTPException
import pandas as pd
from app.models.responses.ash_overall_object_response import ChartModel, ChartResponse
from app.services.cdb_ash_overall_service import CdbAshOverallService
from app.models.request_model import AshOverallRequest
from helper import helper

class CdbAshOverallController:
    
    def __init__(self, ash_overall_service: CdbAshOverallService):
        self._service = ash_overall_service
    
    
    async def get_ash_overall_table(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_object_metric(request.metric_type, 
                                                                         request.customer_code, 
                                                                         request.dbid, request.begin_snap, request.end_snap)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Table", "x_axis":"ObjectName", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def get_ash_overall_index(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_index(request.customer_code, request.dbid)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Index", "x_axis":"ObjectName", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
        
    async def get_ash_overall_segment(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_segment(request.customer_code, request.dbid)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Table", "x_axis":"ObjectName", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")


    async def get_ash_overall_wait_class(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_wait_class(request.customer_code, request.dbid)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Table", "x_axis":"WaitClass", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")

    async def get_ash_overall_event(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_event(request.customer_code, request.dbid)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Table", "x_axis":"Event", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def get_ash_overall_module(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_module(request.customer_code, request.dbid)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Table", "x_axis":"Module", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def get_ash_overall_program(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_program(request.customer_code, request.dbid)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Table", "x_axis":"Program", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def get_ash_overall_sql_cpu(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_sql_cpu(request.customer_code, request.dbid)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Table", "x_axis":"SqlId", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def get_ash_overall_sql_io(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_sql_io(request.customer_code, request.dbid)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Table", "x_axis":"SqlId", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def get_ash_overall_sql_operation(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_sql_operation(request.customer_code, request.dbid)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Table", "x_axis":"Operation", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def get_ash_overall_wait(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_wait(request.customer_code, request.dbid)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Table", "x_axis":"PdbName", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
    
    async def get_ash_overall_wait_global(self, request: AshOverallRequest):
        try:
            if self._validate_request(request):
                data = await self._service.get_ash_overall_wait_global(request.customer_code, request.dbid)
                if data:
                    chart_model = ChartModel(**{"type": 'pie', "title": "Ash Overall Table", "x_axis":"PdbName", "y_axis": ["Percentage"]})
                    return ChartResponse(**{"chart_model":chart_model, "data": [vars(o) for o in data]})

        except Exception as ex:
            raise HTTPException(status_code=400, detail=f"{ex}")
            

    def _validate_request(self, request: AshOverallRequest):
        if not helper.strNotEmpty(request.customer_code):
            raise HTTPException(status_code=400, detail="Customer code is required")
        if request.dbid is None:
            raise HTTPException(status_code=400, detail="Dbid is required")
        return True