import csv
import pip._vendor.colorama
from pip._vendor.colorama import init
init()
f = open('/failingtest_15may.csv')
#f = open('/Users/abajracharya/gitrepo/git_personal/Tutorials/list.csv')
csv_f = csv.reader(f)
header = next(csv_f)
failingTest = []
if header != None:
    for column in csv_f:
        if column[0] == 'AssetDB':
            failingTest.append(column[2])
        else:
            failingTest.append(column[3])
#print (failingTest)
f = open('misconfiguredhosts_15May.csv')
#f = open('/Users/abajracharya/gitrepo/git_personal/Tutorials/list2.csv')
csv_f = csv.reader(f)
header = next(csv_f)
misconfiguredHost = []
if header != None:
    for column in csv_f:
        if column[0] == 'AssetDB':
            misconfiguredHost.append(column[2])
        else:
            misconfiguredHost.append(column[3])
#print (misconfiguredHost)
f.close()
failingTest = set(failingTest)
misconfiguredHost = set(misconfiguredHost)
from pip._vendor.colorama import Fore, Back, Style
print (Fore.BLUE + f'{"The number of asset from failing test is:":15} {len(failingTest):16d}')
print (Fore.BLUE + f'{"The number of misconfigured asset is:":15} {len(misconfiguredHost):20d}')
diff = (misconfiguredHost.difference(failingTest))
merged = (misconfiguredHost.union(failingTest))
inter = (misconfiguredHost.intersection(failingTest))
with open ('/Users/abajracharya/gitrepo/arjun-test//python/sources/uniquelist.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(sorted(diff))
#print (diff)
with open ('/Users/abajracharya/gitrepo/arjun-test//python/sources/combinedlist.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(sorted(merged))
with open ('/Users/abajracharya/gitrepo/arjun-test//python/sources/intersectedlist.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(sorted(inter))
print (Fore.GREEN + f'{"the number of distinct or unique asset is:":10} {len(diff):15d}')
print (Fore.GREEN + f'{"the number of merged or combined asset is:":10} {len(merged):15d}')
print (Fore.RED+ f'{"the number of duplicate or intersected asset is:":10} {len(inter):9d}')
Style.RESET_ALL
