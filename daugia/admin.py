from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(MemberFee)
admin.site.register(MemberFeeLog)

admin.site.register(BidderUser)
admin.site.register(AuctionUser)

admin.site.register(Status)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SessionDate)
admin.site.register(SessionTime)

admin.site.register(Product)
admin.site.register(AuctedProduct)
admin.site.register(Result)

admin.site.register(Payment)
admin.site.register(Participant)
admin.site.register(SendFeedback)
