class sales_channel(object):
    def __init__(self):
        oulet : str
        dvision : str
        country : str
        eff_date : str

west = sales_channel()
west.outlet = "one"
west.division = "west"
west.country = "usa"
west.eff_date = "20201010"

print(west)

est = sales_channel()
est.outlet = "two"
est.division = "est"
est.country = "usa"
est.eff_date = "20201010"

print(est.country)

class cml:
    def update(self,s1:sales_channel):
        s1.country = "uk"

c = cml()
c.update(est)

print(est.country)

