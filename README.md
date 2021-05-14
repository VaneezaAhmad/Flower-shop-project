# Flower Shop Location Recommendation Using Yelp API

## Goal
To assess the viability of opening a Flower-shop either in the Leesburg, VA or Silver Spring, MD area.


## Analysis

Locations of all flower shops within a 5-mile radius of each respective city were plotted using Folium.
The flower shops pulled by the Yelp API are not representative of simply the location of the business 
but also what area the particular business serve

![alt text](https://github.com/VaneezaAhmad/Flower-shop-project/blob/main/Images/map.jpg)

Next an analysis of how flower shops are rated in each area was done. Represented clearly in the graph is the fact that shops in the Silver Spring area have a larger variety of ratings while in the Leesburg area, shops bottom out at 3.5 stars. 

![alt text](https://github.com/VaneezaAhmad/Flower-shop-project/blob/main/Images/ss_bar.png)
![alt text](https://github.com/VaneezaAhmad/Flower-shop-project/blob/main/Images/lb_bar.png)

Regarding a connection between a shop’s rating and its review count. We found that there is a very weak correlation between the two. So weak in fact that we would not advise one to worry about garnering a lot of reviews but rather quality reviews. 

![alt text](https://github.com/VaneezaAhmad/Flower-shop-project/blob/main/Images/ss_scatter.png)
![alt text](https://github.com/VaneezaAhmad/Flower-shop-project/blob/main/Images/lb_scatter.png)

Lastly, demographic data on flower buyers pulled through Numerator and demographic data pulled through the US Census gave us a better understanding of who best fits our target profile. When it comes to age, persons over 65 are the most likely to purchase flowers and Silver Spring has the higher proportion. When it comes to race, Asians are by and large more Riley to purchase flowers followed by hispanics. Leesburg has the higher Asian population and Silver Spring has the higher Hispanic population. With regard to income, generally speaking the more money you make the more likely it is that you would purchase flowers. Leesburg has a much higher median household income at $114,444. And finally those with advanced degrees are most likely to purchase flowers. The Census data only displays Bachelor’s and onward though Silver Spring and Leesburg are extremely close.

## Conclusions
Leesburg was chosen as the recommendation for a few reasons. First, there are less flower shops and those shops are spread far apart. While
the shops in Leesburg are generally rated highly, if one were to open shop in the area, it would be unlikely that your competition would be so close as to encroach. Next, Leesburg has a slightly larger Asian population. While it is only slightly larger, it remains significant because that is the biggest indicator of whether one is likely to purchase flowers. Lastly, the second biggest indicator is income. The median income is extremely high in Leesburg making it the obvious choice.

## Authors
[Vaneeza Ahmad](https://github.com/VaneezaAhmad)

[Natnael Tsegaw](https://github.com/ntsegaw)
