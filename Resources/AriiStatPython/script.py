try:
    import pip
    import sys
    import numpy
    import matplotlib
    import pandas as pd
    from AriiStat import *
except ImportError as e:
    print e
    #print "I/O error({0}): {1}".format(e.errno, e.strerror)



#Pour connaitre les librairies installe
def print1():
    installed_packages = pip.get_installed_distributions()
    installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
    for i in installed_packages])
    print(installed_packages_list)

def writeXML(file, xmlstr):
    try:
        f = open(file, 'w')
        f.write(xmlstr)
        f.close()
    except Exception, e:
        print e


try:
    #print1();
    pd.DataFrame();
    name = str(sys.argv[1]);
    spooler = str(sys.argv[2]);
    start = str(sys.argv[3]);
    end = str(sys.argv[4]);

    #name = "ACV/check_open_event_0_AID_M001DWSCOACV"
    #spooler = "jsapp"
    #start = "2016-04-10"
    #end = "2016-05-10"

    #Description
    df = create_dataframe(name, spooler, config1);
    #print df;
    df = filter_date(df, start, end);
    xml = dfDescribe2xml(df.describe());
    writeXML('../views/tempChart/gridStat.xml.twig', xml);
    #print xml;

    #Anomalies potentielles
    tmp = anomalyByDate(df, start, end)
    xml = df2xml(tmp)
    writeXML('../views/tempChart/anoStat.xml.twig', xml);
    #print xml

    #lineChart temps moyen et nombre d'Anomalies potentielles
    tmp = study_frame(df, jsapp);
    json = df2json(tmp)
    writeXML('../views/tempChart/lineChart.json.twig', json);
    #print json


    #PieCHart


    #boxplot

except Exception, e:
    xml = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><rows><row><cell>ERROR</cell></row></rows>";
    writeXML('../views/tempChart/anoStat.xml.twig', xml);
    writeXML('../views/tempChart/gridStat.xml.twig', xml);
    print e
