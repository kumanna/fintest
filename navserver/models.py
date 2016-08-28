from django.db import models

class MutualFund(models.Model):
    amfisymbol = models.CharField(max_length=10, unique=True)
    mfname = models.CharField(max_length=300,default='Unnamed MF')

    def __str__(self):
        return self.amfisymbol

class MutualFundNAV(models.Model):
    mf = models.ForeignKey(MutualFund, related_name="nav", on_delete=models.CASCADE)
    date = models.DateField(db_index=True)
    nav = models.DecimalField(max_digits=20,decimal_places=6)

    def __str__(self):
        return "%s, %s, %s" % (self.mf.amfisymbol, str(self.date), str(self.nav))
