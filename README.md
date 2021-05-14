# Sample_Python_Methods

Required: 
* Python 3.9.5
* Modules: lxml, xml, json, getopt, datetime


Example runs:

**** XML ****
$ python3 test_generali.py -P 1 -x 9 -y 10

Usage: test_generali.py -p problem_number -s string -x X -y Y -f file_path (Problem_number: 1-3)
Problem Number: 1 
X: 9 
Y: 10 
1

2021-05-14 01:31:30.951152
<?xml version="1.0" ?>
<QUOTE_REQUEST>
    <REQUEST>
        <AC>
            <AGC>XXX</AGC>
            <AG>YYY</AG>
        </AC>
        <RQ>
            <TY>Q</TY>
            <LAN>EN</LAN>
        </RQ>
        <TP>
            <DEPART>2021-05-23</DEPART>
            <RETURN>2021-05-24</RETURN>
            <ORG>CA</ORG>
            <DES>TEST</DES>
            <V1>302.30</V1>
        </TP>
    </REQUEST>
</QUOTE_REQUEST>

**** JSON ****

$ python3 test_generali.py -P 2 -s dateterm
Usage: test_generali.py -p problem_number -s string -x X -y Y -f file_path (Problem_number: 1-3)
Problem Number: 2 
key pattern to delete: dateterm 
2

{"spreadsheetName": "ABC.xls", "inParams": {"planselect_1": "test11", "retdt": "2019-04-10", "appdate": "2019-04-02", "statecode": "CA", "deptdt": "2019-04-09"}, "outParams": ["dateeff", "coverageresult", "calcdescr", "errorchk", "planresult", "covgsummary", "prem"], "sessionId": null}


$ python3 test_generali.py -P 2 -s outParams
Usage: test_generali.py -p problem_number -s string -x X -y Y -f file_path (Problem_number: 1-3)
Problem Number: 2 
key pattern to delete: outParams 
2

{"spreadsheetName": "ABC.xls", "inParams": {"planselect_1": "test11", "retdt": "2019-04-10", "appdate": "2019-04-02", "statecode": "CA", "deptdt": "2019-04-09"}, "sessionId": null}



**** JMETER logs ****


$ python3 test_generali.py -P 3 -f ../PYTHON/generali/Updated_Python_exercises_QA_Engr/Jmeter_log1.jtl

Usage: test_generali.py -p problem_number -s string -x X -y Y -f file_path (Problem_number: 1-3)
Problem Number: 3 
JMeter log file_path: ../PYTHON/generali/Updated_Python_exercises_QA_Engr/Jmeter_log1.jtl 
3

Parsing JMeter log file ../PYTHON/generali/Updated_Python_exercises_QA_Engr/Jmeter_log1.jtl
timeStamp, label, responseCode, responseMessage, failureMessage

2021-02-09 06:01:23, Direct_test_Services_QuoteRequest, 504, Gateway Time-out, 

2021-02-09 06:01:23, Internal_Quote_Travel, 504, Gateway Timeout, 

2021-02-09 06:01:30, Proxy_test_Services_QuoteRequest, 504, Gateway Timeout, 

2021-02-09 06:02:55, Proxy_test_Services_QuoteRequest, 504, Gateway Timeout, 

2021-02-09 06:03:04, Internal_Quote_Travel, 504, Gateway Timeout, 
