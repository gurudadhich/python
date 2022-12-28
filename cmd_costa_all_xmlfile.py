import xml.etree.ElementTree as ET
from pathlib import Path
import argparse
import mysql.connector

conn = mysql.connector.connect(user='root',
                               password='4863',
                               host='localhost',
                               database='costa_data')
def costa_fare(dir_path):
    fare_path = dir_path / 'costafare.xml'
    tree = ET.parse(fare_path)
    myroot = tree.getroot()
    cruises = []

    for Destination in myroot.findall('./FareCatalog/Destination'):
        cruise_detail = {}
        # print(Destination.tag)
        # print(Destination.attrib)
        cruise_detail['DestCode'] = Destination.attrib['Code']
        cruise_detail['DestName'] = Destination.attrib['DisplayName']

        for Cruise in Destination:
            cruise_detail['CruiseCode'] = Cruise.attrib['Code']

            for Fares in Cruise:
                for Fare in Fares:
                    cruises.append({**cruise_detail, **Fare.attrib})
                
    for cruise in cruises:
        DestCode = cruise.get('DestCode')
        DestName = cruise.get('DestName')
        CruiseCode = cruise.get('CruiseCode')
        Code = cruise.get('Code')
        FareDescription = cruise.get('FareDescription')

        sql = """INSERT INTO costa_fare (DestCode,DestName,CruiseCode,Code,FareDescription) VALUES (%s,%s,%s,%s,%s)"""
        c = conn.cursor()
        c.execute(sql, (DestCode,DestName,CruiseCode,Code,FareDescription))
        conn.commit()
        print("data inserted successfully")


