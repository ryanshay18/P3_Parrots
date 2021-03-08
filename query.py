import sqlite3
import json

# https://collegescorecard.ed.gov/data/documentation/

conn = sqlite3.connect('schools.db')

crs = conn.cursor()

# def construct_query(region, locale)

for row in conn.execute("select name, city, state, url, locale, carnegie_basic from schools where city in ('Denver', 'Aurora') and carnegie_basic < 12"):
  print(row)


def where_locale(answer):
    print(answer)
    # Answer(1, "City (Population: over 250,000)"),
    #  Answer(2, "Suburb (Population: 100,000 - 250,000)"),
    #  Answer(3, "Town (cluster 10 - 35 miles away from urban area)"),
    #  Answer(4, "Rural (5 - 25 miles away from urban area)")]),
    if answer == "1":
        return "locale >= 11 and locale <= 13"
    if answer == "2":
        return "locale >= 21 and locale <= 23"
    if answer == "3":
        return "locale >= 31 and locale <= 33"
    if answer == "4":
        return "locale >= 41 and locale <= 43"


def where_state(answer):
   # Answer(1, "New England (CT, ME, MA, NH, RI, VT)"),
   # Answer(2, "Mid East (DE, DC, MD, NJ, NY, PA)"),
   # Answer(3, "Great Lakes (IL, IN, MI, OH, WI)"),
   # Answer(4, "Plains (IA, KS, MN, MO, NE, ND, SD)"),
   # Answer(5, "Southeast (AL, AR, FL, GA, KY, LA, MS, NC, SC, TN, VA, WV)"),
   # Answer(6, "Southwest (AZ, NM, OK, TX)"),
   # Answer(7, "Rocky Mountains (CO, ID, MT, UT, WY)"),
   # Answer(8, "Outlying Areas (AS, FM, GU, MH, MP, PR, PW, VI)")]),
    if answer == "1":
        return "state in ('CT', 'ME', 'MA', 'NH', 'RI', 'VT')"
    if answer == "4":
        return "state in ('IA', 'KS', 'MN', 'MO', 'NE', 'ND', 'SD')"
    # TODO: finish other regions
    return ""


def where_carnegie_basic(answer):
    #  Answer(1, "Associates Degree"),
    #  Answer(2, "Doctorate"),
    #  Answer(3, "Master's Degree"),
    #  Answer(4, "Bachelor's Degree"),
    #  Answer(5, "2 Year / 4 Year Special Focus")]),
    if answer == "1":
        return "carnegie_basic >= 1 and carnegie_basic <= 9"
    if answer == "2":
        return "carnegie_basic >= 15 and carnegie_basic <= 17"
    if answer == "3":
        return "carnegie_basic >= 18 and carnegie_basic <= 20"
    if answer == "4":
        return "carnegie_basic >= 21 and carnegie_basic <= 23"
    if answer == "5":
        return "(carnegie_basic >= 10 and carnegie_basic <= 13) or" \
               " (carnegie_basic >= 24 and carnegie_basic <= 32)"
    return ""


def query_colleges(answers):
    conn = sqlite3.connect('schools.db')
    answers_json = json.loads(answers)
    print(answers_json)
    where = where_locale(answers_json['0']) + " and " + \
            where_state(answers_json['1']) + " and " + \
            where_carnegie_basic(answers_json['4'])
    query = "select name, city, state, url, ownership from schools" \
            " where " + where
    print(query)
    result = []
    for row in conn.execute(query):
        # print(row)
        result.append(row)

    return result
