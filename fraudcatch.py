import json
import sys, argparse

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

def findfraud(NAME):
    with open(NAME + '.json') as f:
        x = json.load(f)
    TotalVotesLost = 0
    for i in range(len(x["data"]["races"][0]["timeseries"])):
        if i != 0 and x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["trumpd"] < x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["trumpd"]:
            if x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["bidenj"] > x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["bidenj"]:
                #  print ("Index : " + str(i) + " Past Index : " + str(i-1))
                #  print (x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["trumpd"] - x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["trumpd"])
                TotalVotesLost += x["data"]["races"][0]["timeseries"][i]["votes"] * x["data"]["races"][0]["timeseries"][i]["vote_shares"]["trumpd"] - x["data"]["races"][0]["timeseries"][i-1]["votes"] * x["data"]["races"][0]["timeseries"][i-1]["vote_shares"]["trumpd"]
    print(NAME.capitalize() + ": " + str(TotalVotesLost))

def findfraud2(NAME):
    with open(NAME + '.json') as f:
        x = json.load(f)
    TotalVotesLost = 0
    for i in range(len(x["data"]["races"][0]["timeseries"])):
        if i != 0 and x["data"]["races"][0]["timeseries"][i]["votes"] < x["data"]["races"][0]["timeseries"][i-1]["votes"]:
            TotalVotesLost += x["data"]["races"][0]["timeseries"][i]["votes"] - x["data"]["races"][0]["timeseries"][i-1]["votes"]
    print (TotalVotesLost)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--state')
    args = parser.parse_args()
    if args.state:
        findfraud(args.state)
    else:
        for state in sorted(states):
            try:
                findfraud(state.lower())
            except Exception as e:
                print(state + ": " + "No Data")
