stri = 'X-DSPAM-Confidence:0.8475'

float_loc = stri.find(":")

float_raw = stri[float_loc+1:]

confidence = float(float_raw.strip())

print("Confidence:" + str(confidence))

