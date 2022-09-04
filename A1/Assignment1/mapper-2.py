#!/usr/bin/env python3
import sys
import simplejson as json
 
def main():
 
    # loop through each line of stdin
    for line in sys.stdin:
        try:
 
            # parse the incoming json 
            j = json.loads(line.strip())
 
            # initialize output structure
            output = dict()
 
            # and any other useful information from input json
            output["timestamp"] = j["timestamp"]
            output["location"]  = j["location"]
            output["SensorID"]  = j["sensor_id"]
            output["pressure"]  = j["pressure"]
            output["humidity"]  = j["humidity"]
            output["temperature"]  = j["temperature"]
            
        except Exception as e:
            sys.stderr.write("unable to read log: %s" % e)
            continue
 
        try:
            if output["location"]>1700 and output["location"]<2500 and output["SensorID"]<5000 and output["pressure"]>=93500 and output["humidity"]>=72 and output["temperature"]>=12:
            
                print(output["timestamp"],1)
 
            # generate json output
                output_json = json.dumps(output)
 
        except Exception as e:
            sys.stderr.write("unable to write mapper output: %s" % e)
            continue
 
 
if __name__ == "__main__":
        main()
