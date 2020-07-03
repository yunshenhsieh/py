s="""method: search
searchMethod: true
searchTarget: ATM
orgName: 
orgId: 
hid_1: 1
tenderName: 
tenderId: 
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 109/05/30
awardAnnounceEndDate: 109/05/30
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: gg
hid_2: 1
gottenVendorName: ggg
gottenVendorId: 
hid_3: 1
submitVendorName: ree
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢"""

data = {}
for r in s.split('\n'):
    data[r.split(':')[0]] = r.split(':')[1]

print(data)