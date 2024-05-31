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

    destString = "[{\n\"name\": \"MyPreset\",\n\"preamp\":0,\n\"parametric\": true,\n\"bands\": ["
    for i in range(len(freqs)):
        destString += "{\n\"type\": 3,\n\"channels\":0,\n\"frequency\": " + freqs[i] + ", \n\"q\":" + q[i] + ",\n\"gain\": " + gains[i] +",\n\"color\": 0},"
    
    destString = destString[:-1]
    destString += "]}]"

    d.write(destString)

    f.close()
    d.close()