from ReportType import ReportType

if __name__ == '__main__':
	rt = ReportType()
	rt.set_report_type('aarp')
	print('The type is : ', rt.get_report_type())
    # print 'Subclass:', issubclass(RegisteredImplementation, PluginBase)
    # print 'Instance:', isinstance(RegisteredImplementation(), PluginBase)
