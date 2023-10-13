#Program to convert minutes to format (_ hours, _minutes)

M = int(raw_input("Enter minutes:"))

HRS = M // 60
MNS = M % 60
print HRS, "hours,", MNS, "minutes"
