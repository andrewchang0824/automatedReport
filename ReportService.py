from interfaces.ReportServiceInterface import ReportServiceInterface
from QueryStrategyFactory import QueryStrategyFactory
from BuilderStrategyFactory import BuilderStrategyFactory
from SenderStrategyFactory import SenderStrategyFactory
from errors.BusinessErrorException import BusinessErrorException
from errors.ValidationException import ValidationException


class ReportService(ReportServiceInterface):
    """ Implementation of ReportServiceInterface"""

    def send_report(self, reportTypeInterface):
        try:
            # query
            queryStrategyFactory = QueryStrategyFactory()
            queryStrategy = queryStrategyFactory.get_query_strategy(reportTypeInterface)
            dBUtil = DBUtil()
            queryResult = queryStrategy.query(dBUtil)
            # builder
            builderStrategyFactory = BuilderStrategyFactory()
            builderStrategy = builderStrategyFactory.get_builder_strategy(reportTypeInterface)
            excelUtil = ExcelUtil()
            filePath = builderStrategy.build(queryResult, excelUtil)
            # sender
            senderStrategyFactory = SenderStrategyFactory()
            senderStrategy = senderStrategyFactory.get_sender_strategy(reportTypeInterface)
            emailUtil = EmailUtil()
            senderStrategy.build(filePath, emailUtil)
        except ValidationException as ve:
            print("error : ", ve)
        except BusinessErrorException as bee:
            print("error : ", bee)


ReportServiceInterface.register(ReportService)
