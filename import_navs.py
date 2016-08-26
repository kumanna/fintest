import sys
from navserver.models import MutualFund, MutualFundNAV
import datetime, time
import decimal

if len(sys.argv) < 2:
    print("%s <amfinumber> <navfile>")
    sys.exit(1)

with open(sys.argv[2], 'r') as f:
    lines = f.readlines()

# Keep only the required lines
lines = [i for i in lines if i.startswith(sys.argv[1])]

m = MutualFund.objects.get_or_create(amfisymbol=sys.argv[1])[0]

for navline in lines:
    field_list = navline.split(';')
    print('%s, %s' % (field_list[3], field_list[-1].strip()))
    t = time.strptime(field_list[-1].strip(), '%d-%b-%Y')
    entry = m.nav.get_or_create(nav=decimal.Decimal(field_list[3]),
                                date=datetime.date.fromtimestamp(time.mktime(t)))[0]
    entry.save()
m.save()