def costa_itin(dir_path):
    itin_path = dir_path / 'costaitn.xml'
    tree = ET.parse(itin_path)
    myroot = tree.getroot()
    cruises = []
    # print(myroot)
    for Destination in myroot:
        # print(Destination.tag)
        # print(Destination.attrib)
        cruise_detail = {}
        cruise_detail['DestCode'] = Destination.attrib['Code']
        cruise_detail['DestName'] = Destination.attrib['DisplayName']

        for Itinerary in Destination:
            cruise_detail['ItinCode'] = Itinerary.attrib['Code']
            cruise_detail['ItinName'] = Itinerary.attrib['DisplayName']
            for Steps in Itinerary:
                for Step in Steps:
                    cruises.append({**cruise_detail, **Step.attrib})
    for cruise in cruises:
        DestCode = cruise.get('DestCode')
        DestName = cruise.get('DestName')
        ItinCode = cruise.get('ItinCode')
        ItinName = cruise.get('ItinName')
        CodeDeparturePort = cruise.get('CodeDeparturePort')
        DeparturePortDescription = cruise.get('DeparturePortDescription')
        CodeArrivelPort = cruise.get('CodeArrivelPort')
        ArrivelPortDescrption = cruise.get('ArrivelPortDescrption')
        DepartureTime = cruise.get('DepartureTime')
        ArrivalTime = cruise.get('ArrivalTime')
        DepartureDay = cruise.get('DepartureDay')
        ArrivalDay = cruise.get('ArrivalDay')

        sql = """INSERT INTO costa_itinerary (DestCode ,DestName ,ItinCode ,ItinName, CodeDeparturePort ,DeparturePortDescription, CodeArrivelPort, ArrivelPortDescrption ,DepartureTime ,ArrivalTime, DepartureDay ,ArrivalDay) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        c = conn.cursor()
        c.execute(sql, (DestCode, DestName, ItinCode, ItinName, CodeDeparturePort, DeparturePortDescription,
                CodeArrivelPort, ArrivelPortDescrption, DepartureTime, ArrivalTime, DepartureDay, ArrivalDay))
        conn.commit()


def costa_price(dir_path):
    price_path = dir_path / 'costaprice.xml'
    tree = ET.parse(price_path)
    myroot = tree.getroot()
    cruises = []

    for Cruise in myroot.findall('./CruisePriceCatalog/Cruises/Cruise'):
        # print(Cruise.tag, "\n",Cruise.attrib)
        cruise_detail = {}
        cruise_detail['CruiseCode'] = Cruise.attrib['Code']
        cruise_detail['CruiseName'] = Cruise.attrib['DisplayName']

        for Categories in Cruise:
            for Category in Categories:
                cruises.append({**cruise_detail, **Category.attrib})
    for cruise in cruises:
        CruiseCode = cruise.get('CruiseCode')
        CruiseName = cruise.get('CruiseName')
        Code = cruise.get('Code')
        Description = cruise.get('Description')
        Discount  = cruise.get('Discount')
        BestPrice = cruise.get('BestPrice')
        ListPrice = cruise.get('ListPrice')
        CurrencyCode = cruise.get('CurrencyCode')
        MandatoryFlight = cruise.get('MandatoryFlight')
        Availability = cruise.get('Availability')
        HotelMandatory = cruise.get('HotelMandatory')

        sql = '''INSERT INTO costa_price (CruiseCode ,CruiseName, Code ,Description ,Discount , BestPrice ,ListPrice ,CurrencyCode, MandatoryFlight ,Availability ,HotelMandatory) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        c = conn.cursor()
        c.execute(sql, (CruiseCode ,CruiseName, Code ,Description ,Discount , BestPrice ,ListPrice ,CurrencyCode, MandatoryFlight ,Availability ,HotelMandatory))
        conn.commit()
        print("data inserted successfully")



def costa_pricepax(dir_path):
    pricepax_path = dir_path  / 'costapricepax.xml'
    tree = ET.parse(pricepax_path)
    myroot = tree.getroot()
    cruises = []

    for Cruise in myroot.findall('./CruisePriceCatalog/Cruises/Cruise'):
        cruise_detail = {}
        cruise_detail['CruiseCode'] = Cruise.attrib['Code']
        cruise_detail['CruiseName'] = Cruise.attrib['DisplayName']

        for Categories in Cruise:
            for Category in Categories:
                cruises.append({**cruise_detail, **Category.attrib})
    for cruise in cruises:
        CruiseCode = cruise.get('CruiseCode')
        CruiseName = cruise.get('CruiseName')
        Code = cruise.get('Code')
        Description = cruise.get('Description')
        Discount = cruise.get('Discount')
        BestPrice = cruise.get('BestPrice')
        ListPrice = cruise.get('ListPrice')
        FirstAdult = cruise.get('FirstAdult')
        SecondAdult = cruise.get('SecondAdult')
        ThirdAdult = cruise.get('ThirdAdult')
        FourthAdult = cruise.get('FourthAdult')
        ThirdChild = cruise.get('ThirdChild')
        ThirdJunior = cruise.get('ThirdJunior')
        SingleSupplement = cruise.get('SingleSupplement')
        CurrencyCode = cruise.get('CurrencyCode')
        MandatoryFlight = cruise.get('MandatoryFlight')
        Availability = cruise.get('Availability')
        HotelMandatory = cruise.get('HotelMandatory')

        sql = '''INSERT INTO costa_price_pax (CruiseCode, CruiseName, Code, Description ,  Discount ,BestPrice ,ListPrice ,FirstAdult, SecondAdult ,ThirdAdult ,FourthAdult, ThirdChild ,ThirdJunior ,SingleSupplement, CurrencyCode, MandatoryFlight ,Availability ,HotelMandatory) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        c = conn.cursor()
        c.execute(sql, (CruiseCode, CruiseName, Code, Description,  Discount, BestPrice, ListPrice, FirstAdult, SecondAdult, ThirdAdult,
                FourthAdult, ThirdChild, ThirdJunior, SingleSupplement, CurrencyCode, MandatoryFlight, Availability, HotelMandatory))
        conn.commit()
        print("data inserted successfully")


if __name__ == "__main__":
    # using sys module
    # fare_path = sys.argv[1]+'costafare.xml'

    # using argparse module
    parser = argparse.ArgumentParser()
    parser.add_argument("directory_path")
    args = parser.parse_args()
    # print(args.directory_path)

    dir_path = Path(args.directory_path)

    costa_fare(dir_path)
    costa_itin(dir_path)
    costa_price(dir_path)
    costa_pricepax(dir_path)

    print(costa_fare(dir_path))
