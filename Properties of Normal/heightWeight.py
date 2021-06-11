import pandas as pd
import statistics 
import csv
import plotly.figure_factory as ff

df=pd.read_csv("height-weight.csv")
height=df["Height(Inches)"].to_list()
weight=df["Weight(Pounds)"].to_list()
heightmean=statistics.mean(height)
weightmean=statistics.mean(weight)
heightmode=statistics.mode(height)
weightmode=statistics.mode(weight)
heightmedian=statistics.median(height)
weightmedian=statistics.median(weight)
print("mean,median and mode of height is {}, {}, and {} respectively".format(heightmean,heightmedian,heightmode))
print("mean,median and mode of weight is {}, {}, and {} respectively".format(weightmean,weightmedian,weightmode))
fig=ff.create_distplot([height],["height"],show_hist=False)
fig.show()
fig2=ff.create_distplot([weight],["weight"],show_hist=False)
fig2.show()
heightstdev=statistics.stdev(height)
weightstdev=statistics.stdev(weight)
print("standard devation of height is {}".format(heightstdev))
print("standard devation of weight is {}".format(weightstdev))
hfirst_stdStart, hfirst_stdEnd= heightmean-heightstdev,heightmean+heightstdev
hsecond_stdStart, hsecond_stdEnd= heightmean-(2*heightstdev), heightmean+(2*heightstdev)
hthird_stdStart, hthird_stdEnd= heightmean-(3*heightstdev), heightmean+(3*heightstdev)
wfirst_stdStart, wfirst_stdEnd= weightmean-weightstdev, weightmean+weightstdev
wsecond_stdStart, wsecond_stdEnd= weightmean-(2*weightstdev), weightmean+(2*weightstdev)
wthird_stdStart, wthird_stdEnd= weightmean-(3*weightstdev), weightmean+(3*weightstdev)

heightDataWithinFirst_std=[result for result in height if result > hfirst_stdStart and result < hfirst_stdEnd]
heightDataWithinSecond_std=[result for result in height if result > hsecond_stdStart and result < hsecond_stdEnd]
heightDataWithinThird_std=[result for result in height if result > hthird_stdStart and result < hthird_stdEnd]
weightDataWithinFirst_std=[result for result in weight if result > wfirst_stdStart and result < wfirst_stdEnd]
weightDataWithinSecond_std=[result for result in weight if result > wsecond_stdStart and result < wsecond_stdEnd]
weightDataWithinThird_std=[result for result in weight if result > wthird_stdStart and result < wthird_stdEnd]

print("{} % of data for height lies within first standard devation".format(len(heightDataWithinFirst_std)*100/len(height)))
print("{} % of data for height lies within second standard devation".format(len(heightDataWithinSecond_std)*100/len(height)))
print("{} % of data for height lies within third standard devation".format(len(heightDataWithinThird_std)*100/len(height)))
print("{} % of data for weight lies within first standard devation".format(len(weightDataWithinFirst_std)*100/len(weight)))
print("{} % of data for weight lies within second standard devation".format(len(weightDataWithinSecond_std)*100/len(weight)))
print("{} % of data for weight lies within third standard devation".format(len(weightDataWithinThird_std)*100/len(weight)))