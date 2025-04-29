from enum import Enum


class AwrEnum(Enum):
    
    AWR_REPOSITORY_INFO = 'awr.awr_repository_information'
    AWR_GL_CONFIG = 'awr.awr_gl_config'
    ALL_AWRS_FOR_OUTPUT_HTML = 'awr.get_all_awrs_for_output_html'
    OUTPUT_AWR_TO_HTML = 'awr.get_output_html'
    DROP_AWR = 'awr.drop_awr'    
    AWRS_FOR_HEALTHCHECK = 'awr.awrs_for_healthcheck'
