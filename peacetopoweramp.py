import json

if __name__ == "__main__":
    f = open("preset.peace", "r")
    d = open("preset.json", "w")
    freqs = []
    gains = []
    q = []
    inFrequencies = False
    inGains = False
    inQ = False
    for line in f:
        if line == "[Frequencies]\n":
            inFrequencies = True
        elif inFrequencies and line != "[Gains]\n":
            freqs.append(line.split("=")[1])
        elif line == "[Gains]\n":
            inFrequencies = False
            inGains = True
        elif inGains and line != "[Qualities]\n":
            gains.append(line.split("=")[1])
        elif line == "[Qualities]\n":
            inGains = False
            inQ = True
        elif inQ and line != "[Filters]\n":
            q.append(line.split("=")[1])
        else:
            pass
        
    destDict = {
        "name" : "MyPreset",
        "preamp" : 0,
        "parametric" : True,
        "bands" : []
    }

    for i in range(len(freqs)):
        destDict["bands"].append({
            "type" : 3,
            "channels" : 0,
            "frequency" : freqs[i],
            "q" : q[i],
            "gain" : gains[i],
            "color" : 0
        })

    destString = "[" + json.dumps(destDict, indent=4) + "]"

    d.write(destString)

    f.close()
    d.close()