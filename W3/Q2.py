imp = {'s_0':1}
es = {'s_0':1}
dt = .05
for t in range(1,6):
    imp['s_' + str(t)] = imp['s_' + str(t - 1)] / (1 + 10 * dt)
    es['s_' + str(t)] = es['s_' + str(t - 1)] * (1 - 10 * dt)

print(round(es['s_4'], 7))
print(round(imp['s_4'], 7))

imp = {'s_0':1}
es = {'s_0':1}
dt = .1
for t in range(1,6):
    imp['s_' + str(t)] = imp['s_' + str(t - 1)] / (1 + 10 * dt)
    es['s_' + str(t)] = es['s_' + str(t - 1)] * (1 - 10 * dt)

print(round(es['s_4'], 7))
print(round(imp['s_4'], 7))

imp = {'s_0':1}
es = {'s_0':1}
dt = .2
for t in range(1,6):
    imp['s_' + str(t)] = imp['s_' + str(t - 1)] / (1 + 10 * dt)
    es['s_' + str(t)] = es['s_' + str(t - 1)] * (1 - 10 * dt)

print(round(es['s_4'], 7))
print(round(imp['s_4'], 7))

imp = {'s_0':1}
es = {'s_0':1}
dt = .25
for t in range(1,6):
    imp['s_' + str(t)] = imp['s_' + str(t - 1)] / (1 + 10 * dt)
    es['s_' + str(t)] = es['s_' + str(t - 1)] * (1 - 10 * dt)

print(round(es['s_4'], 7))
print(round(imp['s_4'], 7))


imp = {'s_0':1}
es = {'s_0':1}
dt = .2
for t in range(1,16):
    imp['s_' + str(t)] = imp['s_' + str(t - 1)] / (1 + 10 * dt)
    es['s_' + str(t)] = es['s_' + str(t - 1)] * (1 - 10 * dt)

print(es)
#print(es)

